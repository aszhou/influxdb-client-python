# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint

import six


class Task(object):
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
        'type': 'str',
        'org_id': 'str',
        'org': 'str',
        'name': 'str',
        'description': 'str',
        'status': 'TaskStatusType',
        'labels': 'list[Label]',
        'authorization_id': 'str',
        'flux': 'str',
        'every': 'str',
        'cron': 'str',
        'offset': 'str',
        'latest_completed': 'datetime',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'links': 'TaskLinks'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'org_id': 'orgID',
        'org': 'org',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'labels': 'labels',
        'authorization_id': 'authorizationID',
        'flux': 'flux',
        'every': 'every',
        'cron': 'cron',
        'offset': 'offset',
        'latest_completed': 'latestCompleted',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'links': 'links'
    }

    def __init__(self, id=None, type=None, org_id=None, org=None, name=None, description=None, status=None, labels=None, authorization_id=None, flux=None, every=None, cron=None, offset=None, latest_completed=None, created_at=None, updated_at=None, links=None):  # noqa: E501
        """Task - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._type = None
        self._org_id = None
        self._org = None
        self._name = None
        self._description = None
        self._status = None
        self._labels = None
        self._authorization_id = None
        self._flux = None
        self._every = None
        self._cron = None
        self._offset = None
        self._latest_completed = None
        self._created_at = None
        self._updated_at = None
        self._links = None
        self.discriminator = None

        self.id = id
        if type is not None:
            self.type = type
        self.org_id = org_id
        if org is not None:
            self.org = org
        self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if labels is not None:
            self.labels = labels
        if authorization_id is not None:
            self.authorization_id = authorization_id
        self.flux = flux
        if every is not None:
            self.every = every
        if cron is not None:
            self.cron = cron
        if offset is not None:
            self.offset = offset
        if latest_completed is not None:
            self.latest_completed = latest_completed
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this Task.  # noqa: E501


        :return: The id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Task.


        :param id: The id of this Task.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this Task.  # noqa: E501

        The type of task, this can be used for filtering tasks on list actions.  # noqa: E501

        :return: The type of this Task.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Task.

        The type of task, this can be used for filtering tasks on list actions.  # noqa: E501

        :param type: The type of this Task.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def org_id(self):
        """Gets the org_id of this Task.  # noqa: E501

        The ID of the organization that owns this Task.  # noqa: E501

        :return: The org_id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Task.

        The ID of the organization that owns this Task.  # noqa: E501

        :param org_id: The org_id of this Task.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def org(self):
        """Gets the org of this Task.  # noqa: E501

        The name of the organization that owns this Task.  # noqa: E501

        :return: The org of this Task.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this Task.

        The name of the organization that owns this Task.  # noqa: E501

        :param org: The org of this Task.  # noqa: E501
        :type: str
        """

        self._org = org

    @property
    def name(self):
        """Gets the name of this Task.  # noqa: E501

        The name of the task.  # noqa: E501

        :return: The name of this Task.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Task.

        The name of the task.  # noqa: E501

        :param name: The name of this Task.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Task.  # noqa: E501

        An optional description of the task.  # noqa: E501

        :return: The description of this Task.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Task.

        An optional description of the task.  # noqa: E501

        :param description: The description of this Task.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this Task.  # noqa: E501


        :return: The status of this Task.  # noqa: E501
        :rtype: TaskStatusType
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Task.


        :param status: The status of this Task.  # noqa: E501
        :type: TaskStatusType
        """

        self._status = status

    @property
    def labels(self):
        """Gets the labels of this Task.  # noqa: E501


        :return: The labels of this Task.  # noqa: E501
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Task.


        :param labels: The labels of this Task.  # noqa: E501
        :type: list[Label]
        """

        self._labels = labels

    @property
    def authorization_id(self):
        """Gets the authorization_id of this Task.  # noqa: E501

        The ID of the authorization used when this task communicates with the query engine.  # noqa: E501

        :return: The authorization_id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._authorization_id

    @authorization_id.setter
    def authorization_id(self, authorization_id):
        """Sets the authorization_id of this Task.

        The ID of the authorization used when this task communicates with the query engine.  # noqa: E501

        :param authorization_id: The authorization_id of this Task.  # noqa: E501
        :type: str
        """

        self._authorization_id = authorization_id

    @property
    def flux(self):
        """Gets the flux of this Task.  # noqa: E501

        The Flux script to run for this task.  # noqa: E501

        :return: The flux of this Task.  # noqa: E501
        :rtype: str
        """
        return self._flux

    @flux.setter
    def flux(self, flux):
        """Sets the flux of this Task.

        The Flux script to run for this task.  # noqa: E501

        :param flux: The flux of this Task.  # noqa: E501
        :type: str
        """
        if flux is None:
            raise ValueError("Invalid value for `flux`, must not be `None`")  # noqa: E501

        self._flux = flux

    @property
    def every(self):
        """Gets the every of this Task.  # noqa: E501

        A simple task repetition schedule; parsed from Flux.  # noqa: E501

        :return: The every of this Task.  # noqa: E501
        :rtype: str
        """
        return self._every

    @every.setter
    def every(self, every):
        """Sets the every of this Task.

        A simple task repetition schedule; parsed from Flux.  # noqa: E501

        :param every: The every of this Task.  # noqa: E501
        :type: str
        """

        self._every = every

    @property
    def cron(self):
        """Gets the cron of this Task.  # noqa: E501

        A task repetition schedule in the form '* * * * * *'; parsed from Flux.  # noqa: E501

        :return: The cron of this Task.  # noqa: E501
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Sets the cron of this Task.

        A task repetition schedule in the form '* * * * * *'; parsed from Flux.  # noqa: E501

        :param cron: The cron of this Task.  # noqa: E501
        :type: str
        """

        self._cron = cron

    @property
    def offset(self):
        """Gets the offset of this Task.  # noqa: E501

        Duration to delay after the schedule, before executing the task; parsed from flux, if set to zero it will remove this option and use 0 as the default.  # noqa: E501

        :return: The offset of this Task.  # noqa: E501
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this Task.

        Duration to delay after the schedule, before executing the task; parsed from flux, if set to zero it will remove this option and use 0 as the default.  # noqa: E501

        :param offset: The offset of this Task.  # noqa: E501
        :type: str
        """

        self._offset = offset

    @property
    def latest_completed(self):
        """Gets the latest_completed of this Task.  # noqa: E501

        Timestamp of latest scheduled, completed run, RFC3339.  # noqa: E501

        :return: The latest_completed of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._latest_completed

    @latest_completed.setter
    def latest_completed(self, latest_completed):
        """Sets the latest_completed of this Task.

        Timestamp of latest scheduled, completed run, RFC3339.  # noqa: E501

        :param latest_completed: The latest_completed of this Task.  # noqa: E501
        :type: datetime
        """

        self._latest_completed = latest_completed

    @property
    def created_at(self):
        """Gets the created_at of this Task.  # noqa: E501


        :return: The created_at of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Task.


        :param created_at: The created_at of this Task.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Task.  # noqa: E501


        :return: The updated_at of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Task.


        :param updated_at: The updated_at of this Task.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def links(self):
        """Gets the links of this Task.  # noqa: E501


        :return: The links of this Task.  # noqa: E501
        :rtype: TaskLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Task.


        :param links: The links of this Task.  # noqa: E501
        :type: TaskLinks
        """

        self._links = links

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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
