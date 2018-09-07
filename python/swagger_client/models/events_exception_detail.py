# coding: utf-8

"""
    AI public API

    This API exposes AI metric & event information and associated metadata  # noqa: E501

    OpenAPI spec version: v1
    Contact: aiapi@microsoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.events_exception_details_parsed_stack import EventsExceptionDetailsParsedStack  # noqa: F401,E501


class EventsExceptionDetail(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'severity_level': 'str',
        'outer_id': 'str',
        'message': 'str',
        'type': 'str',
        'id': 'str',
        'parsed_stack': 'list[EventsExceptionDetailsParsedStack]'
    }

    attribute_map = {
        'severity_level': 'severityLevel',
        'outer_id': 'outerId',
        'message': 'message',
        'type': 'type',
        'id': 'id',
        'parsed_stack': 'parsedStack'
    }

    def __init__(self, severity_level=None, outer_id=None, message=None, type=None, id=None, parsed_stack=None):  # noqa: E501
        """EventsExceptionDetail - a model defined in Swagger"""  # noqa: E501

        self._severity_level = None
        self._outer_id = None
        self._message = None
        self._type = None
        self._id = None
        self._parsed_stack = None
        self.discriminator = None

        if severity_level is not None:
            self.severity_level = severity_level
        if outer_id is not None:
            self.outer_id = outer_id
        if message is not None:
            self.message = message
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if parsed_stack is not None:
            self.parsed_stack = parsed_stack

    @property
    def severity_level(self):
        """Gets the severity_level of this EventsExceptionDetail.  # noqa: E501

        The severity level of the exception detail  # noqa: E501

        :return: The severity_level of this EventsExceptionDetail.  # noqa: E501
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        """Sets the severity_level of this EventsExceptionDetail.

        The severity level of the exception detail  # noqa: E501

        :param severity_level: The severity_level of this EventsExceptionDetail.  # noqa: E501
        :type: str
        """

        self._severity_level = severity_level

    @property
    def outer_id(self):
        """Gets the outer_id of this EventsExceptionDetail.  # noqa: E501

        The outer ID of the exception detail  # noqa: E501

        :return: The outer_id of this EventsExceptionDetail.  # noqa: E501
        :rtype: str
        """
        return self._outer_id

    @outer_id.setter
    def outer_id(self, outer_id):
        """Sets the outer_id of this EventsExceptionDetail.

        The outer ID of the exception detail  # noqa: E501

        :param outer_id: The outer_id of this EventsExceptionDetail.  # noqa: E501
        :type: str
        """

        self._outer_id = outer_id

    @property
    def message(self):
        """Gets the message of this EventsExceptionDetail.  # noqa: E501

        The message of the exception detail  # noqa: E501

        :return: The message of this EventsExceptionDetail.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this EventsExceptionDetail.

        The message of the exception detail  # noqa: E501

        :param message: The message of this EventsExceptionDetail.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def type(self):
        """Gets the type of this EventsExceptionDetail.  # noqa: E501

        The type of the exception detail  # noqa: E501

        :return: The type of this EventsExceptionDetail.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EventsExceptionDetail.

        The type of the exception detail  # noqa: E501

        :param type: The type of this EventsExceptionDetail.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this EventsExceptionDetail.  # noqa: E501

        The ID of the exception detail  # noqa: E501

        :return: The id of this EventsExceptionDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventsExceptionDetail.

        The ID of the exception detail  # noqa: E501

        :param id: The id of this EventsExceptionDetail.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def parsed_stack(self):
        """Gets the parsed_stack of this EventsExceptionDetail.  # noqa: E501

        The parsed stack  # noqa: E501

        :return: The parsed_stack of this EventsExceptionDetail.  # noqa: E501
        :rtype: list[EventsExceptionDetailsParsedStack]
        """
        return self._parsed_stack

    @parsed_stack.setter
    def parsed_stack(self, parsed_stack):
        """Sets the parsed_stack of this EventsExceptionDetail.

        The parsed stack  # noqa: E501

        :param parsed_stack: The parsed_stack of this EventsExceptionDetail.  # noqa: E501
        :type: list[EventsExceptionDetailsParsedStack]
        """

        self._parsed_stack = parsed_stack

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, EventsExceptionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
