# This file was generated by jschema_to_python version 0.1.0.

class Attachment(object):
    """An artifact relevant to a result."""
    def __init__(self,
        artifactLocation=None,
        description=None,
        properties=None,
        rectangles=[],
        regions=[]):

        missing_properties = []
        if artifactLocation is None:
            missing_properties.append('artifactLocation')
        if len(missing_properties) > 0:
            raise Exception('required properties of class Attachment were not provided: {}'.format(', '.join(missing_properties)))

        self.artifactLocation=artifactLocation
        self.description=description
        self.properties=properties
        self.rectangles=rectangles
        self.regions=regions
