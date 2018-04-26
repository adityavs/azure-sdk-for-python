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


class JobManagerTask(Model):
    """Specifies details of a Job Manager task.

    The Job Manager task is automatically started when the job is created. The
    Batch service tries to schedule the Job Manager task before any other tasks
    in the job. When shrinking a pool, the Batch service tries to preserve
    compute nodes where Job Manager tasks are running for as long as possible
    (that is, nodes running 'normal' tasks are removed before nodes running Job
    Manager tasks). When a Job Manager task fails and needs to be restarted,
    the system tries to schedule it at the highest priority. If there are no
    idle nodes available, the system may terminate one of the running tasks in
    the pool and return it to the queue in order to make room for the Job
    Manager task to restart. Note that a Job Manager task in one job does not
    have priority over tasks in other jobs. Across jobs, only job level
    priorities are observed. For example, if a Job Manager in a priority 0 job
    needs to be restarted, it will not displace tasks of a priority 1 job.
    Batch will retry tasks when a recovery operation is triggered on a compute
    node. Examples of recovery operations include (but are not limited to) when
    an unhealthy compute node is rebooted or a compute node disappeared due to
    host failure. Retries due to recovery operations are independent of and are
    not counted against the maxTaskRetryCount. Even if the maxTaskRetryCount is
    0, an internal retry due to a recovery operation may occur. Because of
    this, all tasks should be idempotent. This means tasks need to tolerate
    being interrupted and restarted without causing any corruption or duplicate
    data. The best practice for long running tasks is to use some form of
    checkpointing.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. A string that uniquely identifies the Job Manager
     task within the job. The ID can contain any combination of alphanumeric
     characters including hyphens and underscores and cannot contain more than
     64 characters.
    :type id: str
    :param display_name: The display name of the Job Manager task. It need not
     be unique and can contain any Unicode characters up to a maximum length of
     1024.
    :type display_name: str
    :param command_line: Required. The command line of the Job Manager task.
     The command line does not run under a shell, and therefore cannot take
     advantage of shell features such as environment variable expansion. If you
     want to take advantage of such features, you should invoke the shell in
     the command line, for example using "cmd /c MyCommand" in Windows or
     "/bin/sh -c MyCommand" in Linux. If the command line refers to file paths,
     it should use a relative path (relative to the task working directory), or
     use the Batch provided environment variable
     (https://docs.microsoft.com/en-us/azure/batch/batch-compute-node-environment-variables).
    :type command_line: str
    :param container_settings: The settings for the container under which the
     Job Manager task runs. If the pool that will run this task has
     containerConfiguration set, this must be set as well. If the pool that
     will run this task doesn't have containerConfiguration set, this must not
     be set. When this is specified, all directories recursively below the
     AZ_BATCH_NODE_ROOT_DIR (the root of Azure Batch directories on the node)
     are mapped into the container, all task environment variables are mapped
     into the container, and the task command line is executed in the
     container.
    :type container_settings: ~azure.batch.models.TaskContainerSettings
    :param resource_files: A list of files that the Batch service will
     download to the compute node before running the command line. Files listed
     under this element are located in the task's working directory.
    :type resource_files: list[~azure.batch.models.ResourceFile]
    :param output_files: A list of files that the Batch service will upload
     from the compute node after running the command line. For multi-instance
     tasks, the files will only be uploaded from the compute node on which the
     primary task is executed.
    :type output_files: list[~azure.batch.models.OutputFile]
    :param environment_settings: A list of environment variable settings for
     the Job Manager task.
    :type environment_settings: list[~azure.batch.models.EnvironmentSetting]
    :param constraints: Constraints that apply to the Job Manager task.
    :type constraints: ~azure.batch.models.TaskConstraints
    :param kill_job_on_completion: Whether completion of the Job Manager task
     signifies completion of the entire job. If true, when the Job Manager task
     completes, the Batch service marks the job as complete. If any tasks are
     still running at this time (other than Job Release), those tasks are
     terminated. If false, the completion of the Job Manager task does not
     affect the job status. In this case, you should either use the
     onAllTasksComplete attribute to terminate the job, or have a client or
     user terminate the job explicitly. An example of this is if the Job
     Manager creates a set of tasks but then takes no further role in their
     execution. The default value is true. If you are using the
     onAllTasksComplete and onTaskFailure attributes to control job lifetime,
     and using the Job Manager task only to create the tasks for the job (not
     to monitor progress), then it is important to set killJobOnCompletion to
     false.
    :type kill_job_on_completion: bool
    :param user_identity: The user identity under which the Job Manager task
     runs. If omitted, the task runs as a non-administrative user unique to the
     task.
    :type user_identity: ~azure.batch.models.UserIdentity
    :param run_exclusive: Whether the Job Manager task requires exclusive use
     of the compute node where it runs. If true, no other tasks will run on the
     same compute node for as long as the Job Manager is running. If false,
     other tasks can run simultaneously with the Job Manager on a compute node.
     The Job Manager task counts normally against the node's concurrent task
     limit, so this is only relevant if the node allows multiple concurrent
     tasks. The default value is true.
    :type run_exclusive: bool
    :param application_package_references: A list of application packages that
     the Batch service will deploy to the compute node before running the
     command line. Application packages are downloaded and deployed to a shared
     directory, not the task working directory. Therefore, if a referenced
     package is already on the compute node, and is up to date, then it is not
     re-downloaded; the existing copy on the compute node is used. If a
     referenced application package cannot be installed, for example because
     the package has been deleted or because download failed, the task fails.
    :type application_package_references:
     list[~azure.batch.models.ApplicationPackageReference]
    :param authentication_token_settings: The settings for an authentication
     token that the task can use to perform Batch service operations. If this
     property is set, the Batch service provides the task with an
     authentication token which can be used to authenticate Batch service
     operations without requiring an account access key. The token is provided
     via the AZ_BATCH_AUTHENTICATION_TOKEN environment variable. The operations
     that the task can carry out using the token depend on the settings. For
     example, a task can request job permissions in order to add other tasks to
     the job, or check the status of the job or of other tasks under the job.
    :type authentication_token_settings:
     ~azure.batch.models.AuthenticationTokenSettings
    :param allow_low_priority_node: Whether the Job Manager task may run on a
     low-priority compute node. The default value is true.
    :type allow_low_priority_node: bool
    """

    _validation = {
        'id': {'required': True},
        'command_line': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'command_line': {'key': 'commandLine', 'type': 'str'},
        'container_settings': {'key': 'containerSettings', 'type': 'TaskContainerSettings'},
        'resource_files': {'key': 'resourceFiles', 'type': '[ResourceFile]'},
        'output_files': {'key': 'outputFiles', 'type': '[OutputFile]'},
        'environment_settings': {'key': 'environmentSettings', 'type': '[EnvironmentSetting]'},
        'constraints': {'key': 'constraints', 'type': 'TaskConstraints'},
        'kill_job_on_completion': {'key': 'killJobOnCompletion', 'type': 'bool'},
        'user_identity': {'key': 'userIdentity', 'type': 'UserIdentity'},
        'run_exclusive': {'key': 'runExclusive', 'type': 'bool'},
        'application_package_references': {'key': 'applicationPackageReferences', 'type': '[ApplicationPackageReference]'},
        'authentication_token_settings': {'key': 'authenticationTokenSettings', 'type': 'AuthenticationTokenSettings'},
        'allow_low_priority_node': {'key': 'allowLowPriorityNode', 'type': 'bool'},
    }

    def __init__(self, *, id: str, command_line: str, display_name: str=None, container_settings=None, resource_files=None, output_files=None, environment_settings=None, constraints=None, kill_job_on_completion: bool=None, user_identity=None, run_exclusive: bool=None, application_package_references=None, authentication_token_settings=None, allow_low_priority_node: bool=None, **kwargs) -> None:
        super(JobManagerTask, self).__init__(**kwargs)
        self.id = id
        self.display_name = display_name
        self.command_line = command_line
        self.container_settings = container_settings
        self.resource_files = resource_files
        self.output_files = output_files
        self.environment_settings = environment_settings
        self.constraints = constraints
        self.kill_job_on_completion = kill_job_on_completion
        self.user_identity = user_identity
        self.run_exclusive = run_exclusive
        self.application_package_references = application_package_references
        self.authentication_token_settings = authentication_token_settings
        self.allow_low_priority_node = allow_low_priority_node
