from __future__ import print_function

from templates.password_restore import password_restore_template
from templates.reg_confirm import reg_confirm_template

from .base_manager import BaseEmailSender


class ConfirmRegistrationEmailSender(BaseEmailSender):
    @staticmethod
    def get_http_template(**kwargs) -> str:
        return reg_confirm_template.format(**kwargs)

    @staticmethod
    def get_subject() -> str:
        return "Подтверждение регистрации"


class ResetPasswordEmailSender(BaseEmailSender):
    @staticmethod
    def get_http_template(**kwargs) -> str:
        return password_restore_template.format(**kwargs)

    @staticmethod
    def get_subject() -> str:
        return "Восстановление доступа к аккаунту."
