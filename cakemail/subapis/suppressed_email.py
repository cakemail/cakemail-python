from cakemail.wrapper import WrappedApi
from cakemail_openapi import SuppressedEmailApi


class SuppressedEmail(WrappedApi):
    """ SuppressedEmail view of SuppressedEmailApi """
    create: SuppressedEmailApi.create_suppressed_email
    delete: SuppressedEmailApi.delete_suppressed_email
    list: SuppressedEmailApi.list_suppressed_emails
