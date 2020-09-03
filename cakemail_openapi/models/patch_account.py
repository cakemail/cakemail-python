# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.0.14
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class PatchAccount(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'address': 'Address',
        'name': 'str',
        'account_owner': 'AccountOwner',
        'fax': 'str',
        'phone': 'str',
        'website': 'str',
        'usage_limits': 'UsageLimits',
        'trial': 'bool',
        'partner': 'bool'
    }

    attribute_map = {
        'address': 'address',
        'name': 'name',
        'account_owner': 'account_owner',
        'fax': 'fax',
        'phone': 'phone',
        'website': 'website',
        'usage_limits': 'usage_limits',
        'trial': 'trial',
        'partner': 'partner'
    }

    def __init__(self, address=None, name=None, account_owner=None, fax=None, phone=None, website=None, usage_limits=None, trial=None, partner=None, local_vars_configuration=None):  # noqa: E501
        """PatchAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._name = None
        self._account_owner = None
        self._fax = None
        self._phone = None
        self._website = None
        self._usage_limits = None
        self._trial = None
        self._partner = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if name is not None:
            self.name = name
        if account_owner is not None:
            self.account_owner = account_owner
        if fax is not None:
            self.fax = fax
        if phone is not None:
            self.phone = phone
        if website is not None:
            self.website = website
        if usage_limits is not None:
            self.usage_limits = usage_limits
        if trial is not None:
            self.trial = trial
        if partner is not None:
            self.partner = partner

    @property
    def address(self):
        """Gets the address of this PatchAccount.  # noqa: E501


        :return: The address of this PatchAccount.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PatchAccount.


        :param address: The address of this PatchAccount.  # noqa: E501
        :type: Address
        """

        self._address = address

    @property
    def name(self):
        """Gets the name of this PatchAccount.  # noqa: E501


        :return: The name of this PatchAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchAccount.


        :param name: The name of this PatchAccount.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def account_owner(self):
        """Gets the account_owner of this PatchAccount.  # noqa: E501


        :return: The account_owner of this PatchAccount.  # noqa: E501
        :rtype: AccountOwner
        """
        return self._account_owner

    @account_owner.setter
    def account_owner(self, account_owner):
        """Sets the account_owner of this PatchAccount.


        :param account_owner: The account_owner of this PatchAccount.  # noqa: E501
        :type: AccountOwner
        """

        self._account_owner = account_owner

    @property
    def fax(self):
        """Gets the fax of this PatchAccount.  # noqa: E501


        :return: The fax of this PatchAccount.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this PatchAccount.


        :param fax: The fax of this PatchAccount.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def phone(self):
        """Gets the phone of this PatchAccount.  # noqa: E501


        :return: The phone of this PatchAccount.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PatchAccount.


        :param phone: The phone of this PatchAccount.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def website(self):
        """Gets the website of this PatchAccount.  # noqa: E501


        :return: The website of this PatchAccount.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this PatchAccount.


        :param website: The website of this PatchAccount.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                website is not None and len(website) > 2083):
            raise ValueError("Invalid value for `website`, length must be less than or equal to `2083`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                website is not None and len(website) < 1):
            raise ValueError("Invalid value for `website`, length must be greater than or equal to `1`")  # noqa: E501

        self._website = website

    @property
    def usage_limits(self):
        """Gets the usage_limits of this PatchAccount.  # noqa: E501


        :return: The usage_limits of this PatchAccount.  # noqa: E501
        :rtype: UsageLimits
        """
        return self._usage_limits

    @usage_limits.setter
    def usage_limits(self, usage_limits):
        """Sets the usage_limits of this PatchAccount.


        :param usage_limits: The usage_limits of this PatchAccount.  # noqa: E501
        :type: UsageLimits
        """

        self._usage_limits = usage_limits

    @property
    def trial(self):
        """Gets the trial of this PatchAccount.  # noqa: E501


        :return: The trial of this PatchAccount.  # noqa: E501
        :rtype: bool
        """
        return self._trial

    @trial.setter
    def trial(self, trial):
        """Sets the trial of this PatchAccount.


        :param trial: The trial of this PatchAccount.  # noqa: E501
        :type: bool
        """

        self._trial = trial

    @property
    def partner(self):
        """Gets the partner of this PatchAccount.  # noqa: E501


        :return: The partner of this PatchAccount.  # noqa: E501
        :rtype: bool
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this PatchAccount.


        :param partner: The partner of this PatchAccount.  # noqa: E501
        :type: bool
        """

        self._partner = partner

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PatchAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchAccount):
            return True

        return self.to_dict() != other.to_dict()
