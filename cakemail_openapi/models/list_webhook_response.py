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


class ListWebhookResponse(object):
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
        'url': 'str',
        'actions': 'list[ListWebhookAction]'
    }

    attribute_map = {
        'url': 'url',
        'actions': 'actions'
    }

    def __init__(self, url=None, actions=None, local_vars_configuration=None):  # noqa: E501
        """ListWebhookResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._actions = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if actions is not None:
            self.actions = actions

    @property
    def url(self):
        """Gets the url of this ListWebhookResponse.  # noqa: E501


        :return: The url of this ListWebhookResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ListWebhookResponse.


        :param url: The url of this ListWebhookResponse.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def actions(self):
        """Gets the actions of this ListWebhookResponse.  # noqa: E501


        :return: The actions of this ListWebhookResponse.  # noqa: E501
        :rtype: list[ListWebhookAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ListWebhookResponse.


        :param actions: The actions of this ListWebhookResponse.  # noqa: E501
        :type: list[ListWebhookAction]
        """

        self._actions = actions

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
        if not isinstance(other, ListWebhookResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListWebhookResponse):
            return True

        return self.to_dict() != other.to_dict()
