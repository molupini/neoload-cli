# coding: utf-8

"""
    NeoLoad API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ElementDefinition(object):
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
        'id': 'str',
        'name': 'str',
        'path': 'list[str]',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'path': 'path',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, path=None, type=None, local_vars_configuration=None):  # noqa: E501
        """ElementDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._path = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this ElementDefinition.  # noqa: E501

        Unique identifier of the element.  # noqa: E501

        :return: The id of this ElementDefinition.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ElementDefinition.

        Unique identifier of the element.  # noqa: E501

        :param id: The id of this ElementDefinition.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ElementDefinition.  # noqa: E501

        Name of the element.  # noqa: E501

        :return: The name of this ElementDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ElementDefinition.

        Name of the element.  # noqa: E501

        :param name: The name of this ElementDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this ElementDefinition.  # noqa: E501

        Full path of the element including the element itself.  # noqa: E501

        :return: The path of this ElementDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ElementDefinition.

        Full path of the element including the element itself.  # noqa: E501

        :param path: The path of this ElementDefinition.  # noqa: E501
        :type: list[str]
        """

        self._path = path

    @property
    def type(self):
        """Gets the type of this ElementDefinition.  # noqa: E501

        Type of the element.  # noqa: E501

        :return: The type of this ElementDefinition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ElementDefinition.

        Type of the element.  # noqa: E501

        :param type: The type of this ElementDefinition.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, ElementDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElementDefinition):
            return True

        return self.to_dict() != other.to_dict()
