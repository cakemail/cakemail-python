import time

from cakemail.token import Token
from cakemail_openapi import AccountApi, SubAccountApi, ApiClient, TokenApi, \
    Configuration, CampaignApi, ContactApi, CustomAttributeApi, DomainApi, \
    FormApi, ListApi, LogApi, LogoApi, ReportApi, UserApi, SegmentApi, \
    SenderApi, SuppressedEmailApi, TransactionalEmailApi
from .subapis.account import Account
from .subapis.campaign import Campaign
from .subapis.contact import Contact
from .subapis.custom_attribute import CustomAttribute
from .subapis.domain import Domain
from .subapis.form import Form
from .subapis.list import List
from .subapis.log import Log
from .subapis.logo import Logo
from .subapis.report import Report
from .subapis.segment import Segment
from .subapis.sender import Sender
from .subapis.sub_account import SubAccount
from .subapis.suppressed_email import SuppressedEmail
from .subapis.transactional_email import TransactionalEmail
from .subapis.user import User


class Api:
    _api_client = None
    _config = None
    _token: Token = None

    account: Account
    sub_account: SubAccount
    campaign: Campaign
    contact: Contact
    custom_attribute: CustomAttribute
    domain: Domain
    form: Form
    list: List
    log: Log
    logo: Logo
    report: Report
    segment: Segment
    sender: Sender
    suppressed_email: SuppressedEmail
    transactional_email: TransactionalEmail
    user: User

    def __init__(self, username, password):
        self._config = Configuration(host='https://api.cakemail.dev')
        self._api_client = ApiClient(self._config)
        self._token = Token(
            email=username,
            password=password,
            token_api=TokenApi(self._api_client),
            configuration=self._config
        )

        self.account = Account(AccountApi(self._api_client), 'account')
        self.sub_account = SubAccount(SubAccountApi(self._api_client),
                                      'account')
        self.campaign = Campaign(CampaignApi(self._api_client), 'campaign')
        self.contact = Contact(ContactApi(self._api_client), 'contact')
        self.custom_attribute = CustomAttribute(
            CustomAttributeApi(self._api_client), 'custom_attribute')
        self.domain = Domain(DomainApi(self._api_client), 'domain')
        self.form = Form(FormApi(self._api_client), 'form')
        self.list = List(ListApi(self._api_client), 'list')
        self.log = Log(LogApi(self._api_client), 'log')
        self.logo = Logo(LogoApi(self._api_client), 'logo')
        self.report = Report(ReportApi(self._api_client), 'report')
        self.segment = Segment(SegmentApi(self._api_client), 'segment')
        self.sender = Sender(SenderApi(self._api_client), 'sender')
        self.suppressed_email = SuppressedEmail(
            SuppressedEmailApi(self._api_client), 'suppressed_email')
        self.transactional_email = TransactionalEmail(
            TransactionalEmailApi(self._api_client), 'email')
        self.user = User(UserApi(self._api_client), 'user')

    def __getattribute__(self, name):
        """ Refresh the token if expired """
        if name not in ['_api_client', '_config', '_token']:
            if self._token.expires_at < time.time():
                self._token.refresh()

        return super(Api, self).__getattribute__(name)
