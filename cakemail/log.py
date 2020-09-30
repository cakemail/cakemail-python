from cakemail_openapi import LogApi


class Log:
    def __init__(self, api):
        self.__api = LogApi(api)
        self.get_campaign = self.__api.get_campaign_logs
        self.get_email = self.__api.get_email_logs
        self.get_list = self.__api.get_list_logs

    get_campaign: LogApi.get_campaign_logs
    get_email: LogApi.get_email_logs
    get_list: LogApi.get_list_logs
