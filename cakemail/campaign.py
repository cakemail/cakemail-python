from cakemail_openapi import CampaignApi


class Campaign:
    def __init__(self, api):
        self.__api = CampaignApi(api)
        self.archive = self.__api.archive_campaign
        self.cancel = self.__api.cancel_campaign
        self.create = self.__api.create_campaign
        self.delete = self.__api.delete_campaign
        self.get = self.__api.get_campaign
        self.list = self.__api.list_campaigns
        self.list_links = self.__api.list_links
        self.update = self.__api.patch_campaign
        self.render = self.__api.render_campaign
        self.reschedule = self.__api.reschedule_campaign
        self.resume = self.__api.resume_campaign
        self.schedule = self.__api.schedule_campaign
        self.send_test_email = self.__api.send_test_email
        self.suspend = self.__api.suspend_campaign
        self.unarchive = self.__api.unarchive_campaign
        self.unschedule = self.__api.unschedule_campaign

    archive: CampaignApi.archive_campaign
    cancel: CampaignApi.cancel_campaign
    create: CampaignApi.create_campaign
    delete: CampaignApi.delete_campaign
    get: CampaignApi.get_campaign
    list: CampaignApi.list_campaigns
    list_links: CampaignApi.list_links
    update: CampaignApi.patch_campaign
    render: CampaignApi.render_campaign
    reschedule: CampaignApi.reschedule_campaign
    resume: CampaignApi.resume_campaign
    schedule: CampaignApi.schedule_campaign
    send_test_email: CampaignApi.send_test_email
    suspend: CampaignApi.suspend_campaign
    unarchive: CampaignApi.unarchive_campaign
    unschedule: CampaignApi.unschedule_campaign
