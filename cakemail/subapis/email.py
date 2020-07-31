from cakemail.wrapper import WrappedApi
from cakemail_openapi import TransactionalEmailApi


class TransactionalEmail(WrappedApi):
    """ TransactionalEmail view of TransactionalEmailApi """
    send: TransactionalEmailApi.send_email
