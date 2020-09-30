import time

from cakemail_openapi import Configuration, ApiClient, TokenApi
from .token import Token
from .account import Account
from .campaign import Campaign
from .contact import Contact
from .custom_attribute import CustomAttribute
from .domain import Domain
from .transactional_email import TransactionalEmail
from .form import Form
from .list import List
from .log import Log
from .logo import Logo
from .segment import Segment
from .sender import Sender
from .report import Report
from .suppressed_email import SuppressedEmail
from .user import User
from .sub_account import SubAccount
from .template import Template


class Api:
    account: Account
    campaign: Campaign
    contact: Contact
    custom_attribute: CustomAttribute
    domain: Domain
    transactional_email: TransactionalEmail
    form: Form
    list: List
    log: Log
    logo: Logo
    segment: Segment
    sender: Sender
    report: Report
    suppressed_email: SuppressedEmail
    user: User
    sub_account: SubAccount
    template: Template

    def __init__(
            self,
            username,
            password,
            url='https://api.cakemail.dev'
    ):
        self._config = Configuration(host=url)
        self._api_client = ApiClient(self._config)
        self._token = Token(
            email=username,
            password=password,
            token_api=TokenApi(self._api_client),
            configuration=self._config
        )

        self.account = Account(self._api_client)
        self.template = Template(self._api_client)
        self.account = Account(self._api_client)
        self.campaign = Campaign(self._api_client)
        self.contact = Contact(self._api_client)
        self.custom_attribute = CustomAttribute(self._api_client)
        self.domain = Domain(self._api_client)
        self.transactional_email = TransactionalEmail(self._api_client)
        self.form = Form(self._api_client)
        self.list = List(self._api_client)
        self.log = Log(self._api_client)
        self.logo = Logo(self._api_client)
        self.segment = Segment(self._api_client)
        self.sender = Sender(self._api_client)
        self.report = Report(self._api_client)
        self.suppressed_email = SuppressedEmail(self._api_client)
        self.user = User(self._api_client)
        self.sub_account = SubAccount(self._api_client)
        self.template = Template(self._api_client)

    def __getattribute__(self, name):
        if name not in ['_api_client', '_config', '_token']:
            if self._token.expires_at < time.time():
                self._token.refresh()

        return super(Api, self).__getattribute__(name)