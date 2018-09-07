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


class EventsBrowserTimingInfo(object):
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
        'url_path': 'str',
        'url_host': 'str',
        'name': 'str',
        'url': 'str',
        'total_duration': 'int',
        'performance_bucket': 'str',
        'network_duration': 'int',
        'send_duration': 'int',
        'receive_duration': 'int',
        'processing_duration': 'int'
    }

    attribute_map = {
        'url_path': 'urlPath',
        'url_host': 'urlHost',
        'name': 'name',
        'url': 'url',
        'total_duration': 'totalDuration',
        'performance_bucket': 'performanceBucket',
        'network_duration': 'networkDuration',
        'send_duration': 'sendDuration',
        'receive_duration': 'receiveDuration',
        'processing_duration': 'processingDuration'
    }

    def __init__(self, url_path=None, url_host=None, name=None, url=None, total_duration=None, performance_bucket=None, network_duration=None, send_duration=None, receive_duration=None, processing_duration=None):  # noqa: E501
        """EventsBrowserTimingInfo - a model defined in Swagger"""  # noqa: E501

        self._url_path = None
        self._url_host = None
        self._name = None
        self._url = None
        self._total_duration = None
        self._performance_bucket = None
        self._network_duration = None
        self._send_duration = None
        self._receive_duration = None
        self._processing_duration = None
        self.discriminator = None

        if url_path is not None:
            self.url_path = url_path
        if url_host is not None:
            self.url_host = url_host
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if total_duration is not None:
            self.total_duration = total_duration
        if performance_bucket is not None:
            self.performance_bucket = performance_bucket
        if network_duration is not None:
            self.network_duration = network_duration
        if send_duration is not None:
            self.send_duration = send_duration
        if receive_duration is not None:
            self.receive_duration = receive_duration
        if processing_duration is not None:
            self.processing_duration = processing_duration

    @property
    def url_path(self):
        """Gets the url_path of this EventsBrowserTimingInfo.  # noqa: E501

        The path of the URL  # noqa: E501

        :return: The url_path of this EventsBrowserTimingInfo.  # noqa: E501
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """Sets the url_path of this EventsBrowserTimingInfo.

        The path of the URL  # noqa: E501

        :param url_path: The url_path of this EventsBrowserTimingInfo.  # noqa: E501
        :type: str
        """

        self._url_path = url_path

    @property
    def url_host(self):
        """Gets the url_host of this EventsBrowserTimingInfo.  # noqa: E501

        The host of the URL  # noqa: E501

        :return: The url_host of this EventsBrowserTimingInfo.  # noqa: E501
        :rtype: str
        """
        return self._url_host

    @url_host.setter
    def url_host(self, url_host):
        """Sets the url_host of this EventsBrowserTimingInfo.

        The host of the URL  # noqa: E501

        :param url_host: The url_host of this EventsBrowserTimingInfo.  # noqa: E501
        :type: str
        """

        self._url_host = url_host

    @property
    def name(self):
        """Gets the name of this EventsBrowserTimingInfo.  # noqa: E501

        The name of the page  # noqa: E501

        :return: The name of this EventsBrowserTimingInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventsBrowserTimingInfo.

        The name of the page  # noqa: E501

        :param name: The name of this EventsBrowserTimingInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this EventsBrowserTimingInfo.  # noqa: E501

        The url of the page  # noqa: E501

        :return: The url of this EventsBrowserTimingInfo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this EventsBrowserTimingInfo.

        The url of the page  # noqa: E501

        :param url: The url of this EventsBrowserTimingInfo.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def total_duration(self):
        """Gets the total_duration of this EventsBrowserTimingInfo.  # noqa: E501

        The total duration of the load  # noqa: E501

        :return: The total_duration of this EventsBrowserTimingInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_duration

    @total_duration.setter
    def total_duration(self, total_duration):
        """Sets the total_duration of this EventsBrowserTimingInfo.

        The total duration of the load  # noqa: E501

        :param total_duration: The total_duration of this EventsBrowserTimingInfo.  # noqa: E501
        :type: int
        """

        self._total_duration = total_duration

    @property
    def performance_bucket(self):
        """Gets the performance_bucket of this EventsBrowserTimingInfo.  # noqa: E501

        The performance bucket of the load  # noqa: E501

        :return: The performance_bucket of this EventsBrowserTimingInfo.  # noqa: E501
        :rtype: str
        """
        return self._performance_bucket

    @performance_bucket.setter
    def performance_bucket(self, performance_bucket):
        """Sets the performance_bucket of this EventsBrowserTimingInfo.

        The performance bucket of the load  # noqa: E501

        :param performance_bucket: The performance_bucket of this EventsBrowserTimingInfo.  # noqa: E501
        :type: str
        """

        self._performance_bucket = performance_bucket

    @property
    def network_duration(self):
        """Gets the network_duration of this EventsBrowserTimingInfo.  # noqa: E501

        The network duration of the load  # noqa: E501

        :return: The network_duration of this EventsBrowserTimingInfo.  # noqa: E501
        :rtype: int
        """
        return self._network_duration

    @network_duration.setter
    def network_duration(self, network_duration):
        """Sets the network_duration of this EventsBrowserTimingInfo.

        The network duration of the load  # noqa: E501

        :param network_duration: The network_duration of this EventsBrowserTimingInfo.  # noqa: E501
        :type: int
        """

        self._network_duration = network_duration

    @property
    def send_duration(self):
        """Gets the send_duration of this EventsBrowserTimingInfo.  # noqa: E501

        The send duration of the load  # noqa: E501

        :return: The send_duration of this EventsBrowserTimingInfo.  # noqa: E501
        :rtype: int
        """
        return self._send_duration

    @send_duration.setter
    def send_duration(self, send_duration):
        """Sets the send_duration of this EventsBrowserTimingInfo.

        The send duration of the load  # noqa: E501

        :param send_duration: The send_duration of this EventsBrowserTimingInfo.  # noqa: E501
        :type: int
        """

        self._send_duration = send_duration

    @property
    def receive_duration(self):
        """Gets the receive_duration of this EventsBrowserTimingInfo.  # noqa: E501

        The receive duration of the load  # noqa: E501

        :return: The receive_duration of this EventsBrowserTimingInfo.  # noqa: E501
        :rtype: int
        """
        return self._receive_duration

    @receive_duration.setter
    def receive_duration(self, receive_duration):
        """Sets the receive_duration of this EventsBrowserTimingInfo.

        The receive duration of the load  # noqa: E501

        :param receive_duration: The receive_duration of this EventsBrowserTimingInfo.  # noqa: E501
        :type: int
        """

        self._receive_duration = receive_duration

    @property
    def processing_duration(self):
        """Gets the processing_duration of this EventsBrowserTimingInfo.  # noqa: E501

        The processing duration of the load  # noqa: E501

        :return: The processing_duration of this EventsBrowserTimingInfo.  # noqa: E501
        :rtype: int
        """
        return self._processing_duration

    @processing_duration.setter
    def processing_duration(self, processing_duration):
        """Sets the processing_duration of this EventsBrowserTimingInfo.

        The processing duration of the load  # noqa: E501

        :param processing_duration: The processing_duration of this EventsBrowserTimingInfo.  # noqa: E501
        :type: int
        """

        self._processing_duration = processing_duration

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
        if not isinstance(other, EventsBrowserTimingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
