# This file was generated by jschema_to_python version 1.1.0.

import attr

@attr.s
class ArtifactChange(object):
    """A change to a single artifact."""
    artifact_location = attr.ib()
    replacements = attr.ib()
    properties = attr.ib(default=None)