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


class ListFullResponse(object):
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
        'name': 'str',
        'status': 'str',
        'policy_accepted': 'bool',
        'language': 'str',
        'created_on': 'int',
        'default_sender': 'ListSenderResponse',
        'redirections': 'ListRedirectionsResponse',
        'pages': 'ListPagesResponse',
        'webhook': 'ListWebhookResponse'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'policy_accepted': 'policy_accepted',
        'language': 'language',
        'created_on': 'created_on',
        'default_sender': 'default_sender',
        'redirections': 'redirections',
        'pages': 'pages',
        'webhook': 'webhook'
    }

    def __init__(self, id=None, name=None, status=None, policy_accepted=False, language=None, created_on=None, default_sender=None, redirections=None, pages=None, webhook=None, local_vars_configuration=None):  # noqa: E501
        """ListFullResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._status = None
        self._policy_accepted = None
        self._language = None
        self._created_on = None
        self._default_sender = None
        self._redirections = None
        self._pages = None
        self._webhook = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        if policy_accepted is not None:
            self.policy_accepted = policy_accepted
        self.language = language
        self.created_on = created_on
        self.default_sender = default_sender
        self.redirections = redirections
        self.pages = pages
        self.webhook = webhook

    @property
    def id(self):
        """Gets the id of this ListFullResponse.  # noqa: E501


        :return: The id of this ListFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListFullResponse.


        :param id: The id of this ListFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ListFullResponse.  # noqa: E501


        :return: The name of this ListFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListFullResponse.


        :param name: The name of this ListFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this ListFullResponse.  # noqa: E501


        :return: The status of this ListFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListFullResponse.


        :param status: The status of this ListFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def policy_accepted(self):
        """Gets the policy_accepted of this ListFullResponse.  # noqa: E501


        :return: The policy_accepted of this ListFullResponse.  # noqa: E501
        :rtype: bool
        """
        return self._policy_accepted

    @policy_accepted.setter
    def policy_accepted(self, policy_accepted):
        """Sets the policy_accepted of this ListFullResponse.


        :param policy_accepted: The policy_accepted of this ListFullResponse.  # noqa: E501
        :type: bool
        """

        self._policy_accepted = policy_accepted

    @property
    def language(self):
        """Gets the language of this ListFullResponse.  # noqa: E501


        :return: The language of this ListFullResponse.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ListFullResponse.


        :param language: The language of this ListFullResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and language is None:  # noqa: E501
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def created_on(self):
        """Gets the created_on of this ListFullResponse.  # noqa: E501


        :return: The created_on of this ListFullResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ListFullResponse.


        :param created_on: The created_on of this ListFullResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and created_on is None:  # noqa: E501
            raise ValueError("Invalid value for `created_on`, must not be `None`")  # noqa: E501

        self._created_on = created_on

    @property
    def default_sender(self):
        """Gets the default_sender of this ListFullResponse.  # noqa: E501


        :return: The default_sender of this ListFullResponse.  # noqa: E501
        :rtype: ListSenderResponse
        """
        return self._default_sender

    @default_sender.setter
    def default_sender(self, default_sender):
        """Sets the default_sender of this ListFullResponse.


        :param default_sender: The default_sender of this ListFullResponse.  # noqa: E501
        :type: ListSenderResponse
        """
        if self.local_vars_configuration.client_side_validation and default_sender is None:  # noqa: E501
            raise ValueError("Invalid value for `default_sender`, must not be `None`")  # noqa: E501

        self._default_sender = default_sender

    @property
    def redirections(self):
        """Gets the redirections of this ListFullResponse.  # noqa: E501


        :return: The redirections of this ListFullResponse.  # noqa: E501
        :rtype: ListRedirectionsResponse
        """
        return self._redirections

    @redirections.setter
    def redirections(self, redirections):
        """Sets the redirections of this ListFullResponse.


        :param redirections: The redirections of this ListFullResponse.  # noqa: E501
        :type: ListRedirectionsResponse
        """
        if self.local_vars_configuration.client_side_validation and redirections is None:  # noqa: E501
            raise ValueError("Invalid value for `redirections`, must not be `None`")  # noqa: E501

        self._redirections = redirections

    @property
    def pages(self):
        """Gets the pages of this ListFullResponse.  # noqa: E501


        :return: The pages of this ListFullResponse.  # noqa: E501
        :rtype: ListPagesResponse
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this ListFullResponse.


        :param pages: The pages of this ListFullResponse.  # noqa: E501
        :type: ListPagesResponse
        """
        if self.local_vars_configuration.client_side_validation and pages is None:  # noqa: E501
            raise ValueError("Invalid value for `pages`, must not be `None`")  # noqa: E501

        self._pages = pages

    @property
    def webhook(self):
        """Gets the webhook of this ListFullResponse.  # noqa: E501


        :return: The webhook of this ListFullResponse.  # noqa: E501
        :rtype: ListWebhookResponse
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this ListFullResponse.


        :param webhook: The webhook of this ListFullResponse.  # noqa: E501
        :type: ListWebhookResponse
        """
        if self.local_vars_configuration.client_side_validation and webhook is None:  # noqa: E501
            raise ValueError("Invalid value for `webhook`, must not be `None`")  # noqa: E501

        self._webhook = webhook

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
        if not isinstance(other, ListFullResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListFullResponse):
            return True

        return self.to_dict() != other.to_dict()
