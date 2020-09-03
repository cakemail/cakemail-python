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


class DeleteSenderResponse(object):
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
        'id': 'str',
        'deleted': 'bool',
        'object': 'str'
    }

    attribute_map = {
        'id': 'id',
        'deleted': 'deleted',
        'object': 'object'
    }

    def __init__(self, id=None, deleted=True, object='sender', local_vars_configuration=None):  # noqa: E501
        """DeleteSenderResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._deleted = None
        self._object = None
        self.discriminator = None

        self.id = id
        if deleted is not None:
            self.deleted = deleted
        if object is not None:
            self.object = object

    @property
    def id(self):
        """Gets the id of this DeleteSenderResponse.  # noqa: E501


        :return: The id of this DeleteSenderResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteSenderResponse.


        :param id: The id of this DeleteSenderResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def deleted(self):
        """Gets the deleted of this DeleteSenderResponse.  # noqa: E501


        :return: The deleted of this DeleteSenderResponse.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this DeleteSenderResponse.


        :param deleted: The deleted of this DeleteSenderResponse.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def object(self):
        """Gets the object of this DeleteSenderResponse.  # noqa: E501


        :return: The object of this DeleteSenderResponse.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this DeleteSenderResponse.


        :param object: The object of this DeleteSenderResponse.  # noqa: E501
        :type: str
        """

        self._object = object

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
        if not isinstance(other, DeleteSenderResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteSenderResponse):
            return True

        return self.to_dict() != other.to_dict()
