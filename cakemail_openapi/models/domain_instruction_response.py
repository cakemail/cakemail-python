# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.0.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class DomainInstructionResponse(object):
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
        'entry': 'str',
        'valid': 'bool'
    }

    attribute_map = {
        'entry': 'entry',
        'valid': 'valid'
    }

    def __init__(self, entry=None, valid=None, local_vars_configuration=None):  # noqa: E501
        """DomainInstructionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._entry = None
        self._valid = None
        self.discriminator = None

        self.entry = entry
        self.valid = valid

    @property
    def entry(self):
        """Gets the entry of this DomainInstructionResponse.  # noqa: E501


        :return: The entry of this DomainInstructionResponse.  # noqa: E501
        :rtype: str
        """
        return self._entry

    @entry.setter
    def entry(self, entry):
        """Sets the entry of this DomainInstructionResponse.


        :param entry: The entry of this DomainInstructionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and entry is None:  # noqa: E501
            raise ValueError("Invalid value for `entry`, must not be `None`")  # noqa: E501

        self._entry = entry

    @property
    def valid(self):
        """Gets the valid of this DomainInstructionResponse.  # noqa: E501


        :return: The valid of this DomainInstructionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this DomainInstructionResponse.


        :param valid: The valid of this DomainInstructionResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and valid is None:  # noqa: E501
            raise ValueError("Invalid value for `valid`, must not be `None`")  # noqa: E501

        self._valid = valid

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
        if not isinstance(other, DomainInstructionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DomainInstructionResponse):
            return True

        return self.to_dict() != other.to_dict()
