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

from swagger_client.models.metrics_segment_info import MetricsSegmentInfo  # noqa: F401,E501


class MetricsResultInfo(object):
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
        'start': 'str',
        'end': 'str',
        'interval': 'str',
        'segments': 'list[MetricsSegmentInfo]'
    }

    attribute_map = {
        'start': 'start',
        'end': 'end',
        'interval': 'interval',
        'segments': 'segments'
    }

    def __init__(self, start=None, end=None, interval=None, segments=None):  # noqa: E501
        """MetricsResultInfo - a model defined in Swagger"""  # noqa: E501

        self._start = None
        self._end = None
        self._interval = None
        self._segments = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if interval is not None:
            self.interval = interval
        if segments is not None:
            self.segments = segments

    @property
    def start(self):
        """Gets the start of this MetricsResultInfo.  # noqa: E501

        Start time of the metric.  # noqa: E501

        :return: The start of this MetricsResultInfo.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this MetricsResultInfo.

        Start time of the metric.  # noqa: E501

        :param start: The start of this MetricsResultInfo.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this MetricsResultInfo.  # noqa: E501

        Start time of the metric.  # noqa: E501

        :return: The end of this MetricsResultInfo.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this MetricsResultInfo.

        Start time of the metric.  # noqa: E501

        :param end: The end of this MetricsResultInfo.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def interval(self):
        """Gets the interval of this MetricsResultInfo.  # noqa: E501

        The interval used to segment the metric data.  # noqa: E501

        :return: The interval of this MetricsResultInfo.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this MetricsResultInfo.

        The interval used to segment the metric data.  # noqa: E501

        :param interval: The interval of this MetricsResultInfo.  # noqa: E501
        :type: str
        """

        self._interval = interval

    @property
    def segments(self):
        """Gets the segments of this MetricsResultInfo.  # noqa: E501

        Segmented metric data (if segmented).  # noqa: E501

        :return: The segments of this MetricsResultInfo.  # noqa: E501
        :rtype: list[MetricsSegmentInfo]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this MetricsResultInfo.

        Segmented metric data (if segmented).  # noqa: E501

        :param segments: The segments of this MetricsResultInfo.  # noqa: E501
        :type: list[MetricsSegmentInfo]
        """

        self._segments = segments

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
        if not isinstance(other, MetricsResultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
