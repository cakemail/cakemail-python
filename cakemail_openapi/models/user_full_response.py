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


class UserFullResponse(object):
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
        'id': 'int',
        'email': 'str',
        'status': 'str',
        'created_on': 'int',
        'last_activity_on': 'int',
        'first_name': 'str',
        'last_name': 'str',
        'title': 'str',
        'language': 'str',
        'timezone': 'str',
        'office_phone': 'str',
        'mobile_phone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'status': 'status',
        'created_on': 'created_on',
        'last_activity_on': 'last_activity_on',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'title': 'title',
        'language': 'language',
        'timezone': 'timezone',
        'office_phone': 'office_phone',
        'mobile_phone': 'mobile_phone'
    }

    def __init__(self, id=None, email=None, status=None, created_on=None, last_activity_on=None, first_name=None, last_name=None, title=None, language=None, timezone=None, office_phone=None, mobile_phone=None, local_vars_configuration=None):  # noqa: E501
        """UserFullResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._status = None
        self._created_on = None
        self._last_activity_on = None
        self._first_name = None
        self._last_name = None
        self._title = None
        self._language = None
        self._timezone = None
        self._office_phone = None
        self._mobile_phone = None
        self.discriminator = None

        self.id = id
        self.email = email
        self.status = status
        if created_on is not None:
            self.created_on = created_on
        if last_activity_on is not None:
            self.last_activity_on = last_activity_on
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if title is not None:
            self.title = title
        if language is not None:
            self.language = language
        if timezone is not None:
            self.timezone = timezone
        if office_phone is not None:
            self.office_phone = office_phone
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone

    @property
    def id(self):
        """Gets the id of this UserFullResponse.  # noqa: E501


        :return: The id of this UserFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserFullResponse.


        :param id: The id of this UserFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email(self):
        """Gets the email of this UserFullResponse.  # noqa: E501


        :return: The email of this UserFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserFullResponse.


        :param email: The email of this UserFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def status(self):
        """Gets the status of this UserFullResponse.  # noqa: E501


        :return: The status of this UserFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserFullResponse.


        :param status: The status of this UserFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def created_on(self):
        """Gets the created_on of this UserFullResponse.  # noqa: E501


        :return: The created_on of this UserFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this UserFullResponse.


        :param created_on: The created_on of this UserFullResponse.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def last_activity_on(self):
        """Gets the last_activity_on of this UserFullResponse.  # noqa: E501


        :return: The last_activity_on of this UserFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_activity_on

    @last_activity_on.setter
    def last_activity_on(self, last_activity_on):
        """Sets the last_activity_on of this UserFullResponse.


        :param last_activity_on: The last_activity_on of this UserFullResponse.  # noqa: E501
        :type: int
        """

        self._last_activity_on = last_activity_on

    @property
    def first_name(self):
        """Gets the first_name of this UserFullResponse.  # noqa: E501


        :return: The first_name of this UserFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserFullResponse.


        :param first_name: The first_name of this UserFullResponse.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserFullResponse.  # noqa: E501


        :return: The last_name of this UserFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserFullResponse.


        :param last_name: The last_name of this UserFullResponse.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def title(self):
        """Gets the title of this UserFullResponse.  # noqa: E501


        :return: The title of this UserFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UserFullResponse.


        :param title: The title of this UserFullResponse.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def language(self):
        """Gets the language of this UserFullResponse.  # noqa: E501


        :return: The language of this UserFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UserFullResponse.


        :param language: The language of this UserFullResponse.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def timezone(self):
        """Gets the timezone of this UserFullResponse.  # noqa: E501


        :return: The timezone of this UserFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this UserFullResponse.


        :param timezone: The timezone of this UserFullResponse.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def office_phone(self):
        """Gets the office_phone of this UserFullResponse.  # noqa: E501


        :return: The office_phone of this UserFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._office_phone

    @office_phone.setter
    def office_phone(self, office_phone):
        """Sets the office_phone of this UserFullResponse.


        :param office_phone: The office_phone of this UserFullResponse.  # noqa: E501
        :type: str
        """

        self._office_phone = office_phone

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this UserFullResponse.  # noqa: E501


        :return: The mobile_phone of this UserFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this UserFullResponse.


        :param mobile_phone: The mobile_phone of this UserFullResponse.  # noqa: E501
        :type: str
        """

        self._mobile_phone = mobile_phone

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
        if not isinstance(other, UserFullResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserFullResponse):
            return True

        return self.to_dict() != other.to_dict()
