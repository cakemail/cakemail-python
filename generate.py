from mako.template import Template
from pydantic import BaseModel, validator

import cakemail_openapi


class Method(BaseModel):
    name: str
    super: str

    @validator('name')
    def validate_name(cls, v):
        if v == 'import':
            return 'import_contacts'
        if v == 'patch':
            return 'update'
        if v == 'patch_self':
            return 'update_self'
        if v == 'get_campaign_links':
            return 'get_campaign_link'
        if v == 'get_emails':
            return 'get_email'
        return v


def short(method, suffix):
    if method.endswith(f'_{suffix}'):
        return method.split(f'_{suffix}')[0]
    else:
        return method.split(f'_{suffix}s')[0]


class Api(BaseModel):
    name: str
    suffix: str
    file: str


APIS = [
    Api(name='AccountApi', suffix='account', file='account.py'),
    Api(name='CampaignApi', suffix='campaign', file='campaign.py'),
    Api(name='ContactApi', suffix='contact', file='contact.py'),
    Api(name='CustomAttributeApi', suffix='custom_attribute',
        file='custom_attribute.py'),
    Api(name='DomainApi', suffix='domain', file='domain.py'),
    Api(name='TransactionalEmailApi', suffix='email',
        file='transactional_email.py'),
    Api(name='FormApi', suffix='form', file='form.py'),
    Api(name='ListApi', suffix='list', file='list.py'),
    Api(name='LogApi', suffix='log', file='log.py'),
    Api(name='LogoApi', suffix='logo', file='logo.py'),
    Api(name='SegmentApi', suffix='segment', file='segment.py'),
    Api(name='SenderApi', suffix='sender', file='sender.py'),
    Api(name='ReportApi', suffix='stats', file='report.py'),
    Api(name='SuppressedEmailApi', suffix='suppressed_email',
        file='suppressed_email.py'),
    Api(name='UserApi', suffix='user', file='user.py'),
    Api(name='SubAccountApi', suffix='account', file='sub_account.py'),
]

for api in APIS:
    super_api_class = api.name
    api_class = super_api_class.split('Api')[0]
    api_short = ''.join(['_' + i.lower() if i.isupper() else i for i in
                         api.name.split('Api')[0]]).lstrip('_')
    methods = [
        Method(name=short(method, api.suffix), super=method)
        for method in dir(getattr(cakemail_openapi, api.name))
        if method.endswith(f'_{api.suffix}') or method.endswith(
            f'_{api.suffix}s')
    ]

    with open(f'cakemail/subapis/{api.file}', 'w') as file:
        a = Template(
            filename='customapi.py.mako',
            default_filters=['h']
        ).render(
            super_api_class=super_api_class,
            api_class=api_class,
            methods=methods
        )
        file.write(a)
