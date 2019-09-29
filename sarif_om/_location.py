# This file was generated by jschema_to_python version 1.1.0.

import attr

@attr.s
class Location(object):
    """A location within a programming artifact."""
    annotations = attr.ib(default=None)
    id = attr.ib(default=-1)
    logical_locations = attr.ib(default=None)
    message = attr.ib(default=None)
    physical_location = attr.ib(default=None)
    properties = attr.ib(default=None)
    relationships = attr.ib(default=None)