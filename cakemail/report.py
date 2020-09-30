from cakemail_openapi import ReportApi


class Report:
    def __init__(self, api):
        self.__api = ReportApi(api)
        self.get_account = self.__api.get_account_stats
        self.get_campaign_link = self.__api.get_campaign_links_stats
        self.get_campaign = self.__api.get_campaign_stats
        self.get_email = self.__api.get_emails_stats
        self.get_list = self.__api.get_list_stats
        self.get_self_account = self.__api.get_self_account_stats

    get_account: ReportApi.get_account_stats
    get_campaign_link: ReportApi.get_campaign_links_stats
    get_campaign: ReportApi.get_campaign_stats
    get_email: ReportApi.get_emails_stats
    get_list: ReportApi.get_list_stats
    get_self_account: ReportApi.get_self_account_stats
