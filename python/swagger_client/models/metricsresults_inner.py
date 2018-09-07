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

from swagger_client.models.metrics_result import MetricsResult  # noqa: F401,E501


class MetricsresultsInner(object):
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
        'id': 'str',
        'status': 'int',
        'body': 'MetricsResult'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'body': 'body'
    }

    def __init__(self, id=None, status=None, body=None):  # noqa: E501
        """MetricsresultsInner - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._status = None
        self._body = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.body = body

    @property
    def id(self):
        """Gets the id of this MetricsresultsInner.  # noqa: E501

        The specified ID for this metric.  # noqa: E501

        :return: The id of this MetricsresultsInner.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetricsresultsInner.

        The specified ID for this metric.  # noqa: E501

        :param id: The id of this MetricsresultsInner.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status(self):
        """Gets the status of this MetricsresultsInner.  # noqa: E501

        The HTTP status code of this metric query.  # noqa: E501

        :return: The status of this MetricsresultsInner.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MetricsresultsInner.

        The HTTP status code of this metric query.  # noqa: E501

        :param status: The status of this MetricsresultsInner.  # noqa: E501
        :type: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def body(self):
        """Gets the body of this MetricsresultsInner.  # noqa: E501

        The results of this metric query.  # noqa: E501

        :return: The body of this MetricsresultsInner.  # noqa: E501
        :rtype: MetricsResult
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this MetricsresultsInner.

        The results of this metric query.  # noqa: E501

        :param body: The body of this MetricsresultsInner.  # noqa: E501
        :type: MetricsResult
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

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
        if not isinstance(other, MetricsresultsInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
