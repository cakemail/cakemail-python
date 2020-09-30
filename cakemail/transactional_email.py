from cakemail_openapi import TransactionalEmailApi


class TransactionalEmail:
    def __init__(self, api):
        self.__api = TransactionalEmailApi(api)
        self.send = self.__api.send_email

    send: TransactionalEmailApi.send_email
