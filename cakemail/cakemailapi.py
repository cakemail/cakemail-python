import time

import cakemail_openapi
from cakemail.token import Token
from cakemail_openapi import ApiClient
from cakemail_openapi import TokenApi, Configuration


class CakemailApi:
    api_client = None
    config = None
    _token: Token = None

    account: cakemail_openapi.AccountApi
    campaign: cakemail_openapi.CampaignApi
    contact: cakemail_openapi.ContactApi
    custom_attribute: cakemail_openapi.CustomAttributeApi
    domain: cakemail_openapi.DomainApi
    form: cakemail_openapi.FormApi
    list: cakemail_openapi.ListApi
    log: cakemail_openapi.LogApi
    logo: cakemail_openapi.LogoApi
    report: cakemail_openapi.ReportApi
    segment: cakemail_openapi.SegmentApi
    sender: cakemail_openapi.SenderApi
    sub_account: cakemail_openapi.SubAccountApi
    suppressed_email: cakemail_openapi.SuppressedEmailApi
    test_email: cakemail_openapi.TestEmailApi
    token: cakemail_openapi.TokenApi
    transactional_email: cakemail_openapi.TransactionalEmailApi
    user: cakemail_openapi.UserApi

    def __init__(self, username, password):
        self.config = Configuration(host='https://api.cakemail.dev')
        self.api_client = ApiClient(self.config)
        self._token = Token(
            email=username,
            password=password,
            token_api=TokenApi(self.api_client),
            configuration=self.config
        )

        for api in [api for api in dir(cakemail_openapi) if
                    api.endswith('Api')]:
            setattr(
                self,
                ''.join(['_' + i.lower() if i.isupper() else i for i in
                         api.split('Api')[0]]).lstrip('_'),
                getattr(cakemail_openapi, api)(self.api_client)
            )

    def __getattribute__(self, name):
        """ Refresh the token if expired """
        if name not in ['api_client', 'config', '_token']:
            if self._token.expires_at < time.time():
                self._token.refresh()

        return super(CakemailApi, self).__getattribute__(name)
