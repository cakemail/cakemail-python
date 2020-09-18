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


class List(object):
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
        'name': 'str',
        'default_sender': 'Sender',
        'language': 'Languages',
        'redirections': 'Redirections',
        'webhook': 'Webhook'
    }

    attribute_map = {
        'name': 'name',
        'default_sender': 'default_sender',
        'language': 'language',
        'redirections': 'redirections',
        'webhook': 'webhook'
    }

    def __init__(self, name=None, default_sender=None, language=None, redirections=None, webhook=None, local_vars_configuration=None):  # noqa: E501
        """List - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._default_sender = None
        self._language = None
        self._redirections = None
        self._webhook = None
        self.discriminator = None

        self.name = name
        self.default_sender = default_sender
        if language is not None:
            self.language = language
        if redirections is not None:
            self.redirections = redirections
        if webhook is not None:
            self.webhook = webhook

    @property
    def name(self):
        """Gets the name of this List.  # noqa: E501


        :return: The name of this List.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this List.


        :param name: The name of this List.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def default_sender(self):
        """Gets the default_sender of this List.  # noqa: E501


        :return: The default_sender of this List.  # noqa: E501
        :rtype: Sender
        """
        return self._default_sender

    @default_sender.setter
    def default_sender(self, default_sender):
        """Sets the default_sender of this List.


        :param default_sender: The default_sender of this List.  # noqa: E501
        :type: Sender
        """
        if self.local_vars_configuration.client_side_validation and default_sender is None:  # noqa: E501
            raise ValueError("Invalid value for `default_sender`, must not be `None`")  # noqa: E501

        self._default_sender = default_sender

    @property
    def language(self):
        """Gets the language of this List.  # noqa: E501


        :return: The language of this List.  # noqa: E501
        :rtype: Languages
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this List.


        :param language: The language of this List.  # noqa: E501
        :type: Languages
        """

        self._language = language

    @property
    def redirections(self):
        """Gets the redirections of this List.  # noqa: E501


        :return: The redirections of this List.  # noqa: E501
        :rtype: Redirections
        """
        return self._redirections

    @redirections.setter
    def redirections(self, redirections):
        """Sets the redirections of this List.


        :param redirections: The redirections of this List.  # noqa: E501
        :type: Redirections
        """

        self._redirections = redirections

    @property
    def webhook(self):
        """Gets the webhook of this List.  # noqa: E501


        :return: The webhook of this List.  # noqa: E501
        :rtype: Webhook
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this List.


        :param webhook: The webhook of this List.  # noqa: E501
        :type: Webhook
        """

        self._webhook = webhook

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
        if not isinstance(other, List):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, List):
            return True

        return self.to_dict() != other.to_dict()
