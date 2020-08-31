from cakemail.wrapper import WrappedApi
from cakemail_openapi import SenderApi


class Sender(WrappedApi):
    """ Sender view of SenderApi """
    confirm: SenderApi.confirm_sender
    create: SenderApi.create_sender
    delete: SenderApi.delete_sender
    get: SenderApi.get_sender
    list: SenderApi.list_senders
    resend_confirmation: SenderApi.resend_confirmation_email
    update: SenderApi.patch_sender
