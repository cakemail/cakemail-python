# coding: utf-8

# flake8: noqa
"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.0.15
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from cakemail_openapi.models.accept_list_policy_response import AcceptListPolicyResponse
from cakemail_openapi.models.account_full_response import AccountFullResponse
from cakemail_openapi.models.account_owner import AccountOwner
from cakemail_openapi.models.account_owner_response import AccountOwnerResponse
from cakemail_openapi.models.account_response import AccountResponse
from cakemail_openapi.models.account_stat_response import AccountStatResponse
from cakemail_openapi.models.account_stats_response import AccountStatsResponse
from cakemail_openapi.models.account_status_response import AccountStatusResponse
from cakemail_openapi.models.account_summary_response import AccountSummaryResponse
from cakemail_openapi.models.accounts_response import AccountsResponse
from cakemail_openapi.models.address import Address
from cakemail_openapi.models.address_response import AddressResponse
from cakemail_openapi.models.archive_campaign_response import ArchiveCampaignResponse
from cakemail_openapi.models.archive_list_response import ArchiveListResponse
from cakemail_openapi.models.audience import Audience
from cakemail_openapi.models.audience_response import AudienceResponse
from cakemail_openapi.models.audience_summary_response import AudienceSummaryResponse
from cakemail_openapi.models.bad_request_message import BadRequestMessage
from cakemail_openapi.models.body_create_token_token_post import BodyCreateTokenTokenPost
from cakemail_openapi.models.body_refresh_token_token_put import BodyRefreshTokenTokenPut
from cakemail_openapi.models.campaign_content import CampaignContent
from cakemail_openapi.models.campaign_content_response import CampaignContentResponse
from cakemail_openapi.models.campaign_full_response import CampaignFullResponse
from cakemail_openapi.models.campaign_link_stats_response import CampaignLinkStatsResponse
from cakemail_openapi.models.campaign_links_stats_response import CampaignLinksStatsResponse
from cakemail_openapi.models.campaign_log_response import CampaignLogResponse
from cakemail_openapi.models.campaign_logs_response import CampaignLogsResponse
from cakemail_openapi.models.campaign_response import CampaignResponse
from cakemail_openapi.models.campaign_stat_response import CampaignStatResponse
from cakemail_openapi.models.campaign_stats_response import CampaignStatsResponse
from cakemail_openapi.models.campaign_status import CampaignStatus
from cakemail_openapi.models.campaign_summary_response import CampaignSummaryResponse
from cakemail_openapi.models.campaign_type import CampaignType
from cakemail_openapi.models.campaigns_response import CampaignsResponse
from cakemail_openapi.models.cancel_campaign_response import CancelCampaignResponse
from cakemail_openapi.models.confirm_sender import ConfirmSender
from cakemail_openapi.models.confirm_sender_response import ConfirmSenderResponse
from cakemail_openapi.models.contact import Contact
from cakemail_openapi.models.contact_full_response import ContactFullResponse
from cakemail_openapi.models.contact_response import ContactResponse
from cakemail_openapi.models.contact_status import ContactStatus
from cakemail_openapi.models.contacts_response import ContactsResponse
from cakemail_openapi.models.content_type import ContentType
from cakemail_openapi.models.content_type_response import ContentTypeResponse
from cakemail_openapi.models.create_account import CreateAccount
from cakemail_openapi.models.create_account_response import CreateAccountResponse
from cakemail_openapi.models.create_attribute_response import CreateAttributeResponse
from cakemail_openapi.models.create_campaign import CreateCampaign
from cakemail_openapi.models.create_campaign_response import CreateCampaignResponse
from cakemail_openapi.models.create_contact_response import CreateContactResponse
from cakemail_openapi.models.create_custom_attribute import CreateCustomAttribute
from cakemail_openapi.models.create_form import CreateForm
from cakemail_openapi.models.create_form_response import CreateFormResponse
from cakemail_openapi.models.create_list_response import CreateListResponse
from cakemail_openapi.models.create_segment_response import CreateSegmentResponse
from cakemail_openapi.models.create_sender import CreateSender
from cakemail_openapi.models.create_sender_response import CreateSenderResponse
from cakemail_openapi.models.create_suppressed_email_response import CreateSuppressedEmailResponse
from cakemail_openapi.models.create_user_response import CreateUserResponse
from cakemail_openapi.models.custom_attribute import CustomAttribute
from cakemail_openapi.models.custom_attribute_full_response import CustomAttributeFullResponse
from cakemail_openapi.models.custom_attribute_response import CustomAttributeResponse
from cakemail_openapi.models.custom_attribute_type import CustomAttributeType
from cakemail_openapi.models.custom_attributes_data_response import CustomAttributesDataResponse
from cakemail_openapi.models.custom_attributes_response import CustomAttributesResponse
from cakemail_openapi.models.delete_account_response import DeleteAccountResponse
from cakemail_openapi.models.delete_campaign_response import DeleteCampaignResponse
from cakemail_openapi.models.delete_contact_response import DeleteContactResponse
from cakemail_openapi.models.delete_custom_attribute_response import DeleteCustomAttributeResponse
from cakemail_openapi.models.delete_form_response import DeleteFormResponse
from cakemail_openapi.models.delete_list_response import DeleteListResponse
from cakemail_openapi.models.delete_segment_response import DeleteSegmentResponse
from cakemail_openapi.models.delete_sender_response import DeleteSenderResponse
from cakemail_openapi.models.delete_suppressed_email_response import DeleteSuppressedEmailResponse
from cakemail_openapi.models.delete_user_response import DeleteUserResponse
from cakemail_openapi.models.domain_instruction_response import DomainInstructionResponse
from cakemail_openapi.models.domains import Domains
from cakemail_openapi.models.domains_full_response import DomainsFullResponse
from cakemail_openapi.models.domains_instruction_response import DomainsInstructionResponse
from cakemail_openapi.models.domains_response import DomainsResponse
from cakemail_openapi.models.email import Email
from cakemail_openapi.models.email_content import EmailContent
from cakemail_openapi.models.email_log_response import EmailLogResponse
from cakemail_openapi.models.email_logs_response import EmailLogsResponse
from cakemail_openapi.models.email_stat_response import EmailStatResponse
from cakemail_openapi.models.email_stats_response import EmailStatsResponse
from cakemail_openapi.models.email_tracking import EmailTracking
from cakemail_openapi.models.encoding import Encoding
from cakemail_openapi.models.encoding_response import EncodingResponse
from cakemail_openapi.models.event_type_response import EventTypeResponse
from cakemail_openapi.models.forgot_my_password import ForgotMyPassword
from cakemail_openapi.models.form import Form
from cakemail_openapi.models.form_content import FormContent
from cakemail_openapi.models.form_content_response import FormContentResponse
from cakemail_openapi.models.form_full_response import FormFullResponse
from cakemail_openapi.models.form_redirections import FormRedirections
from cakemail_openapi.models.form_redirections_response import FormRedirectionsResponse
from cakemail_openapi.models.form_response import FormResponse
from cakemail_openapi.models.form_status import FormStatus
from cakemail_openapi.models.form_urls_response import FormUrlsResponse
from cakemail_openapi.models.forms_response import FormsResponse
from cakemail_openapi.models.http_bad_request_error import HTTPBadRequestError
from cakemail_openapi.models.http_unauthorized_error import HTTPUnauthorizedError
from cakemail_openapi.models.http_validation_error import HTTPValidationError
from cakemail_openapi.models.import_contact_data import ImportContactData
from cakemail_openapi.models.import_contacts import ImportContacts
from cakemail_openapi.models.import_contacts_response import ImportContactsResponse
from cakemail_openapi.models.languages import Languages
from cakemail_openapi.models.link_full_response import LinkFullResponse
from cakemail_openapi.models.links_response import LinksResponse
from cakemail_openapi.models.list import List
from cakemail_openapi.models.list_full_response import ListFullResponse
from cakemail_openapi.models.list_log_response import ListLogResponse
from cakemail_openapi.models.list_logs_response import ListLogsResponse
from cakemail_openapi.models.list_pages_response import ListPagesResponse
from cakemail_openapi.models.list_redirections_response import ListRedirectionsResponse
from cakemail_openapi.models.list_response import ListResponse
from cakemail_openapi.models.list_sender_response import ListSenderResponse
from cakemail_openapi.models.list_stat_response import ListStatResponse
from cakemail_openapi.models.list_stats_response import ListStatsResponse
from cakemail_openapi.models.list_summary_response import ListSummaryResponse
from cakemail_openapi.models.list_webhook_action import ListWebhookAction
from cakemail_openapi.models.list_webhook_response import ListWebhookResponse
from cakemail_openapi.models.lists_response import ListsResponse
from cakemail_openapi.models.log_type import LogType
from cakemail_openapi.models.pagination import Pagination
from cakemail_openapi.models.password_grant_type import PasswordGrantType
from cakemail_openapi.models.patch_account import PatchAccount
from cakemail_openapi.models.patch_campaign import PatchCampaign
from cakemail_openapi.models.patch_campaign_content import PatchCampaignContent
from cakemail_openapi.models.patch_campaign_response import PatchCampaignResponse
from cakemail_openapi.models.patch_contact import PatchContact
from cakemail_openapi.models.patch_contact_response import PatchContactResponse
from cakemail_openapi.models.patch_domains import PatchDomains
from cakemail_openapi.models.patch_domains_response import PatchDomainsResponse
from cakemail_openapi.models.patch_form_response import PatchFormResponse
from cakemail_openapi.models.patch_list_response import PatchListResponse
from cakemail_openapi.models.patch_segment_response import PatchSegmentResponse
from cakemail_openapi.models.patch_self_account import PatchSelfAccount
from cakemail_openapi.models.patch_sender_response import PatchSenderResponse
from cakemail_openapi.models.patch_user import PatchUser
from cakemail_openapi.models.patch_user_response import PatchUserResponse
from cakemail_openapi.models.redirections import Redirections
from cakemail_openapi.models.refresh_grant_type import RefreshGrantType
from cakemail_openapi.models.render_campaign_full_response import RenderCampaignFullResponse
from cakemail_openapi.models.render_campaign_response import RenderCampaignResponse
from cakemail_openapi.models.resend_confirmation_email_response import ResendConfirmationEmailResponse
from cakemail_openapi.models.reset_password_confirm import ResetPasswordConfirm
from cakemail_openapi.models.reset_password_confirm_response import ResetPasswordConfirmResponse
from cakemail_openapi.models.reset_password_response import ResetPasswordResponse
from cakemail_openapi.models.reset_user_password import ResetUserPassword
from cakemail_openapi.models.resume_campaign_response import ResumeCampaignResponse
from cakemail_openapi.models.schedule_campaign import ScheduleCampaign
from cakemail_openapi.models.schedule_campaign_response import ScheduleCampaignResponse
from cakemail_openapi.models.segment import Segment
from cakemail_openapi.models.segment_full_response import SegmentFullResponse
from cakemail_openapi.models.segment_response import SegmentResponse
from cakemail_openapi.models.segments_response import SegmentsResponse
from cakemail_openapi.models.send_email_response import SendEmailResponse
from cakemail_openapi.models.send_test_email import SendTestEmail
from cakemail_openapi.models.send_test_email_response import SendTestEmailResponse
from cakemail_openapi.models.sender import Sender
from cakemail_openapi.models.sender_full_response import SenderFullResponse
from cakemail_openapi.models.sender_response import SenderResponse
from cakemail_openapi.models.senders_response import SendersResponse
from cakemail_openapi.models.suppressed_email import SuppressedEmail
from cakemail_openapi.models.suppressed_email_response import SuppressedEmailResponse
from cakemail_openapi.models.suppressed_emails_response import SuppressedEmailsResponse
from cakemail_openapi.models.suspend_account_response import SuspendAccountResponse
from cakemail_openapi.models.suspend_campaign_response import SuspendCampaignResponse
from cakemail_openapi.models.suspend_user_response import SuspendUserResponse
from cakemail_openapi.models.test_email_type import TestEmailType
from cakemail_openapi.models.token_response import TokenResponse
from cakemail_openapi.models.tracking import Tracking
from cakemail_openapi.models.tracking_response import TrackingResponse
from cakemail_openapi.models.unarchive_list_response import UnarchiveListResponse
from cakemail_openapi.models.unauthorized_message import UnauthorizedMessage
from cakemail_openapi.models.unsubscribe_contact_response import UnsubscribeContactResponse
from cakemail_openapi.models.unsuspend_account_response import UnsuspendAccountResponse
from cakemail_openapi.models.update_list import UpdateList
from cakemail_openapi.models.update_segment import UpdateSegment
from cakemail_openapi.models.update_sender import UpdateSender
from cakemail_openapi.models.upload_logo import UploadLogo
from cakemail_openapi.models.upload_logo_response import UploadLogoResponse
from cakemail_openapi.models.usage_limits import UsageLimits
from cakemail_openapi.models.usage_limits_response import UsageLimitsResponse
from cakemail_openapi.models.user import User
from cakemail_openapi.models.user_full_response import UserFullResponse
from cakemail_openapi.models.user_response import UserResponse
from cakemail_openapi.models.user_summary_response import UserSummaryResponse
from cakemail_openapi.models.users_response import UsersResponse
from cakemail_openapi.models.validate_domains_response import ValidateDomainsResponse
from cakemail_openapi.models.validation_error import ValidationError
from cakemail_openapi.models.webhook import Webhook
