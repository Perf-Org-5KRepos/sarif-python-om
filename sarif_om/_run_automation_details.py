# This file was generated by jschema_to_python version 1.1.0.

import attr

@attr.s
class RunAutomationDetails(object):
    """Information that describes a run's identity and role within an engineering system process."""
    correlation_guid = attr.ib(default=None)
    description = attr.ib(default=None)
    guid = attr.ib(default=None)
    id = attr.ib(default=None)
    properties = attr.ib(default=None)