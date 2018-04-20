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

from .proxy_resource import ProxyResource


class RestorableDroppedDatabase(ProxyResource):
    """A restorable dropped database.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar location: The geo-location where the resource lives
    :vartype location: str
    :ivar database_name: The name of the database
    :vartype database_name: str
    :ivar edition: The edition of the database
    :vartype edition: str
    :ivar max_size_bytes: The max size in bytes of the database
    :vartype max_size_bytes: str
    :ivar service_level_objective: The service level objective name of the
     database
    :vartype service_level_objective: str
    :ivar elastic_pool_name: The elastic pool name of the database
    :vartype elastic_pool_name: str
    :ivar creation_date: The creation date of the database (ISO8601 format)
    :vartype creation_date: datetime
    :ivar deletion_date: The deletion date of the database (ISO8601 format)
    :vartype deletion_date: datetime
    :ivar earliest_restore_date: The earliest restore date of the database
     (ISO8601 format)
    :vartype earliest_restore_date: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'database_name': {'readonly': True},
        'edition': {'readonly': True},
        'max_size_bytes': {'readonly': True},
        'service_level_objective': {'readonly': True},
        'elastic_pool_name': {'readonly': True},
        'creation_date': {'readonly': True},
        'deletion_date': {'readonly': True},
        'earliest_restore_date': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'database_name': {'key': 'properties.databaseName', 'type': 'str'},
        'edition': {'key': 'properties.edition', 'type': 'str'},
        'max_size_bytes': {'key': 'properties.maxSizeBytes', 'type': 'str'},
        'service_level_objective': {'key': 'properties.serviceLevelObjective', 'type': 'str'},
        'elastic_pool_name': {'key': 'properties.elasticPoolName', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'deletion_date': {'key': 'properties.deletionDate', 'type': 'iso-8601'},
        'earliest_restore_date': {'key': 'properties.earliestRestoreDate', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs) -> None:
        super(RestorableDroppedDatabase, self).__init__(**kwargs)
        self.location = None
        self.database_name = None
        self.edition = None
        self.max_size_bytes = None
        self.service_level_objective = None
        self.elastic_pool_name = None
        self.creation_date = None
        self.deletion_date = None
        self.earliest_restore_date = None
