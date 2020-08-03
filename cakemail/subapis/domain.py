from cakemail.wrapper import WrappedApi
from cakemail_openapi import DomainApi


class Domain(WrappedApi):
    """ Domain view of DomainApi """
    patch: DomainApi.patch_domains
    show: DomainApi.show_domains
    validate: DomainApi.validate_domains
