"""
    py-ISPyB

    FastAPI Prototype  # noqa: E501

    The version of the OpenAPI document: 0.1alpha
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from mxcubecore.utils.pyispyb_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from mxcubecore.utils.pyispyb_client.exceptions import ApiAttributeError


def lazy_import():
    from mxcubecore.utils.pyispyb_client.model.crystal_response import CrystalResponse
    from mxcubecore.utils.pyispyb_client.model.sample_composition_response import SampleCompositionResponse
    globals()['CrystalResponse'] = CrystalResponse
    globals()['SampleCompositionResponse'] = SampleCompositionResponse


class SSXSampleResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'bl_sample_id': (int,),  # noqa: E501
            'record_time_stamp': (datetime,),  # noqa: E501
            'crystal': (CrystalResponse,),  # noqa: E501
            'sample_compositions': ([SampleCompositionResponse],),  # noqa: E501
            'diffraction_plan_id': (int,),  # noqa: E501
            'crystal_id': (int,),  # noqa: E501
            'container_id': (int,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'code': (str,),  # noqa: E501
            'location': (str,),  # noqa: E501
            'holder_length': (float,),  # noqa: E501
            'loop_length': (float,),  # noqa: E501
            'loop_type': (str,),  # noqa: E501
            'wire_width': (float,),  # noqa: E501
            'comments': (str,),  # noqa: E501
            'completion_stage': (str,),  # noqa: E501
            'structure_stage': (str,),  # noqa: E501
            'publication_stage': (str,),  # noqa: E501
            'publication_comments': (str,),  # noqa: E501
            'bl_sample_status': (str,),  # noqa: E501
            'is_in_sample_changer': (int,),  # noqa: E501
            'last_known_centering_position': (str,),  # noqa: E501
            'smiles': (str,),  # noqa: E501
            'last_image_url': (str,),  # noqa: E501
            'position_id': (int,),  # noqa: E501
            'bl_sub_sample_id': (int,),  # noqa: E501
            'screen_component_group_id': (int,),  # noqa: E501
            'volume': (float,),  # noqa: E501
            'dimension1': (float,),  # noqa: E501
            'dimension2': (float,),  # noqa: E501
            'dimension3': (float,),  # noqa: E501
            'shape': (str,),  # noqa: E501
            'sub_location': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'bl_sample_id': 'blSampleId',  # noqa: E501
        'record_time_stamp': 'recordTimeStamp',  # noqa: E501
        'crystal': 'Crystal',  # noqa: E501
        'sample_compositions': 'sample_compositions',  # noqa: E501
        'diffraction_plan_id': 'diffractionPlanId',  # noqa: E501
        'crystal_id': 'crystalId',  # noqa: E501
        'container_id': 'containerId',  # noqa: E501
        'name': 'name',  # noqa: E501
        'code': 'code',  # noqa: E501
        'location': 'location',  # noqa: E501
        'holder_length': 'holderLength',  # noqa: E501
        'loop_length': 'loopLength',  # noqa: E501
        'loop_type': 'loopType',  # noqa: E501
        'wire_width': 'wireWidth',  # noqa: E501
        'comments': 'comments',  # noqa: E501
        'completion_stage': 'completionStage',  # noqa: E501
        'structure_stage': 'structureStage',  # noqa: E501
        'publication_stage': 'publicationStage',  # noqa: E501
        'publication_comments': 'publicationComments',  # noqa: E501
        'bl_sample_status': 'blSampleStatus',  # noqa: E501
        'is_in_sample_changer': 'isInSampleChanger',  # noqa: E501
        'last_known_centering_position': 'lastKnownCenteringPosition',  # noqa: E501
        'smiles': 'SMILES',  # noqa: E501
        'last_image_url': 'lastImageURL',  # noqa: E501
        'position_id': 'positionId',  # noqa: E501
        'bl_sub_sample_id': 'blSubSampleId',  # noqa: E501
        'screen_component_group_id': 'screenComponentGroupId',  # noqa: E501
        'volume': 'volume',  # noqa: E501
        'dimension1': 'dimension1',  # noqa: E501
        'dimension2': 'dimension2',  # noqa: E501
        'dimension3': 'dimension3',  # noqa: E501
        'shape': 'shape',  # noqa: E501
        'sub_location': 'subLocation',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, bl_sample_id, record_time_stamp, crystal, sample_compositions, *args, **kwargs):  # noqa: E501
        """SSXSampleResponse - a model defined in OpenAPI

        Args:
            bl_sample_id (int):
            record_time_stamp (datetime):
            crystal (CrystalResponse):
            sample_compositions ([SampleCompositionResponse]):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            diffraction_plan_id (int): [optional]  # noqa: E501
            crystal_id (int): [optional]  # noqa: E501
            container_id (int): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            code (str): [optional]  # noqa: E501
            location (str): [optional]  # noqa: E501
            holder_length (float): [optional]  # noqa: E501
            loop_length (float): [optional]  # noqa: E501
            loop_type (str): [optional]  # noqa: E501
            wire_width (float): [optional]  # noqa: E501
            comments (str): [optional]  # noqa: E501
            completion_stage (str): [optional]  # noqa: E501
            structure_stage (str): [optional]  # noqa: E501
            publication_stage (str): [optional]  # noqa: E501
            publication_comments (str): [optional]  # noqa: E501
            bl_sample_status (str): [optional]  # noqa: E501
            is_in_sample_changer (int): [optional]  # noqa: E501
            last_known_centering_position (str): [optional]  # noqa: E501
            smiles (str): [optional]  # noqa: E501
            last_image_url (str): [optional]  # noqa: E501
            position_id (int): [optional]  # noqa: E501
            bl_sub_sample_id (int): [optional]  # noqa: E501
            screen_component_group_id (int): [optional]  # noqa: E501
            volume (float): [optional]  # noqa: E501
            dimension1 (float): [optional]  # noqa: E501
            dimension2 (float): [optional]  # noqa: E501
            dimension3 (float): [optional]  # noqa: E501
            shape (str): [optional]  # noqa: E501
            sub_location (int): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.bl_sample_id = bl_sample_id
        self.record_time_stamp = record_time_stamp
        self.crystal = crystal
        self.sample_compositions = sample_compositions
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, bl_sample_id, record_time_stamp, crystal, sample_compositions, *args, **kwargs):  # noqa: E501
        """SSXSampleResponse - a model defined in OpenAPI

        Args:
            bl_sample_id (int):
            record_time_stamp (datetime):
            crystal (CrystalResponse):
            sample_compositions ([SampleCompositionResponse]):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            diffraction_plan_id (int): [optional]  # noqa: E501
            crystal_id (int): [optional]  # noqa: E501
            container_id (int): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            code (str): [optional]  # noqa: E501
            location (str): [optional]  # noqa: E501
            holder_length (float): [optional]  # noqa: E501
            loop_length (float): [optional]  # noqa: E501
            loop_type (str): [optional]  # noqa: E501
            wire_width (float): [optional]  # noqa: E501
            comments (str): [optional]  # noqa: E501
            completion_stage (str): [optional]  # noqa: E501
            structure_stage (str): [optional]  # noqa: E501
            publication_stage (str): [optional]  # noqa: E501
            publication_comments (str): [optional]  # noqa: E501
            bl_sample_status (str): [optional]  # noqa: E501
            is_in_sample_changer (int): [optional]  # noqa: E501
            last_known_centering_position (str): [optional]  # noqa: E501
            smiles (str): [optional]  # noqa: E501
            last_image_url (str): [optional]  # noqa: E501
            position_id (int): [optional]  # noqa: E501
            bl_sub_sample_id (int): [optional]  # noqa: E501
            screen_component_group_id (int): [optional]  # noqa: E501
            volume (float): [optional]  # noqa: E501
            dimension1 (float): [optional]  # noqa: E501
            dimension2 (float): [optional]  # noqa: E501
            dimension3 (float): [optional]  # noqa: E501
            shape (str): [optional]  # noqa: E501
            sub_location (int): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.bl_sample_id = bl_sample_id
        self.record_time_stamp = record_time_stamp
        self.crystal = crystal
        self.sample_compositions = sample_compositions
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
