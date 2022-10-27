from celery_service import celery_app as app
import datetime
import requests
from email.message import EmailMessage
import smtplib
import logging
from celery_service.settings import Setting
from message_html import message_html
from logs import get_log, set_log
import pandas as pd

logging.basicConfig(level=logging.INFO)


@app.task
def check_page():
    """Check status of website."""
    url_list = Setting.TASK_PAGE_LIST
    for url in url_list:
        response = validate_page(url)
        if response["status"] != 200:
            date_time = datetime.datetime.now()
            time = date_time.strftime("%H:%M:%S")
            date = date_time.strftime("%d-%m-%Y")
            response["datetime"] = {"time": time, "date": date}
            log = validate_log(response, url)
            if log is False:
                send_email(response, url)


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
    email_sent = Setting.TASK_DESTINATION_EMAIL
    msg_html = message_html(message)
    email = EmailMessage()
    email["From"] = f"Bot check page <{email_host}>"
    email["To"] = email_sent
    email["Subject"] = f"Error {message['status']} - {url_page}"
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
    """Read and write logs in file json."""
    log_list = get_log()
    set_log(response["datetime"]["date"], response["datetime"]["time"], response["status"], response["message"], url)
    try:
        df = pd.DataFrame(log_list)
        result_filter = df.loc[df["url"] == url].to_dict('records')
    except KeyError:
        result_filter = []
    if result_filter:
        if result_filter[0]["date"] == response["datetime"]["date"]:
            return True
    return False
