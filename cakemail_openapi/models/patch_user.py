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


class PatchUser(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'title': 'str',
        'office_phone': 'str',
        'mobile_phone': 'str',
        'language': 'str',
        'timezone': 'str',
        'password': 'str'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'title': 'title',
        'office_phone': 'office_phone',
        'mobile_phone': 'mobile_phone',
        'language': 'language',
        'timezone': 'timezone',
        'password': 'password'
    }

    def __init__(self, email=None, first_name=None, last_name=None, title=None, office_phone=None, mobile_phone=None, language=None, timezone=None, password=None, local_vars_configuration=None):  # noqa: E501
        """PatchUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._first_name = None
        self._last_name = None
        self._title = None
        self._office_phone = None
        self._mobile_phone = None
        self._language = None
        self._timezone = None
        self._password = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if title is not None:
            self.title = title
        if office_phone is not None:
            self.office_phone = office_phone
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if language is not None:
            self.language = language
        if timezone is not None:
            self.timezone = timezone
        if password is not None:
            self.password = password

    @property
    def email(self):
        """Gets the email of this PatchUser.  # noqa: E501


        :return: The email of this PatchUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PatchUser.


        :param email: The email of this PatchUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this PatchUser.  # noqa: E501


        :return: The first_name of this PatchUser.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this PatchUser.


        :param first_name: The first_name of this PatchUser.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this PatchUser.  # noqa: E501


        :return: The last_name of this PatchUser.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this PatchUser.


        :param last_name: The last_name of this PatchUser.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def title(self):
        """Gets the title of this PatchUser.  # noqa: E501


        :return: The title of this PatchUser.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PatchUser.


        :param title: The title of this PatchUser.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def office_phone(self):
        """Gets the office_phone of this PatchUser.  # noqa: E501


        :return: The office_phone of this PatchUser.  # noqa: E501
        :rtype: str
        """
        return self._office_phone

    @office_phone.setter
    def office_phone(self, office_phone):
        """Sets the office_phone of this PatchUser.


        :param office_phone: The office_phone of this PatchUser.  # noqa: E501
        :type: str
        """

        self._office_phone = office_phone

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this PatchUser.  # noqa: E501


        :return: The mobile_phone of this PatchUser.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this PatchUser.


        :param mobile_phone: The mobile_phone of this PatchUser.  # noqa: E501
        :type: str
        """

        self._mobile_phone = mobile_phone

    @property
    def language(self):
        """Gets the language of this PatchUser.  # noqa: E501


        :return: The language of this PatchUser.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PatchUser.


        :param language: The language of this PatchUser.  # noqa: E501
        :type: str
        """
        allowed_values = ["en_US", "de_DE", "el_GR", "es_US", "et_EE", "fr_CA", "nl_NL", "ro_RO", "ru_RU", "th_TH", "zh_CN", "fi_FI", "sv_SE", "es_ES", "fr_FR", "tr_TR", "pt_BR", "da_DK"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and language not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def timezone(self):
        """Gets the timezone of this PatchUser.  # noqa: E501

        Based on tz database  # noqa: E501

        :return: The timezone of this PatchUser.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this PatchUser.

        Based on tz database  # noqa: E501

        :param timezone: The timezone of this PatchUser.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def password(self):
        """Gets the password of this PatchUser.  # noqa: E501


        :return: The password of this PatchUser.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this PatchUser.


        :param password: The password of this PatchUser.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if not isinstance(other, PatchUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchUser):
            return True

        return self.to_dict() != other.to_dict()
