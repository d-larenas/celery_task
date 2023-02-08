from celery_service import celery_app as app
from datetime import datetime, timedelta
import requests
from email.message import EmailMessage
import smtplib
import logging
from celery_service.settings import Setting
from message_html import message_html
from bd import session_factory, SiteAlert, SiteRegister
from sqlalchemy import select
from sqlalchemy.exc import DatabaseError

session = session_factory()

logging.basicConfig(level=logging.INFO)


@app.task
def check_page():
    """Check status of website."""
    try:
        url_list = session.execute(
            select(SiteAlert).where(SiteAlert.enable == True)).scalars()
    except DatabaseError:
        url_list = []
    for url in url_list:
        response = validate_page(url.url_site)
        if response["status"] != 200:
            log = validate_log(response, url)
            report = save_log(response, url, log)
            date_time = report.created
            time = date_time.strftime("%H:%M:%S")
            date = date_time.strftime("%d-%m-%Y")
            response["datetime"] = {"time": time, "date": date}
            if log:
                send_email(response, url)
        else:
            save_log(response, url, False)


def validate_page(url):
    """Valid the page status."""
    try:
        r = requests.get(url)
        status_msg = {"status": r.status_code, "message": r.reason}
        logging.info(msg=status_msg)
        return status_msg
    except requests.exceptions.RequestException as e:
        status_msg = {"status": 500, "message": str(e)}
        logging.info(msg=status_msg)
        return status_msg


def send_email(message, url_page):
    """Send email if status of page is not 200."""
    email_host = Setting.EMAIL_HOST_USER
    email_sent = url_page.message_type.email
    msg_html = message_html(message)
    email = EmailMessage()
    email["From"] = f"Bot check page <{email_host}>"
    email["To"] = email_sent
    email["Subject"] = f"Error {message['status']} - {url_page.url_site}"
    email.set_content(msg_html, subtype="html")
    smtp = smtplib.SMTP_SSL(Setting.EMAIL_HOST, port=Setting.EMAIL_PORT)

    try:
        smtp.login(email_host, Setting.EMAIL_HOST_PASSWORD)
    except smtplib.SMTPAuthenticationError as e:
        logging.error(e)

    try:
        smtp.sendmail(email_host, email_sent, email.as_string())
    except smtplib.SMTPRecipientsRefused as e:
        logging.error(e)
    finally:
        smtp.quit()
        logging.info(msg=f" Email sent {email_sent}")


def validate_log(response, url):
    """Validate if alert is sent."""
    result = False
    datetime_old = datetime.now() - timedelta(minutes=Setting.TASK_VALIDATE_MINUTES)
    get_register = session.execute(
        select(SiteRegister).where(
            SiteRegister.status_code == str(response["status"]),
            SiteRegister.page_id == url.id,
            SiteRegister.created >= datetime_old
        )).scalar()
    if get_register is None:
        result = True
    logging.info(msg=f"alerted - {result}")
    return result


def save_log(response, url, is_alerted):
    """Save obtained report."""
    register = SiteRegister(
        message_error=response["message"],
        status_code=response["status"],
        page_id=url.id,
        is_alerted=is_alerted,
    )
    session.add(register)
    session.commit()
    return register
