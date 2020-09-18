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


class Email(object):
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
        'group_id': 'int',
        'tracking': 'EmailTracking',
        'sender': 'Sender',
        'content': 'EmailContent'
    }

    attribute_map = {
        'email': 'email',
        'group_id': 'group_id',
        'tracking': 'tracking',
        'sender': 'sender',
        'content': 'content'
    }

    def __init__(self, email=None, group_id=None, tracking=None, sender=None, content=None, local_vars_configuration=None):  # noqa: E501
        """Email - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._group_id = None
        self._tracking = None
        self._sender = None
        self._content = None
        self.discriminator = None

        self.email = email
        if group_id is not None:
            self.group_id = group_id
        if tracking is not None:
            self.tracking = tracking
        self.sender = sender
        self.content = content

    @property
    def email(self):
        """Gets the email of this Email.  # noqa: E501


        :return: The email of this Email.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Email.


        :param email: The email of this Email.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def group_id(self):
        """Gets the group_id of this Email.  # noqa: E501

        Allows you to group multiple transaction emails together for analytics  # noqa: E501

        :return: The group_id of this Email.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this Email.

        Allows you to group multiple transaction emails together for analytics  # noqa: E501

        :param group_id: The group_id of this Email.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def tracking(self):
        """Gets the tracking of this Email.  # noqa: E501


        :return: The tracking of this Email.  # noqa: E501
        :rtype: EmailTracking
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this Email.


        :param tracking: The tracking of this Email.  # noqa: E501
        :type: EmailTracking
        """

        self._tracking = tracking

    @property
    def sender(self):
        """Gets the sender of this Email.  # noqa: E501


        :return: The sender of this Email.  # noqa: E501
        :rtype: Sender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this Email.


        :param sender: The sender of this Email.  # noqa: E501
        :type: Sender
        """
        if self.local_vars_configuration.client_side_validation and sender is None:  # noqa: E501
            raise ValueError("Invalid value for `sender`, must not be `None`")  # noqa: E501

        self._sender = sender

    @property
    def content(self):
        """Gets the content of this Email.  # noqa: E501


        :return: The content of this Email.  # noqa: E501
        :rtype: EmailContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Email.


        :param content: The content of this Email.  # noqa: E501
        :type: EmailContent
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

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
        if not isinstance(other, Email):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Email):
            return True

        return self.to_dict() != other.to_dict()
