from cakemail.wrapper import WrappedApi
from cakemail_openapi import LogoApi


class Logo(WrappedApi):
    """ Logo view of LogoApi """
    upload_default: LogoApi.upload_default_logo
