from cakemail_openapi import LogoApi


class Logo:
    def __init__(self, api):
        self.__api = LogoApi(api)
        self.upload_default = self.__api.upload_default_logo

    upload_default: LogoApi.upload_default_logo
