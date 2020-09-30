# coding: utf-8

"""
    Cakemail API

    The Cakemail API exposes multiple APIs including Authentication, Marketing, Contact, Transactional, Analytic, Content, Account and Partner.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cakemail_openapi.configuration import Configuration


class EmailContent(object):
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
        'subject': 'str',
        'html': 'str',
        'text': 'str',
        'template': 'TemplateInfo',
        'encoding': 'Encoding'
    }

    attribute_map = {
        'subject': 'subject',
        'html': 'html',
        'text': 'text',
        'template': 'template',
        'encoding': 'encoding'
    }

    def __init__(self, subject=None, html=None, text=None, template=None, encoding=None, local_vars_configuration=None):  # noqa: E501
        """EmailContent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._subject = None
        self._html = None
        self._text = None
        self._template = None
        self._encoding = None
        self.discriminator = None

        self.subject = subject
        if html is not None:
            self.html = html
        if text is not None:
            self.text = text
        if template is not None:
            self.template = template
        self.encoding = encoding

    @property
    def subject(self):
        """Gets the subject of this EmailContent.  # noqa: E501


        :return: The subject of this EmailContent.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this EmailContent.


        :param subject: The subject of this EmailContent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subject is None:  # noqa: E501
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def html(self):
        """Gets the html of this EmailContent.  # noqa: E501


        :return: The html of this EmailContent.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this EmailContent.


        :param html: The html of this EmailContent.  # noqa: E501
        :type: str
        """

        self._html = html

    @property
    def text(self):
        """Gets the text of this EmailContent.  # noqa: E501


        :return: The text of this EmailContent.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this EmailContent.


        :param text: The text of this EmailContent.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def template(self):
        """Gets the template of this EmailContent.  # noqa: E501


        :return: The template of this EmailContent.  # noqa: E501
        :rtype: TemplateInfo
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this EmailContent.


        :param template: The template of this EmailContent.  # noqa: E501
        :type: TemplateInfo
        """

        self._template = template

    @property
    def encoding(self):
        """Gets the encoding of this EmailContent.  # noqa: E501


        :return: The encoding of this EmailContent.  # noqa: E501
        :rtype: Encoding
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this EmailContent.


        :param encoding: The encoding of this EmailContent.  # noqa: E501
        :type: Encoding
        """
        if self.local_vars_configuration.client_side_validation and encoding is None:  # noqa: E501
            raise ValueError("Invalid value for `encoding`, must not be `None`")  # noqa: E501

        self._encoding = encoding

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
        if not isinstance(other, EmailContent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailContent):
            return True

        return self.to_dict() != other.to_dict()
