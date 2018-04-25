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

from .resource import Resource


class LocalNetworkGateway(Resource):
    """A common class for general resource information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param local_network_address_space: Required. Local network site address
     space.
    :type local_network_address_space:
     ~azure.mgmt.network.v2016_09_01.models.AddressSpace
    :param gateway_ip_address: IP address of local network gateway.
    :type gateway_ip_address: str
    :param bgp_settings: Local network gateway's BGP speaker settings.
    :type bgp_settings: ~azure.mgmt.network.v2016_09_01.models.BgpSettings
    :param resource_guid: The resource GUID property of the
     LocalNetworkGateway resource.
    :type resource_guid: str
    :ivar provisioning_state: The provisioning state of the
     LocalNetworkGateway resource. Possible values are: 'Updating', 'Deleting',
     and 'Failed'.
    :vartype provisioning_state: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'local_network_address_space': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'local_network_address_space': {'key': 'properties.localNetworkAddressSpace', 'type': 'AddressSpace'},
        'gateway_ip_address': {'key': 'properties.gatewayIpAddress', 'type': 'str'},
        'bgp_settings': {'key': 'properties.bgpSettings', 'type': 'BgpSettings'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LocalNetworkGateway, self).__init__(**kwargs)
        self.local_network_address_space = kwargs.get('local_network_address_space', None)
        self.gateway_ip_address = kwargs.get('gateway_ip_address', None)
        self.bgp_settings = kwargs.get('bgp_settings', None)
        self.resource_guid = kwargs.get('resource_guid', None)
        self.provisioning_state = None
        self.etag = kwargs.get('etag', None)
