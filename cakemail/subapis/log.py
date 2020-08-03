from cakemail.wrapper import WrappedApi
from cakemail_openapi import LogApi


class Log(WrappedApi):
    """ Log view of LogApi """
    get_campaign: LogApi.get_campaign_logs
    get_email: LogApi.get_email_logs
    get_list: LogApi.get_list_logs
