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


class UserInfo(object):
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
        'os': 'OperatingSystemInfo',
        'browser': 'BrowserInfo',
        'device': 'DeviceInfo',
        'is_bot': 'bool',
        'raw': 'str'
    }

    attribute_map = {
        'os': 'os',
        'browser': 'browser',
        'device': 'device',
        'is_bot': 'is_bot',
        'raw': 'raw'
    }

    def __init__(self, os=None, browser=None, device=None, is_bot=None, raw=None, local_vars_configuration=None):  # noqa: E501
        """UserInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._os = None
        self._browser = None
        self._device = None
        self._is_bot = None
        self._raw = None
        self.discriminator = None

        self.os = os
        self.browser = browser
        self.device = device
        if is_bot is not None:
            self.is_bot = is_bot
        if raw is not None:
            self.raw = raw

    @property
    def os(self):
        """Gets the os of this UserInfo.  # noqa: E501


        :return: The os of this UserInfo.  # noqa: E501
        :rtype: OperatingSystemInfo
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this UserInfo.


        :param os: The os of this UserInfo.  # noqa: E501
        :type: OperatingSystemInfo
        """
        if self.local_vars_configuration.client_side_validation and os is None:  # noqa: E501
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501

        self._os = os

    @property
    def browser(self):
        """Gets the browser of this UserInfo.  # noqa: E501


        :return: The browser of this UserInfo.  # noqa: E501
        :rtype: BrowserInfo
        """
        return self._browser

    @browser.setter
    def browser(self, browser):
        """Sets the browser of this UserInfo.


        :param browser: The browser of this UserInfo.  # noqa: E501
        :type: BrowserInfo
        """
        if self.local_vars_configuration.client_side_validation and browser is None:  # noqa: E501
            raise ValueError("Invalid value for `browser`, must not be `None`")  # noqa: E501

        self._browser = browser

    @property
    def device(self):
        """Gets the device of this UserInfo.  # noqa: E501


        :return: The device of this UserInfo.  # noqa: E501
        :rtype: DeviceInfo
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this UserInfo.


        :param device: The device of this UserInfo.  # noqa: E501
        :type: DeviceInfo
        """
        if self.local_vars_configuration.client_side_validation and device is None:  # noqa: E501
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def is_bot(self):
        """Gets the is_bot of this UserInfo.  # noqa: E501


        :return: The is_bot of this UserInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_bot

    @is_bot.setter
    def is_bot(self, is_bot):
        """Sets the is_bot of this UserInfo.


        :param is_bot: The is_bot of this UserInfo.  # noqa: E501
        :type: bool
        """

        self._is_bot = is_bot

    @property
    def raw(self):
        """Gets the raw of this UserInfo.  # noqa: E501


        :return: The raw of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this UserInfo.


        :param raw: The raw of this UserInfo.  # noqa: E501
        :type: str
        """

        self._raw = raw

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
        if not isinstance(other, UserInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserInfo):
            return True

        return self.to_dict() != other.to_dict()
