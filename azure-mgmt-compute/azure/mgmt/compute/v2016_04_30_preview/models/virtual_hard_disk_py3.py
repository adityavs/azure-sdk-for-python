# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualHardDisk(Model):
    """Describes the uri of a disk.

    :param uri: Specifies the virtual hard disk's uri.
    :type uri: str
    """

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'},
    }

    def __init__(self, *, uri: str=None, **kwargs) -> None:
        super(VirtualHardDisk, self).__init__(**kwargs)
        self.uri = uri
