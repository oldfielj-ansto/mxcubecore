"""
    py-ISPyB

    FastAPI Prototype  # noqa: E501

    The version of the OpenAPI document: 0.1alpha
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from mxcubecore.utils import pyispyb_clientfrom mxcubecore.utils.pyispyb_client.model.detector import Detector
from mxcubecore.utils.pyispyb_client.model.pydantic_main_data_collection_group import PydanticMainDataCollectionGroup
globals()['Detector'] = Detector
globals()['PydanticMainDataCollectionGroup'] = PydanticMainDataCollectionGroup
from mxcubecore.utils.pyispyb_client.model.data_collection_response import DataCollectionResponse


class TestDataCollectionResponse(unittest.TestCase):
    """DataCollectionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDataCollectionResponse(self):
        """Test DataCollectionResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DataCollectionResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
