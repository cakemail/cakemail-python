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


class CampaignSummaryResponse(object):
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
        'audience': 'AudienceSummaryResponse',
        'type': 'str',
        'created_on': 'int',
        'scheduled_for': 'int',
        'scheduled_on': 'int',
        'sender': 'ListSenderResponse',
        'next_building_step': 'str',
        'status': 'str',
        'suspended': 'bool',
        'web_email_link': 'str',
        'thumbnail_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'audience': 'audience',
        'type': 'type',
        'created_on': 'created_on',
        'scheduled_for': 'scheduled_for',
        'scheduled_on': 'scheduled_on',
        'sender': 'sender',
        'next_building_step': 'next_building_step',
        'status': 'status',
        'suspended': 'suspended',
        'web_email_link': 'web_email_link',
        'thumbnail_url': 'thumbnail_url'
    }

    def __init__(self, id=None, name=None, audience=None, type=None, created_on=None, scheduled_for=None, scheduled_on=None, sender=None, next_building_step=None, status=None, suspended=None, web_email_link=None, thumbnail_url=None, local_vars_configuration=None):  # noqa: E501
        """CampaignSummaryResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._audience = None
        self._type = None
        self._created_on = None
        self._scheduled_for = None
        self._scheduled_on = None
        self._sender = None
        self._next_building_step = None
        self._status = None
        self._suspended = None
        self._web_email_link = None
        self._thumbnail_url = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if audience is not None:
            self.audience = audience
        if type is not None:
            self.type = type
        if created_on is not None:
            self.created_on = created_on
        if scheduled_for is not None:
            self.scheduled_for = scheduled_for
        if scheduled_on is not None:
            self.scheduled_on = scheduled_on
        if sender is not None:
            self.sender = sender
        if next_building_step is not None:
            self.next_building_step = next_building_step
        if status is not None:
            self.status = status
        if suspended is not None:
            self.suspended = suspended
        if web_email_link is not None:
            self.web_email_link = web_email_link
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url

    @property
    def id(self):
        """Gets the id of this CampaignSummaryResponse.  # noqa: E501


        :return: The id of this CampaignSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CampaignSummaryResponse.


        :param id: The id of this CampaignSummaryResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this CampaignSummaryResponse.  # noqa: E501


        :return: The name of this CampaignSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CampaignSummaryResponse.


        :param name: The name of this CampaignSummaryResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def audience(self):
        """Gets the audience of this CampaignSummaryResponse.  # noqa: E501


        :return: The audience of this CampaignSummaryResponse.  # noqa: E501
        :rtype: AudienceSummaryResponse
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this CampaignSummaryResponse.


        :param audience: The audience of this CampaignSummaryResponse.  # noqa: E501
        :type: AudienceSummaryResponse
        """

        self._audience = audience

    @property
    def type(self):
        """Gets the type of this CampaignSummaryResponse.  # noqa: E501


        :return: The type of this CampaignSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CampaignSummaryResponse.


        :param type: The type of this CampaignSummaryResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["standard", "recurring", "absplit"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def created_on(self):
        """Gets the created_on of this CampaignSummaryResponse.  # noqa: E501


        :return: The created_on of this CampaignSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this CampaignSummaryResponse.


        :param created_on: The created_on of this CampaignSummaryResponse.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def scheduled_for(self):
        """Gets the scheduled_for of this CampaignSummaryResponse.  # noqa: E501


        :return: The scheduled_for of this CampaignSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_for

    @scheduled_for.setter
    def scheduled_for(self, scheduled_for):
        """Sets the scheduled_for of this CampaignSummaryResponse.


        :param scheduled_for: The scheduled_for of this CampaignSummaryResponse.  # noqa: E501
        :type: int
        """

        self._scheduled_for = scheduled_for

    @property
    def scheduled_on(self):
        """Gets the scheduled_on of this CampaignSummaryResponse.  # noqa: E501


        :return: The scheduled_on of this CampaignSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_on

    @scheduled_on.setter
    def scheduled_on(self, scheduled_on):
        """Sets the scheduled_on of this CampaignSummaryResponse.


        :param scheduled_on: The scheduled_on of this CampaignSummaryResponse.  # noqa: E501
        :type: int
        """

        self._scheduled_on = scheduled_on

    @property
    def sender(self):
        """Gets the sender of this CampaignSummaryResponse.  # noqa: E501


        :return: The sender of this CampaignSummaryResponse.  # noqa: E501
        :rtype: ListSenderResponse
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this CampaignSummaryResponse.


        :param sender: The sender of this CampaignSummaryResponse.  # noqa: E501
        :type: ListSenderResponse
        """

        self._sender = sender

    @property
    def next_building_step(self):
        """Gets the next_building_step of this CampaignSummaryResponse.  # noqa: E501


        :return: The next_building_step of this CampaignSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_building_step

    @next_building_step.setter
    def next_building_step(self, next_building_step):
        """Sets the next_building_step of this CampaignSummaryResponse.


        :param next_building_step: The next_building_step of this CampaignSummaryResponse.  # noqa: E501
        :type: str
        """

        self._next_building_step = next_building_step

    @property
    def status(self):
        """Gets the status of this CampaignSummaryResponse.  # noqa: E501


        :return: The status of this CampaignSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CampaignSummaryResponse.


        :param status: The status of this CampaignSummaryResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "delivering", "delivered", "archived", "deleted", "incomplete", "scheduled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def suspended(self):
        """Gets the suspended of this CampaignSummaryResponse.  # noqa: E501


        :return: The suspended of this CampaignSummaryResponse.  # noqa: E501
        :rtype: bool
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        """Sets the suspended of this CampaignSummaryResponse.


        :param suspended: The suspended of this CampaignSummaryResponse.  # noqa: E501
        :type: bool
        """

        self._suspended = suspended

    @property
    def web_email_link(self):
        """Gets the web_email_link of this CampaignSummaryResponse.  # noqa: E501


        :return: The web_email_link of this CampaignSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._web_email_link

    @web_email_link.setter
    def web_email_link(self, web_email_link):
        """Sets the web_email_link of this CampaignSummaryResponse.


        :param web_email_link: The web_email_link of this CampaignSummaryResponse.  # noqa: E501
        :type: str
        """

        self._web_email_link = web_email_link

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this CampaignSummaryResponse.  # noqa: E501


        :return: The thumbnail_url of this CampaignSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this CampaignSummaryResponse.


        :param thumbnail_url: The thumbnail_url of this CampaignSummaryResponse.  # noqa: E501
        :type: str
        """

        self._thumbnail_url = thumbnail_url

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
        if not isinstance(other, CampaignSummaryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignSummaryResponse):
            return True

        return self.to_dict() != other.to_dict()
