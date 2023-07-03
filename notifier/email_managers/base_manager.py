from __future__ import print_function

import abc
from pprint import pprint

import sib_api_v3_sdk as sb_api
from core.conf import SENDINBLUE_API_KEY
from log import get_logger
from sib_api_v3_sdk import Configuration, SendSmtpEmail, TransactionalEmailsApi
from sib_api_v3_sdk.rest import ApiException


logger = get_logger(__name__)


class BaseEmailSender(abc.ABC):
    _configuration: Configuration = None
    _api_instance: TransactionalEmailsApi = None

    SENDER: dict = {"email": "teamschedule@gmail.com", "name": "TeamSchedule"}

    @classmethod
    def _configure(cls):
        cls._configuration: Configuration = sb_api.Configuration()
        cls._configuration.api_key['api-key'] = SENDINBLUE_API_KEY

    @classmethod
    def init(cls):
        cls._configure()
        cls._api_instance: TransactionalEmailsApi = sb_api.TransactionalEmailsApi(sb_api.ApiClient(cls._configuration))

    @classmethod
    def _send(cls, send_smtp_email: SendSmtpEmail) -> bool:
        if cls._configuration is None:
            cls.init()
        try:
            api_response = cls._api_instance.send_transac_email(send_smtp_email)
            pprint(api_response)
            return True
        except ApiException as e:
            logger.error("Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e)
            return False

    @classmethod
    def send(cls, to_email: str, **kwargs) -> bool:
        send_smtp_email: SendSmtpEmail = sb_api.SendSmtpEmail(
            subject=cls.get_subject(),
            to=[{"email": to_email, "name": to_email}],
            reply_to=cls.SENDER,
            sender=cls.SENDER,
            html_content=cls.get_http_template(to_name=to_email, **kwargs),
        )
        return cls._send(send_smtp_email)

    @staticmethod
    @abc.abstractmethod
    def get_http_template(**kwargs) -> str:
        pass

    @staticmethod
    @abc.abstractmethod
    def get_subject() -> str:
        pass
