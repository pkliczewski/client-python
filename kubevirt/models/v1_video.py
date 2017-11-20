# coding: utf-8

"""
    KubeVirt API, 

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1Video(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'heads': 'int',
        'ram': 'int',
        'type': 'str',
        'v_ram': 'int',
        'vga_mem': 'int'
    }

    attribute_map = {
        'heads': 'heads',
        'ram': 'ram',
        'type': 'type',
        'v_ram': 'vRam',
        'vga_mem': 'vgaMem'
    }

    def __init__(self, heads=None, ram=None, type=None, v_ram=None, vga_mem=None):
        """
        V1Video - a model defined in Swagger
        """

        self._heads = None
        self._ram = None
        self._type = None
        self._v_ram = None
        self._vga_mem = None

        if heads is not None:
          self.heads = heads
        if ram is not None:
          self.ram = ram
        self.type = type
        if v_ram is not None:
          self.v_ram = v_ram
        if vga_mem is not None:
          self.vga_mem = vga_mem

    @property
    def heads(self):
        """
        Gets the heads of this V1Video.

        :return: The heads of this V1Video.
        :rtype: int
        """
        return self._heads

    @heads.setter
    def heads(self, heads):
        """
        Sets the heads of this V1Video.

        :param heads: The heads of this V1Video.
        :type: int
        """

        self._heads = heads

    @property
    def ram(self):
        """
        Gets the ram of this V1Video.

        :return: The ram of this V1Video.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """
        Sets the ram of this V1Video.

        :param ram: The ram of this V1Video.
        :type: int
        """

        self._ram = ram

    @property
    def type(self):
        """
        Gets the type of this V1Video.

        :return: The type of this V1Video.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1Video.

        :param type: The type of this V1Video.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def v_ram(self):
        """
        Gets the v_ram of this V1Video.

        :return: The v_ram of this V1Video.
        :rtype: int
        """
        return self._v_ram

    @v_ram.setter
    def v_ram(self, v_ram):
        """
        Sets the v_ram of this V1Video.

        :param v_ram: The v_ram of this V1Video.
        :type: int
        """

        self._v_ram = v_ram

    @property
    def vga_mem(self):
        """
        Gets the vga_mem of this V1Video.

        :return: The vga_mem of this V1Video.
        :rtype: int
        """
        return self._vga_mem

    @vga_mem.setter
    def vga_mem(self, vga_mem):
        """
        Sets the vga_mem of this V1Video.

        :param vga_mem: The vga_mem of this V1Video.
        :type: int
        """

        self._vga_mem = vga_mem

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1Video):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other