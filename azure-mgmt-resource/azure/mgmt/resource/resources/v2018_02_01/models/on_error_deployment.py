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


class OnErrorDeployment(Model):
    """Deployment on error behavior.

    :param type: The deployment on error behavior type. Possible values are
     LastSuccessful and SpecificDeployment. Possible values include:
     'LastSuccessful', 'SpecificDeployment'
    :type type: str or
     ~azure.mgmt.resource.resources.v2018_02_01.models.OnErrorDeploymentType
    :param deployment_name: The deployment to be used on error case.
    :type deployment_name: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'OnErrorDeploymentType'},
        'deployment_name': {'key': 'deploymentName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OnErrorDeployment, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.deployment_name = kwargs.get('deployment_name', None)
