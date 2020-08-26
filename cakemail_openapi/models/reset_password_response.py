# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.0.10
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class ResetPasswordResponse(object):
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
        'email': 'str',
        'object': 'str',
        'reset_link_sent': 'bool'
    }

    attribute_map = {
        'email': 'email',
        'object': 'object',
        'reset_link_sent': 'reset_link_sent'
    }

    def __init__(self, email=None, object='user', reset_link_sent=True, local_vars_configuration=None):  # noqa: E501
        """ResetPasswordResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._object = None
        self._reset_link_sent = None
        self.discriminator = None

        self.email = email
        if object is not None:
            self.object = object
        if reset_link_sent is not None:
            self.reset_link_sent = reset_link_sent

    @property
    def email(self):
        """Gets the email of this ResetPasswordResponse.  # noqa: E501


        :return: The email of this ResetPasswordResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ResetPasswordResponse.


        :param email: The email of this ResetPasswordResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def object(self):
        """Gets the object of this ResetPasswordResponse.  # noqa: E501


        :return: The object of this ResetPasswordResponse.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this ResetPasswordResponse.


        :param object: The object of this ResetPasswordResponse.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def reset_link_sent(self):
        """Gets the reset_link_sent of this ResetPasswordResponse.  # noqa: E501


        :return: The reset_link_sent of this ResetPasswordResponse.  # noqa: E501
        :rtype: bool
        """
        return self._reset_link_sent

    @reset_link_sent.setter
    def reset_link_sent(self, reset_link_sent):
        """Sets the reset_link_sent of this ResetPasswordResponse.


        :param reset_link_sent: The reset_link_sent of this ResetPasswordResponse.  # noqa: E501
        :type: bool
        """

        self._reset_link_sent = reset_link_sent

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
        if not isinstance(other, ResetPasswordResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResetPasswordResponse):
            return True

        return self.to_dict() != other.to_dict()
