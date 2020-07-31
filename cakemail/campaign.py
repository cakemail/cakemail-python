from cakemail.wrapper import WrappedApi
from cakemail_openapi import CampaignApi


class Campaign(WrappedApi):
    list: CampaignApi.list_campaigns
    create: CampaignApi.create_campaign
    get: CampaignApi.get_campaign
    patch: CampaignApi.patch_campaign
    delete: CampaignApi.delete_campaign
    render: CampaignApi.render_campaign
    send_test_email: CampaignApi.send_test_email
    schedule: CampaignApi.schedule_campaign
    unschedule: CampaignApi.unschedule_campaign
    reschedule: CampaignApi.reschedule_campaign
    suspend: CampaignApi.suspend_campaign
    resume: CampaignApi.resume_campaign
    cancel: CampaignApi.cancel_campaign
    archive: CampaignApi.archive_campaign
    unarchive: CampaignApi.unarchive_campaign
    list_links: CampaignApi.list_links
