# https://www.justintodata.com/send-email-using-python-tutorial/
import datetime as dt
import logging
import my_secrets
import smtplib

from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logging import Logger

now: datetime = dt.datetime.now()
todays_date: str = now.strftime('%D').replace('/', '-')

email_reciever: list[str] = my_secrets.email_to
email_sender: str = my_secrets.postfix_mail_from
mail_server = my_secrets.postfix_mailhost
email_user = my_secrets.postfix_user
email_password = my_secrets.postfix_password


def send_mail(subject: str, attachment_path: object = None):
    """ Takes a subject (str) and optional file attachment
        Sends email to receiver_email contacts
    """
    logger: Logger = logging.getLogger(__name__)
    sender_email: str = email_sender
    receiver_email: list[str] = email_reciever

    msg: MIMEMultipart = MIMEMultipart("alternative")
    msg["Subject"]: str = f"{subject}"
    msg["From"]: str = sender_email
    msg["To"]: str = receiver_email[0]

    if attachment_path:
        html_attachments: str = """\
          <html>
            <body>
              <p><b>Python Selenium Tests Report</b></p>
              <br>
              <p>Please find the test results report attached.</p>
              <br>
              <p>Visit below for more information</p>
              <a href="https://tascs.locaL">TASCS - HOA</a>       
            </body>
          </html>
          """
        with open(attachment_path, "rb") as attachment:
            html: MIMEText = MIMEText(html_attachments, "html")
            part_attachments: MIMEBase = MIMEBase("application", "octet-stream")
            part_attachments.set_payload(attachment.read())
            encoders.encode_base64(part_attachments)
            part_attachments.add_header(
                "Content-Disposition",
                "attachment",
                filename=attachment_path
            )
            msg.attach(part_attachments)
            msg.attach(html)
    else:
        html_basic: str = """\
            <html>
              <body>
                <p><b>Python Report Mailer</b>
                <br>
                   Visit <a href="https://roadspies.tascs.test">ROADSPIES</a> 
                   for more information.
                </p>
              </body>
            </html>
            """
        part_basic: MIMEText = MIMEText(html_basic, "html")
        msg.attach(part_basic)

    with smtplib.SMTP(my_secrets.postfix_mailhost, 25) as server:
        try:
            server.sendmail(sender_email, receiver_email, msg.as_string())
            logger.info("email sent")
        except smtplib.SMTPException as e:
            logger.exception(f"email not sent {str(e)}")

    # #################################### SSL TESTING
    # context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)   # ssl.create_default_context
    # context.set_ciphers('TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384')        #("TLS_RSA_WITH_AES_128_CBC_SHA256")     # ("TLS_DHE_RSA_WITH_AES_128_GCM_SHA256")
    # context.hostname_checks_common_name = False
    # context.check_hostname = False
    # context.verify_mode = ssl.CERT_NONE
    # ser_cert = ssl.get_server_certificate(my_secrets.exchange_mailhost, 25)
#     context.load_default_certs()
#     ca = context.get_ca_certs()
#     c = context.get_ciphers()
#     ciphers = list({x['name'] for x in c})
#     # print(ciphers)
#     # print(ca)
#     for c in ca:
#         sub = c.get('subject')
#         org = sub[1]
#         for o in org:
#             for p in o:
#                 print(p, type(p))
#         # for d in c:
#         #     print(d)
#         #     print(type(d))
#     try:
#         with smtplib.SMTP_SSL(my_secrets.exchange_mailhost, 587, context=context) as server:
#             server.login(my_secrets.exchange_user, my_secrets.exchange_password)  # NTLM issue? wrong version issue .997?
#             server.ehlo("tascslt")
#             server.starttls()
#             server.sendmail(my_secrets.mail_from, receiver_email, msg.as_string())
#
#     except smtplib.SMTPException as e:
#         print("SMTPERROR",e)
#     except ssl.SSLError as e:
#         print("SSLError", str(e))
#     except ssl.ALERT_DESCRIPTION_HANDSHAKE_FAILURE as e:
#         print(e)
#     except ssl.SSLCertVerificationError as e:
#         print(e)
#
# send_mail("hello, NON TLS test to rpi4 on port 25. Shows no date!?")
