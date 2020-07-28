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


class CreateCampaign(object):
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
        'name': 'str',
        'audience': 'Audience',
        'tracking': 'Tracking',
        'sender': 'Sender',
        'reply_to_email': 'str',
        'content': 'CampaignContent',
        'editor': 'str'
    }

    attribute_map = {
        'name': 'name',
        'audience': 'audience',
        'tracking': 'tracking',
        'sender': 'sender',
        'reply_to_email': 'reply_to_email',
        'content': 'content',
        'editor': 'editor'
    }

    def __init__(self, name=None, audience=None, tracking=None, sender=None, reply_to_email=None, content=None, editor='bee', local_vars_configuration=None):  # noqa: E501
        """CreateCampaign - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._audience = None
        self._tracking = None
        self._sender = None
        self._reply_to_email = None
        self._content = None
        self._editor = None
        self.discriminator = None

        self.name = name
        if audience is not None:
            self.audience = audience
        if tracking is not None:
            self.tracking = tracking
        if sender is not None:
            self.sender = sender
        if reply_to_email is not None:
            self.reply_to_email = reply_to_email
        if content is not None:
            self.content = content
        if editor is not None:
            self.editor = editor

    @property
    def name(self):
        """Gets the name of this CreateCampaign.  # noqa: E501


        :return: The name of this CreateCampaign.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCampaign.


        :param name: The name of this CreateCampaign.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def audience(self):
        """Gets the audience of this CreateCampaign.  # noqa: E501


        :return: The audience of this CreateCampaign.  # noqa: E501
        :rtype: Audience
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this CreateCampaign.


        :param audience: The audience of this CreateCampaign.  # noqa: E501
        :type: Audience
        """

        self._audience = audience

    @property
    def tracking(self):
        """Gets the tracking of this CreateCampaign.  # noqa: E501


        :return: The tracking of this CreateCampaign.  # noqa: E501
        :rtype: Tracking
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this CreateCampaign.


        :param tracking: The tracking of this CreateCampaign.  # noqa: E501
        :type: Tracking
        """

        self._tracking = tracking

    @property
    def sender(self):
        """Gets the sender of this CreateCampaign.  # noqa: E501


        :return: The sender of this CreateCampaign.  # noqa: E501
        :rtype: Sender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this CreateCampaign.


        :param sender: The sender of this CreateCampaign.  # noqa: E501
        :type: Sender
        """

        self._sender = sender

    @property
    def reply_to_email(self):
        """Gets the reply_to_email of this CreateCampaign.  # noqa: E501

        Specify a different reply-to email address than the sender  # noqa: E501

        :return: The reply_to_email of this CreateCampaign.  # noqa: E501
        :rtype: str
        """
        return self._reply_to_email

    @reply_to_email.setter
    def reply_to_email(self, reply_to_email):
        """Sets the reply_to_email of this CreateCampaign.

        Specify a different reply-to email address than the sender  # noqa: E501

        :param reply_to_email: The reply_to_email of this CreateCampaign.  # noqa: E501
        :type: str
        """

        self._reply_to_email = reply_to_email

    @property
    def content(self):
        """Gets the content of this CreateCampaign.  # noqa: E501


        :return: The content of this CreateCampaign.  # noqa: E501
        :rtype: CampaignContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CreateCampaign.


        :param content: The content of this CreateCampaign.  # noqa: E501
        :type: CampaignContent
        """

        self._content = content

    @property
    def editor(self):
        """Gets the editor of this CreateCampaign.  # noqa: E501


        :return: The editor of this CreateCampaign.  # noqa: E501
        :rtype: str
        """
        return self._editor

    @editor.setter
    def editor(self, editor):
        """Sets the editor of this CreateCampaign.


        :param editor: The editor of this CreateCampaign.  # noqa: E501
        :type: str
        """
        allowed_values = ["html", "bee"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and editor not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `editor` ({0}), must be one of {1}"  # noqa: E501
                .format(editor, allowed_values)
            )

        self._editor = editor

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
        if not isinstance(other, CreateCampaign):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateCampaign):
            return True

        return self.to_dict() != other.to_dict()
