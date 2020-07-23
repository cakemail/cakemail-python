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


class ConfirmSender(object):
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
        'confirmation_id': 'str'
    }

    attribute_map = {
        'confirmation_id': 'confirmation_id'
    }

    def __init__(self, confirmation_id=None, local_vars_configuration=None):  # noqa: E501
        """ConfirmSender - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._confirmation_id = None
        self.discriminator = None

        self.confirmation_id = confirmation_id

    @property
    def confirmation_id(self):
        """Gets the confirmation_id of this ConfirmSender.  # noqa: E501


        :return: The confirmation_id of this ConfirmSender.  # noqa: E501
        :rtype: str
        """
        return self._confirmation_id

    @confirmation_id.setter
    def confirmation_id(self, confirmation_id):
        """Sets the confirmation_id of this ConfirmSender.


        :param confirmation_id: The confirmation_id of this ConfirmSender.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and confirmation_id is None:  # noqa: E501
            raise ValueError("Invalid value for `confirmation_id`, must not be `None`")  # noqa: E501

        self._confirmation_id = confirmation_id

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
        if not isinstance(other, ConfirmSender):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfirmSender):
            return True

        return self.to_dict() != other.to_dict()
