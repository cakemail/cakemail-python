# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.0.16
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class UsageLimits(object):
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
        'per_campaign': 'int',
        'per_month': 'int',
        'maximum_contacts': 'int'
    }

    attribute_map = {
        'per_campaign': 'per_campaign',
        'per_month': 'per_month',
        'maximum_contacts': 'maximum_contacts'
    }

    def __init__(self, per_campaign=None, per_month=None, maximum_contacts=None, local_vars_configuration=None):  # noqa: E501
        """UsageLimits - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._per_campaign = None
        self._per_month = None
        self._maximum_contacts = None
        self.discriminator = None

        if per_campaign is not None:
            self.per_campaign = per_campaign
        if per_month is not None:
            self.per_month = per_month
        if maximum_contacts is not None:
            self.maximum_contacts = maximum_contacts

    @property
    def per_campaign(self):
        """Gets the per_campaign of this UsageLimits.  # noqa: E501


        :return: The per_campaign of this UsageLimits.  # noqa: E501
        :rtype: int
        """
        return self._per_campaign

    @per_campaign.setter
    def per_campaign(self, per_campaign):
        """Sets the per_campaign of this UsageLimits.


        :param per_campaign: The per_campaign of this UsageLimits.  # noqa: E501
        :type: int
        """

        self._per_campaign = per_campaign

    @property
    def per_month(self):
        """Gets the per_month of this UsageLimits.  # noqa: E501


        :return: The per_month of this UsageLimits.  # noqa: E501
        :rtype: int
        """
        return self._per_month

    @per_month.setter
    def per_month(self, per_month):
        """Sets the per_month of this UsageLimits.


        :param per_month: The per_month of this UsageLimits.  # noqa: E501
        :type: int
        """

        self._per_month = per_month

    @property
    def maximum_contacts(self):
        """Gets the maximum_contacts of this UsageLimits.  # noqa: E501


        :return: The maximum_contacts of this UsageLimits.  # noqa: E501
        :rtype: int
        """
        return self._maximum_contacts

    @maximum_contacts.setter
    def maximum_contacts(self, maximum_contacts):
        """Sets the maximum_contacts of this UsageLimits.


        :param maximum_contacts: The maximum_contacts of this UsageLimits.  # noqa: E501
        :type: int
        """

        self._maximum_contacts = maximum_contacts

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
        if not isinstance(other, UsageLimits):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsageLimits):
            return True

        return self.to_dict() != other.to_dict()
