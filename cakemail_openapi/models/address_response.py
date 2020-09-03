# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.0.14
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class AddressResponse(object):
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
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'country': 'str',
        'province': 'str',
        'postal_code': 'str'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'country': 'country',
        'province': 'province',
        'postal_code': 'postal_code'
    }

    def __init__(self, address1=None, address2=None, city=None, country=None, province=None, postal_code=None, local_vars_configuration=None):  # noqa: E501
        """AddressResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address1 = None
        self._address2 = None
        self._city = None
        self._country = None
        self._province = None
        self._postal_code = None
        self.discriminator = None

        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if province is not None:
            self.province = province
        if postal_code is not None:
            self.postal_code = postal_code

    @property
    def address1(self):
        """Gets the address1 of this AddressResponse.  # noqa: E501


        :return: The address1 of this AddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this AddressResponse.


        :param address1: The address1 of this AddressResponse.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this AddressResponse.  # noqa: E501


        :return: The address2 of this AddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this AddressResponse.


        :param address2: The address2 of this AddressResponse.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this AddressResponse.  # noqa: E501


        :return: The city of this AddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AddressResponse.


        :param city: The city of this AddressResponse.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this AddressResponse.  # noqa: E501


        :return: The country of this AddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AddressResponse.


        :param country: The country of this AddressResponse.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def province(self):
        """Gets the province of this AddressResponse.  # noqa: E501


        :return: The province of this AddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this AddressResponse.


        :param province: The province of this AddressResponse.  # noqa: E501
        :type: str
        """

        self._province = province

    @property
    def postal_code(self):
        """Gets the postal_code of this AddressResponse.  # noqa: E501


        :return: The postal_code of this AddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this AddressResponse.


        :param postal_code: The postal_code of this AddressResponse.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

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
        if not isinstance(other, AddressResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddressResponse):
            return True

        return self.to_dict() != other.to_dict()
