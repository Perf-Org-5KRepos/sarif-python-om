# This file was generated by jschema_to_python version 0.1.0.

class ThreadFlow(object):
    """Describes a sequence of code locations that specify a path through a single thread of execution such as an operating system or fiber."""
    def __init__(self,
        id=None,
        immutableState=None,
        initialState=None,
        locations=None,
        message=None,
        properties=None):

        missing_properties = []
        if locations is None:
            missing_properties.append('locations')
        if len(missing_properties) > 0:
            raise Exception('required properties of class ThreadFlow were not provided: {}'.format(', '.join(missing_properties)))

        self.id=id
        self.immutableState=immutableState
        self.initialState=initialState
        self.locations=locations
        self.message=message
        self.properties=properties
