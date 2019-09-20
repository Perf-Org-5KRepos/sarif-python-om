# This file was generated by jschema_to_python version 0.1.0.

class ReportingDescriptorRelationship(object):
    """Information about the relation of one reporting descriptor to another."""
    def __init__(self,
        description=None,
        kinds=['relevant'],
        properties=None,
        target=None):

        missing_properties = []
        if target is None:
            missing_properties.append('target')
        if len(missing_properties) > 0:
            raise Exception('required properties of class ReportingDescriptorRelationship were not provided: {}'.format(', '.join(missing_properties)))

        self.description=description
        self.kinds=kinds
        self.properties=properties
        self.target=target
