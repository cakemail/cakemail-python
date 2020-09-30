from cakemail_openapi import DomainApi


class Domain:
    def __init__(self, api):
        self.__api = DomainApi(api)
        self.update = self.__api.patch_domains
        self.show = self.__api.show_domains
        self.validate = self.__api.validate_domains

    update: DomainApi.patch_domains
    show: DomainApi.show_domains
    validate: DomainApi.validate_domains
