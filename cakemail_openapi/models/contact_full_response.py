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


class ContactFullResponse(object):
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
        'subscribed_on': 'int',
        'last_bounce_type': 'str',
        'bounces_count': 'int',
        'custom_attributes': 'list[CustomAttributesDataResponse]'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'status': 'status',
        'subscribed_on': 'subscribed_on',
        'last_bounce_type': 'last_bounce_type',
        'bounces_count': 'bounces_count',
        'custom_attributes': 'custom_attributes'
    }

    def __init__(self, id=None, email=None, status=None, subscribed_on=None, last_bounce_type=None, bounces_count=None, custom_attributes=None, local_vars_configuration=None):  # noqa: E501
        """ContactFullResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._status = None
        self._subscribed_on = None
        self._last_bounce_type = None
        self._bounces_count = None
        self._custom_attributes = None
        self.discriminator = None

        self.id = id
        self.email = email
        self.status = status
        self.subscribed_on = subscribed_on
        self.last_bounce_type = last_bounce_type
        self.bounces_count = bounces_count
        self.custom_attributes = custom_attributes

    @property
    def id(self):
        """Gets the id of this ContactFullResponse.  # noqa: E501


        :return: The id of this ContactFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContactFullResponse.


        :param id: The id of this ContactFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email(self):
        """Gets the email of this ContactFullResponse.  # noqa: E501


        :return: The email of this ContactFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContactFullResponse.


        :param email: The email of this ContactFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def status(self):
        """Gets the status of this ContactFullResponse.  # noqa: E501


        :return: The status of this ContactFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ContactFullResponse.


        :param status: The status of this ContactFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def subscribed_on(self):
        """Gets the subscribed_on of this ContactFullResponse.  # noqa: E501


        :return: The subscribed_on of this ContactFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._subscribed_on

    @subscribed_on.setter
    def subscribed_on(self, subscribed_on):
        """Sets the subscribed_on of this ContactFullResponse.


        :param subscribed_on: The subscribed_on of this ContactFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and subscribed_on is None:  # noqa: E501
            raise ValueError("Invalid value for `subscribed_on`, must not be `None`")  # noqa: E501

        self._subscribed_on = subscribed_on

    @property
    def last_bounce_type(self):
        """Gets the last_bounce_type of this ContactFullResponse.  # noqa: E501


        :return: The last_bounce_type of this ContactFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_bounce_type

    @last_bounce_type.setter
    def last_bounce_type(self, last_bounce_type):
        """Sets the last_bounce_type of this ContactFullResponse.


        :param last_bounce_type: The last_bounce_type of this ContactFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and last_bounce_type is None:  # noqa: E501
            raise ValueError("Invalid value for `last_bounce_type`, must not be `None`")  # noqa: E501

        self._last_bounce_type = last_bounce_type

    @property
    def bounces_count(self):
        """Gets the bounces_count of this ContactFullResponse.  # noqa: E501


        :return: The bounces_count of this ContactFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._bounces_count

    @bounces_count.setter
    def bounces_count(self, bounces_count):
        """Sets the bounces_count of this ContactFullResponse.


        :param bounces_count: The bounces_count of this ContactFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bounces_count is None:  # noqa: E501
            raise ValueError("Invalid value for `bounces_count`, must not be `None`")  # noqa: E501

        self._bounces_count = bounces_count

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this ContactFullResponse.  # noqa: E501


        :return: The custom_attributes of this ContactFullResponse.  # noqa: E501
        :rtype: list[CustomAttributesDataResponse]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this ContactFullResponse.


        :param custom_attributes: The custom_attributes of this ContactFullResponse.  # noqa: E501
        :type: list[CustomAttributesDataResponse]
        """
        if self.local_vars_configuration.client_side_validation and custom_attributes is None:  # noqa: E501
            raise ValueError("Invalid value for `custom_attributes`, must not be `None`")  # noqa: E501

        self._custom_attributes = custom_attributes

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
        if not isinstance(other, ContactFullResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContactFullResponse):
            return True

        return self.to_dict() != other.to_dict()
