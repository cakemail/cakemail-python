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


class ImportContacts(object):
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
        'import_to': 'ContactStatus',
        'contacts': 'list[ImportContactData]'
    }

    attribute_map = {
        'import_to': 'import_to',
        'contacts': 'contacts'
    }

    def __init__(self, import_to=None, contacts=None, local_vars_configuration=None):  # noqa: E501
        """ImportContacts - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._import_to = None
        self._contacts = None
        self.discriminator = None

        if import_to is not None:
            self.import_to = import_to
        self.contacts = contacts

    @property
    def import_to(self):
        """Gets the import_to of this ImportContacts.  # noqa: E501


        :return: The import_to of this ImportContacts.  # noqa: E501
        :rtype: ContactStatus
        """
        return self._import_to

    @import_to.setter
    def import_to(self, import_to):
        """Sets the import_to of this ImportContacts.


        :param import_to: The import_to of this ImportContacts.  # noqa: E501
        :type: ContactStatus
        """

        self._import_to = import_to

    @property
    def contacts(self):
        """Gets the contacts of this ImportContacts.  # noqa: E501


        :return: The contacts of this ImportContacts.  # noqa: E501
        :rtype: list[ImportContactData]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this ImportContacts.


        :param contacts: The contacts of this ImportContacts.  # noqa: E501
        :type: list[ImportContactData]
        """
        if self.local_vars_configuration.client_side_validation and contacts is None:  # noqa: E501
            raise ValueError("Invalid value for `contacts`, must not be `None`")  # noqa: E501

        self._contacts = contacts

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
        if not isinstance(other, ImportContacts):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportContacts):
            return True

        return self.to_dict() != other.to_dict()
