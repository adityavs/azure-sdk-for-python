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


class TagList(Model):
    """TagList.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar tags:
    :vartype tags:
     list[~azure.cognitiveservices.vision.customvision.training.models.Tag]
    :ivar total_tagged_images:
    :vartype total_tagged_images: int
    :ivar total_untagged_images:
    :vartype total_untagged_images: int
    """

    _validation = {
        'tags': {'readonly': True},
        'total_tagged_images': {'readonly': True},
        'total_untagged_images': {'readonly': True},
    }

    _attribute_map = {
        'tags': {'key': 'Tags', 'type': '[Tag]'},
        'total_tagged_images': {'key': 'TotalTaggedImages', 'type': 'int'},
        'total_untagged_images': {'key': 'TotalUntaggedImages', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(TagList, self).__init__(**kwargs)
        self.tags = None
        self.total_tagged_images = None
        self.total_untagged_images = None
