from cakemail.wrapper import WrappedApi
from cakemail_openapi import ReportApi


class Report(WrappedApi):
    """ Report view of ReportApi """
    get_account: ReportApi.get_account_stats
    get_campaign_link: ReportApi.get_campaign_links_stats
    get_campaign: ReportApi.get_campaign_stats
    get_email: ReportApi.get_emails_stats
    get_list: ReportApi.get_list_stats
    get_self_account: ReportApi.get_self_account_stats
