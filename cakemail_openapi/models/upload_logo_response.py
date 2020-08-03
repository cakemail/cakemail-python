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


class UploadLogoResponse(object):
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
        'logo': 'str',
        'object': 'str',
        'uploaded': 'bool'
    }

    attribute_map = {
        'logo': 'logo',
        'object': 'object',
        'uploaded': 'uploaded'
    }

    def __init__(self, logo=None, object='logo', uploaded=True, local_vars_configuration=None):  # noqa: E501
        """UploadLogoResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._logo = None
        self._object = None
        self._uploaded = None
        self.discriminator = None

        self.logo = logo
        if object is not None:
            self.object = object
        if uploaded is not None:
            self.uploaded = uploaded

    @property
    def logo(self):
        """Gets the logo of this UploadLogoResponse.  # noqa: E501


        :return: The logo of this UploadLogoResponse.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this UploadLogoResponse.


        :param logo: The logo of this UploadLogoResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and logo is None:  # noqa: E501
            raise ValueError("Invalid value for `logo`, must not be `None`")  # noqa: E501

        self._logo = logo

    @property
    def object(self):
        """Gets the object of this UploadLogoResponse.  # noqa: E501


        :return: The object of this UploadLogoResponse.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this UploadLogoResponse.


        :param object: The object of this UploadLogoResponse.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def uploaded(self):
        """Gets the uploaded of this UploadLogoResponse.  # noqa: E501


        :return: The uploaded of this UploadLogoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._uploaded

    @uploaded.setter
    def uploaded(self, uploaded):
        """Sets the uploaded of this UploadLogoResponse.


        :param uploaded: The uploaded of this UploadLogoResponse.  # noqa: E501
        :type: bool
        """

        self._uploaded = uploaded

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
        if not isinstance(other, UploadLogoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UploadLogoResponse):
            return True

        return self.to_dict() != other.to_dict()
