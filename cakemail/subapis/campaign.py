from cakemail.wrapper import WrappedApi
from cakemail_openapi import CampaignApi


class Campaign(WrappedApi):
    """ Campaign view of CampaignApi """
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
    suspend: CampaignApi.suspend_campaign
    unarchive: CampaignApi.unarchive_campaign
    unschedule: CampaignApi.unschedule_campaign
    send_test_email: CampaignApi.send_test_email
