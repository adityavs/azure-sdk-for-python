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


class PerformanceCountersSettings(Model):
    """Performance counters reporting settings.

    All required parameters must be populated in order to send to Azure.

    :param app_insights_reference: Required. Specifies Azure Application
     Insights information for performance counters reporting. If provided,
     Batch AI will upload node performance counters to the corresponding Azure
     Application Insights account.
    :type app_insights_reference:
     ~azure.mgmt.batchai.models.AppInsightsReference
    """

    _validation = {
        'app_insights_reference': {'required': True},
    }

    _attribute_map = {
        'app_insights_reference': {'key': 'appInsightsReference', 'type': 'AppInsightsReference'},
    }

    def __init__(self, **kwargs):
        super(PerformanceCountersSettings, self).__init__(**kwargs)
        self.app_insights_reference = kwargs.get('app_insights_reference', None)
