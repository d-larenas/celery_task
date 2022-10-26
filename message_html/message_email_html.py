def message_body(message):
    body_html = f'''
  <tr>
    <th>Status</th>
    <th>date</th>
    <th>time</th>
    <th>Message</th>
  </tr>
  <tr>
    <td>{message["status"]}</td>
    <td>{message["datetime"]["date"]}</td>
    <td>{message["datetime"]["time"]}</td>
    <td>{message["message"]}</td>
  </tr>
'''
    return body_html


def message_header():
    html_header = """<html>
    <head>
    <style>
    table {
      font-family: arial, sans-serif;
      border-collapse: collapse;
      width: 100%;
    }

    td, th {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }

    tr:nth-child(even) {
      background-color: #dddddd;
    }
    </style>
    </head>
    <body><table>"""
    return html_header


def message_footer():
    html_footer = "</table></body></html>"
    return html_footer


def message_html(message):
    header_html = message_header()
    body_html = message_body(message)
    footer_html = message_footer()
    msg_html = f"{header_html} {body_html} {footer_html}"
    return msg_html
