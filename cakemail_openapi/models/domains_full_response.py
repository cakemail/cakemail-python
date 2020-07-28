# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.0.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class DomainsFullResponse(object):
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
        'auth': 'str',
        'bounce': 'str',
        'dkim': 'str',
        'tracking': 'str'
    }

    attribute_map = {
        'auth': 'auth',
        'bounce': 'bounce',
        'dkim': 'dkim',
        'tracking': 'tracking'
    }

    def __init__(self, auth=None, bounce=None, dkim=None, tracking=None, local_vars_configuration=None):  # noqa: E501
        """DomainsFullResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auth = None
        self._bounce = None
        self._dkim = None
        self._tracking = None
        self.discriminator = None

        self.auth = auth
        self.bounce = bounce
        self.dkim = dkim
        self.tracking = tracking

    @property
    def auth(self):
        """Gets the auth of this DomainsFullResponse.  # noqa: E501


        :return: The auth of this DomainsFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this DomainsFullResponse.


        :param auth: The auth of this DomainsFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and auth is None:  # noqa: E501
            raise ValueError("Invalid value for `auth`, must not be `None`")  # noqa: E501

        self._auth = auth

    @property
    def bounce(self):
        """Gets the bounce of this DomainsFullResponse.  # noqa: E501


        :return: The bounce of this DomainsFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._bounce

    @bounce.setter
    def bounce(self, bounce):
        """Sets the bounce of this DomainsFullResponse.


        :param bounce: The bounce of this DomainsFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and bounce is None:  # noqa: E501
            raise ValueError("Invalid value for `bounce`, must not be `None`")  # noqa: E501

        self._bounce = bounce

    @property
    def dkim(self):
        """Gets the dkim of this DomainsFullResponse.  # noqa: E501


        :return: The dkim of this DomainsFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._dkim

    @dkim.setter
    def dkim(self, dkim):
        """Sets the dkim of this DomainsFullResponse.


        :param dkim: The dkim of this DomainsFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dkim is None:  # noqa: E501
            raise ValueError("Invalid value for `dkim`, must not be `None`")  # noqa: E501

        self._dkim = dkim

    @property
    def tracking(self):
        """Gets the tracking of this DomainsFullResponse.  # noqa: E501


        :return: The tracking of this DomainsFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this DomainsFullResponse.


        :param tracking: The tracking of this DomainsFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tracking is None:  # noqa: E501
            raise ValueError("Invalid value for `tracking`, must not be `None`")  # noqa: E501

        self._tracking = tracking

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
        if not isinstance(other, DomainsFullResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DomainsFullResponse):
            return True

        return self.to_dict() != other.to_dict()
