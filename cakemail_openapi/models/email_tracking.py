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


class EmailTracking(object):
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
        'opens': 'bool',
        'clicks_html': 'bool',
        'clicks_text': 'bool'
    }

    attribute_map = {
        'opens': 'opens',
        'clicks_html': 'clicks_html',
        'clicks_text': 'clicks_text'
    }

    def __init__(self, opens=True, clicks_html=True, clicks_text=True, local_vars_configuration=None):  # noqa: E501
        """EmailTracking - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._opens = None
        self._clicks_html = None
        self._clicks_text = None
        self.discriminator = None

        if opens is not None:
            self.opens = opens
        if clicks_html is not None:
            self.clicks_html = clicks_html
        if clicks_text is not None:
            self.clicks_text = clicks_text

    @property
    def opens(self):
        """Gets the opens of this EmailTracking.  # noqa: E501

        Enable the tracking of opens (only available for the HTML version)  # noqa: E501

        :return: The opens of this EmailTracking.  # noqa: E501
        :rtype: bool
        """
        return self._opens

    @opens.setter
    def opens(self, opens):
        """Sets the opens of this EmailTracking.

        Enable the tracking of opens (only available for the HTML version)  # noqa: E501

        :param opens: The opens of this EmailTracking.  # noqa: E501
        :type: bool
        """

        self._opens = opens

    @property
    def clicks_html(self):
        """Gets the clicks_html of this EmailTracking.  # noqa: E501

        Enable the tracking of link clicks in the HTML version  # noqa: E501

        :return: The clicks_html of this EmailTracking.  # noqa: E501
        :rtype: bool
        """
        return self._clicks_html

    @clicks_html.setter
    def clicks_html(self, clicks_html):
        """Sets the clicks_html of this EmailTracking.

        Enable the tracking of link clicks in the HTML version  # noqa: E501

        :param clicks_html: The clicks_html of this EmailTracking.  # noqa: E501
        :type: bool
        """

        self._clicks_html = clicks_html

    @property
    def clicks_text(self):
        """Gets the clicks_text of this EmailTracking.  # noqa: E501

        Enable the tracking of link clicks in the text version  # noqa: E501

        :return: The clicks_text of this EmailTracking.  # noqa: E501
        :rtype: bool
        """
        return self._clicks_text

    @clicks_text.setter
    def clicks_text(self, clicks_text):
        """Sets the clicks_text of this EmailTracking.

        Enable the tracking of link clicks in the text version  # noqa: E501

        :param clicks_text: The clicks_text of this EmailTracking.  # noqa: E501
        :type: bool
        """

        self._clicks_text = clicks_text

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
        if not isinstance(other, EmailTracking):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailTracking):
            return True

        return self.to_dict() != other.to_dict()
