# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.0.8
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class LinkFullResponse(object):
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
        'status': 'str',
        'link_to': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'link_to': 'link_to'
    }

    def __init__(self, id=None, status=None, link_to=None, local_vars_configuration=None):  # noqa: E501
        """LinkFullResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._status = None
        self._link_to = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.link_to = link_to

    @property
    def id(self):
        """Gets the id of this LinkFullResponse.  # noqa: E501


        :return: The id of this LinkFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LinkFullResponse.


        :param id: The id of this LinkFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status(self):
        """Gets the status of this LinkFullResponse.  # noqa: E501


        :return: The status of this LinkFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LinkFullResponse.


        :param status: The status of this LinkFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def link_to(self):
        """Gets the link_to of this LinkFullResponse.  # noqa: E501


        :return: The link_to of this LinkFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._link_to

    @link_to.setter
    def link_to(self, link_to):
        """Sets the link_to of this LinkFullResponse.


        :param link_to: The link_to of this LinkFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and link_to is None:  # noqa: E501
            raise ValueError("Invalid value for `link_to`, must not be `None`")  # noqa: E501

        self._link_to = link_to

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
        if not isinstance(other, LinkFullResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LinkFullResponse):
            return True

        return self.to_dict() != other.to_dict()
