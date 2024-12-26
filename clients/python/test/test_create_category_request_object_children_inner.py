# coding: utf-8

"""
    Lunch Money API - v2

    This is a version of the Lunch Money API described using the the OpenAPI 3.X specification.    The goal of this project is to validate an \"API Design First\" approach for the Lunch Money API, which should allow us to gather developer feedback prior to implementation in order to develop API endpoints more quickly.  This version of the API will differ from the existing v1 beta version. For more information on the changes please see the  [v2 API Changelog](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/changelog)  Some useful links: - [Current v1 Lunch Money API Documentation](https://lunchmoney.dev) - [v2 API Changelog](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/changelog) - [OpenAPI API YAML Specification](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/openapi/) - [Awesome Lunch Money Projects](https://lunchmoney.dev/#awesome-projects)

    The version of the OpenAPI document: 2.7.4
    Contact: devsupport@lunchmoney.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from lunchable.models.create_category_request_object_children_inner import CreateCategoryRequestObjectChildrenInner

class TestCreateCategoryRequestObjectChildrenInner(unittest.TestCase):
    """CreateCategoryRequestObjectChildrenInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateCategoryRequestObjectChildrenInner:
        """Test CreateCategoryRequestObjectChildrenInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCategoryRequestObjectChildrenInner`
        """
        model = CreateCategoryRequestObjectChildrenInner()
        if include_optional:
            return CreateCategoryRequestObjectChildrenInner(
                id = 56,
                name = '0',
                description = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                group_id = 56,
                is_group = True,
                archived = True,
                archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                order = 1.337
            )
        else:
            return CreateCategoryRequestObjectChildrenInner(
                id = 56,
                name = '0',
                description = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                group_id = 56,
                is_group = True,
                archived = True,
                archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                order = 1.337,
        )
        """

    def testCreateCategoryRequestObjectChildrenInner(self):
        """Test CreateCategoryRequestObjectChildrenInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
