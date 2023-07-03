import json

from email_managers import ConfirmRegistrationEmailSender
from email_managers import ResetPasswordEmailSender

from log import get_logger

from enums import EmailTypeEnum

logger = get_logger(__name__)


def send_email(ch, method, properties, body):
    # get body from queue_service msg
    email_data = json.loads(body.decode())

    # get data from body
    to_email: str = email_data.get('email', None)
    content: str = email_data.get('content', None)
    emailType: EmailTypeEnum = email_data.get('emailType', None)


    logger.debug(f"Email sending... TO:`{to_email}`, REASON: `{emailType}`, CONTENT=`{content}`")
    if to_email is not None and content is not None and emailType is not None:

        if emailType == EmailTypeEnum.REGISTRATION:
            # send email for registration confirm
            is_successfully_sent: bool = ConfirmRegistrationEmailSender.send(
                to_email=to_email,
                confirmation_link=content,
            )
            if is_successfully_sent:
                # mark message as processed
                ch.basic_ack(delivery_tag=method.delivery_tag)
            else:
                logger.error(f"Message doesn't send to `{to_email}`!\n {email_data}")
        elif emailType == EmailTypeEnum.RESTORE_ACCESS:
            # send email with new password
            is_successfully_sent: bool = ResetPasswordEmailSender.send(
                to_email=to_email,
                new_psw=content,
            )
            if is_successfully_sent:
                # mark message as processed
                ch.basic_ack(delivery_tag=method.delivery_tag)
            else:
                logger.error(f"Message doesn't send to `{to_email}`!\n {email_data}")
    else:
        logger.error(f"Bad message format! {email_data}")
