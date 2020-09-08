# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.0.15
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class AccountSummaryResponse(object):
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
        'id': 'int',
        'lineage': 'str',
        'status': 'AccountStatusResponse',
        'partner': 'bool',
        'name': 'str',
        'account_owner': 'AccountOwnerResponse',
        'usage_limits': 'UsageLimitsResponse',
        'created_on': 'int'
    }

    attribute_map = {
        'id': 'id',
        'lineage': 'lineage',
        'status': 'status',
        'partner': 'partner',
        'name': 'name',
        'account_owner': 'account_owner',
        'usage_limits': 'usage_limits',
        'created_on': 'created_on'
    }

    def __init__(self, id=None, lineage=None, status=None, partner=None, name=None, account_owner=None, usage_limits=None, created_on=None, local_vars_configuration=None):  # noqa: E501
        """AccountSummaryResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._lineage = None
        self._status = None
        self._partner = None
        self._name = None
        self._account_owner = None
        self._usage_limits = None
        self._created_on = None
        self.discriminator = None

        self.id = id
        self.lineage = lineage
        self.status = status
        self.partner = partner
        if name is not None:
            self.name = name
        self.account_owner = account_owner
        self.usage_limits = usage_limits
        self.created_on = created_on

    @property
    def id(self):
        """Gets the id of this AccountSummaryResponse.  # noqa: E501


        :return: The id of this AccountSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountSummaryResponse.


        :param id: The id of this AccountSummaryResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def lineage(self):
        """Gets the lineage of this AccountSummaryResponse.  # noqa: E501


        :return: The lineage of this AccountSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._lineage

    @lineage.setter
    def lineage(self, lineage):
        """Sets the lineage of this AccountSummaryResponse.


        :param lineage: The lineage of this AccountSummaryResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and lineage is None:  # noqa: E501
            raise ValueError("Invalid value for `lineage`, must not be `None`")  # noqa: E501

        self._lineage = lineage

    @property
    def status(self):
        """Gets the status of this AccountSummaryResponse.  # noqa: E501


        :return: The status of this AccountSummaryResponse.  # noqa: E501
        :rtype: AccountStatusResponse
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountSummaryResponse.


        :param status: The status of this AccountSummaryResponse.  # noqa: E501
        :type: AccountStatusResponse
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def partner(self):
        """Gets the partner of this AccountSummaryResponse.  # noqa: E501


        :return: The partner of this AccountSummaryResponse.  # noqa: E501
        :rtype: bool
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this AccountSummaryResponse.


        :param partner: The partner of this AccountSummaryResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and partner is None:  # noqa: E501
            raise ValueError("Invalid value for `partner`, must not be `None`")  # noqa: E501

        self._partner = partner

    @property
    def name(self):
        """Gets the name of this AccountSummaryResponse.  # noqa: E501


        :return: The name of this AccountSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountSummaryResponse.


        :param name: The name of this AccountSummaryResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def account_owner(self):
        """Gets the account_owner of this AccountSummaryResponse.  # noqa: E501


        :return: The account_owner of this AccountSummaryResponse.  # noqa: E501
        :rtype: AccountOwnerResponse
        """
        return self._account_owner

    @account_owner.setter
    def account_owner(self, account_owner):
        """Sets the account_owner of this AccountSummaryResponse.


        :param account_owner: The account_owner of this AccountSummaryResponse.  # noqa: E501
        :type: AccountOwnerResponse
        """
        if self.local_vars_configuration.client_side_validation and account_owner is None:  # noqa: E501
            raise ValueError("Invalid value for `account_owner`, must not be `None`")  # noqa: E501

        self._account_owner = account_owner

    @property
    def usage_limits(self):
        """Gets the usage_limits of this AccountSummaryResponse.  # noqa: E501


        :return: The usage_limits of this AccountSummaryResponse.  # noqa: E501
        :rtype: UsageLimitsResponse
        """
        return self._usage_limits

    @usage_limits.setter
    def usage_limits(self, usage_limits):
        """Sets the usage_limits of this AccountSummaryResponse.


        :param usage_limits: The usage_limits of this AccountSummaryResponse.  # noqa: E501
        :type: UsageLimitsResponse
        """
        if self.local_vars_configuration.client_side_validation and usage_limits is None:  # noqa: E501
            raise ValueError("Invalid value for `usage_limits`, must not be `None`")  # noqa: E501

        self._usage_limits = usage_limits

    @property
    def created_on(self):
        """Gets the created_on of this AccountSummaryResponse.  # noqa: E501


        :return: The created_on of this AccountSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this AccountSummaryResponse.


        :param created_on: The created_on of this AccountSummaryResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and created_on is None:  # noqa: E501
            raise ValueError("Invalid value for `created_on`, must not be `None`")  # noqa: E501

        self._created_on = created_on

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
        if not isinstance(other, AccountSummaryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountSummaryResponse):
            return True

        return self.to_dict() != other.to_dict()
