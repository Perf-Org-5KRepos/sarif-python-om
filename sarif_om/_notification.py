# This file was generated by jschema_to_python version 1.1.4.

import attr


@attr.s
class Notification(object):
    """Describes a condition relevant to the tool itself, as opposed to being relevant to a target being analyzed by the tool."""

    message = attr.ib()
    associated_rule = attr.ib(default=None, metadata={"schema_property_name": "associatedRule"})
    descriptor = attr.ib(default=None, metadata={"schema_property_name": "descriptor"})
    exception = attr.ib(default=None, metadata={"schema_property_name": "exception"})
    level = attr.ib(default="warning", metadata={"schema_property_name": "level"})
    locations = attr.ib(default=None, metadata={"schema_property_name": "locations"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
    thread_id = attr.ib(default=None, metadata={"schema_property_name": "threadId"})
    time_utc = attr.ib(default=None, metadata={"schema_property_name": "timeUtc"})
