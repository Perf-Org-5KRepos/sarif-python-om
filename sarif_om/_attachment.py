# This file was generated by jschema_to_python version 1.1.4.

import attr


@attr.s
class Attachment(object):
    """An artifact relevant to a result."""

    artifact_location = attr.ib()
    description = attr.ib(default=None, metadata={"schema_property_name": "description"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
    rectangles = attr.ib(default=None, metadata={"schema_property_name": "rectangles"})
    regions = attr.ib(default=None, metadata={"schema_property_name": "regions"})
