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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class TasksOperations(object):
    """TasksOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Version of the API. Constant value: "2018-03-31-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-03-31-preview"

        self.config = config

    def list(
            self, group_name, service_name, project_name, task_type=None, custom_headers=None, raw=False, **operation_config):
        """Get tasks in a service.

        The services resource is the top-level resource that represents the
        Data Migration Service. This method returns a list of tasks owned by a
        service resource. Some tasks may have a status of Unknown, which
        indicates that an error occurred while querying the status of that
        task.

        :param group_name: Name of the resource group
        :type group_name: str
        :param service_name: Name of the service
        :type service_name: str
        :param project_name: Name of the project
        :type project_name: str
        :param task_type: Filter tasks by task type
        :type task_type: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of ProjectTask
        :rtype:
         ~azure.mgmt.datamigration.models.ProjectTaskPaged[~azure.mgmt.datamigration.models.ProjectTask]
        :raises:
         :class:`ApiErrorException<azure.mgmt.datamigration.models.ApiErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'groupName': self._serialize.url("group_name", group_name, 'str'),
                    'serviceName': self._serialize.url("service_name", service_name, 'str'),
                    'projectName': self._serialize.url("project_name", project_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if task_type is not None:
                    query_parameters['taskType'] = self._serialize.query("task_type", task_type, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ApiErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.ProjectTaskPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ProjectTaskPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks'}

    def create_or_update(
            self, group_name, service_name, project_name, task_name, etag=None, properties=None, custom_headers=None, raw=False, **operation_config):
        """Create or update task.

        The tasks resource is a nested, proxy-only resource representing work
        performed by a DMS instance. The PUT method creates a new task or
        updates an existing one, although since tasks have no mutable custom
        properties, there is little reason to update an exising one.

        :param group_name: Name of the resource group
        :type group_name: str
        :param service_name: Name of the service
        :type service_name: str
        :param project_name: Name of the project
        :type project_name: str
        :param task_name: Name of the Task
        :type task_name: str
        :param etag: HTTP strong entity tag value. This is ignored if
         submitted.
        :type etag: str
        :param properties: Custom task properties
        :type properties:
         ~azure.mgmt.datamigration.models.ProjectTaskProperties
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ProjectTask or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.datamigration.models.ProjectTask or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ApiErrorException<azure.mgmt.datamigration.models.ApiErrorException>`
        """
        parameters = models.ProjectTask(etag=etag, properties=properties)

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'taskName': self._serialize.url("task_name", task_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'ProjectTask')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.ApiErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ProjectTask', response)
        if response.status_code == 201:
            deserialized = self._deserialize('ProjectTask', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName}'}

    def get(
            self, group_name, service_name, project_name, task_name, expand=None, custom_headers=None, raw=False, **operation_config):
        """Get task information.

        The tasks resource is a nested, proxy-only resource representing work
        performed by a DMS instance. The GET method retrieves information about
        a task.

        :param group_name: Name of the resource group
        :type group_name: str
        :param service_name: Name of the service
        :type service_name: str
        :param project_name: Name of the project
        :type project_name: str
        :param task_name: Name of the Task
        :type task_name: str
        :param expand: Expand the response
        :type expand: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ProjectTask or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.datamigration.models.ProjectTask or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ApiErrorException<azure.mgmt.datamigration.models.ApiErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'taskName': self._serialize.url("task_name", task_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ApiErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ProjectTask', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName}'}

    def delete(
            self, group_name, service_name, project_name, task_name, delete_running_tasks=None, custom_headers=None, raw=False, **operation_config):
        """Delete task.

        The tasks resource is a nested, proxy-only resource representing work
        performed by a DMS instance. The DELETE method deletes a task,
        canceling it first if it's running.

        :param group_name: Name of the resource group
        :type group_name: str
        :param service_name: Name of the service
        :type service_name: str
        :param project_name: Name of the project
        :type project_name: str
        :param task_name: Name of the Task
        :type task_name: str
        :param delete_running_tasks: Delete the resource even if it contains
         running tasks
        :type delete_running_tasks: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ApiErrorException<azure.mgmt.datamigration.models.ApiErrorException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'taskName': self._serialize.url("task_name", task_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if delete_running_tasks is not None:
            query_parameters['deleteRunningTasks'] = self._serialize.query("delete_running_tasks", delete_running_tasks, 'bool')
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ApiErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName}'}

    def update(
            self, group_name, service_name, project_name, task_name, etag=None, properties=None, custom_headers=None, raw=False, **operation_config):
        """Create or update task.

        The tasks resource is a nested, proxy-only resource representing work
        performed by a DMS instance. The PATCH method updates an existing task,
        but since tasks have no mutable custom properties, there is little
        reason to do so.

        :param group_name: Name of the resource group
        :type group_name: str
        :param service_name: Name of the service
        :type service_name: str
        :param project_name: Name of the project
        :type project_name: str
        :param task_name: Name of the Task
        :type task_name: str
        :param etag: HTTP strong entity tag value. This is ignored if
         submitted.
        :type etag: str
        :param properties: Custom task properties
        :type properties:
         ~azure.mgmt.datamigration.models.ProjectTaskProperties
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ProjectTask or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.datamigration.models.ProjectTask or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ApiErrorException<azure.mgmt.datamigration.models.ApiErrorException>`
        """
        parameters = models.ProjectTask(etag=etag, properties=properties)

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'taskName': self._serialize.url("task_name", task_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'ProjectTask')

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ApiErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ProjectTask', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName}'}

    def cancel(
            self, group_name, service_name, project_name, task_name, custom_headers=None, raw=False, **operation_config):
        """Cancel a task.

        The tasks resource is a nested, proxy-only resource representing work
        performed by a DMS instance. This method cancels a task if it's
        currently queued or running.

        :param group_name: Name of the resource group
        :type group_name: str
        :param service_name: Name of the service
        :type service_name: str
        :param project_name: Name of the project
        :type project_name: str
        :param task_name: Name of the Task
        :type task_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ProjectTask or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.datamigration.models.ProjectTask or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ApiErrorException<azure.mgmt.datamigration.models.ApiErrorException>`
        """
        # Construct URL
        url = self.cancel.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'taskName': self._serialize.url("task_name", task_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ApiErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ProjectTask', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    cancel.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName}/cancel'}
