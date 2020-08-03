# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.0.8
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class CampaignLinkStatsResponse(object):
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
        'link': 'str',
        'unique': 'str',
        'total': 'str',
        'unique_rate': 'float',
        'total_rate': 'float'
    }

    attribute_map = {
        'id': 'id',
        'link': 'link',
        'unique': 'unique',
        'total': 'total',
        'unique_rate': 'unique_rate',
        'total_rate': 'total_rate'
    }

    def __init__(self, id=None, link=None, unique=None, total=None, unique_rate=None, total_rate=None, local_vars_configuration=None):  # noqa: E501
        """CampaignLinkStatsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._link = None
        self._unique = None
        self._total = None
        self._unique_rate = None
        self._total_rate = None
        self.discriminator = None

        self.id = id
        self.link = link
        self.unique = unique
        self.total = total
        self.unique_rate = unique_rate
        self.total_rate = total_rate

    @property
    def id(self):
        """Gets the id of this CampaignLinkStatsResponse.  # noqa: E501


        :return: The id of this CampaignLinkStatsResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CampaignLinkStatsResponse.


        :param id: The id of this CampaignLinkStatsResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def link(self):
        """Gets the link of this CampaignLinkStatsResponse.  # noqa: E501


        :return: The link of this CampaignLinkStatsResponse.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this CampaignLinkStatsResponse.


        :param link: The link of this CampaignLinkStatsResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and link is None:  # noqa: E501
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

    @property
    def unique(self):
        """Gets the unique of this CampaignLinkStatsResponse.  # noqa: E501


        :return: The unique of this CampaignLinkStatsResponse.  # noqa: E501
        :rtype: str
        """
        return self._unique

    @unique.setter
    def unique(self, unique):
        """Sets the unique of this CampaignLinkStatsResponse.


        :param unique: The unique of this CampaignLinkStatsResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and unique is None:  # noqa: E501
            raise ValueError("Invalid value for `unique`, must not be `None`")  # noqa: E501

        self._unique = unique

    @property
    def total(self):
        """Gets the total of this CampaignLinkStatsResponse.  # noqa: E501


        :return: The total of this CampaignLinkStatsResponse.  # noqa: E501
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CampaignLinkStatsResponse.


        :param total: The total of this CampaignLinkStatsResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and total is None:  # noqa: E501
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def unique_rate(self):
        """Gets the unique_rate of this CampaignLinkStatsResponse.  # noqa: E501


        :return: The unique_rate of this CampaignLinkStatsResponse.  # noqa: E501
        :rtype: float
        """
        return self._unique_rate

    @unique_rate.setter
    def unique_rate(self, unique_rate):
        """Sets the unique_rate of this CampaignLinkStatsResponse.


        :param unique_rate: The unique_rate of this CampaignLinkStatsResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and unique_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `unique_rate`, must not be `None`")  # noqa: E501

        self._unique_rate = unique_rate

    @property
    def total_rate(self):
        """Gets the total_rate of this CampaignLinkStatsResponse.  # noqa: E501


        :return: The total_rate of this CampaignLinkStatsResponse.  # noqa: E501
        :rtype: float
        """
        return self._total_rate

    @total_rate.setter
    def total_rate(self, total_rate):
        """Sets the total_rate of this CampaignLinkStatsResponse.


        :param total_rate: The total_rate of this CampaignLinkStatsResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `total_rate`, must not be `None`")  # noqa: E501

        self._total_rate = total_rate

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
        if not isinstance(other, CampaignLinkStatsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignLinkStatsResponse):
            return True

        return self.to_dict() != other.to_dict()
