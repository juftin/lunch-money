# coding: utf-8

"""
    Lunch Money API - v2

    This is a version of the Lunch Money API described using the the OpenAPI 3.X specification.    The goal of this project is to validate an \"API Design First\" approach for the Lunch Money API, which should allow us to gather developer feedback prior to implementation in order to develop API endpoints more quickly.  This version of the API will differ from the existing v1 beta version. For more information on the changes please see the  [v2 API Changelog](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/changelog)  Some useful links: - [Current v1 Lunch Money API Documentation](https://lunchmoney.dev) - [v2 API Changelog](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/changelog) - [OpenAPI API YAML Specification](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/openapi/) - [Awesome Lunch Money Projects](https://lunchmoney.dev/#awesome-projects)

    The version of the OpenAPI document: 2.7.4
    Contact: devsupport@lunchmoney.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from lunchable.models.transaction_object import TransactionObject
from typing import Optional, Set
from typing_extensions import Self

class CreateNewTransactions201Response(BaseModel):
    """
    CreateNewTransactions201Response
    """ # noqa: E501
    transactions: List[TransactionObject]
    skipped_existing_external_ids: Optional[List[SkippedExistingExternalIdObject]] = None
    __properties: ClassVar[List[str]] = ["transactions", "skipped_existing_external_ids"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateNewTransactions201Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item_transactions in self.transactions:
                if _item_transactions:
                    _items.append(_item_transactions.to_dict())
            _dict['transactions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in skipped_existing_external_ids (list)
        _items = []
        if self.skipped_existing_external_ids:
            for _item_skipped_existing_external_ids in self.skipped_existing_external_ids:
                if _item_skipped_existing_external_ids:
                    _items.append(_item_skipped_existing_external_ids.to_dict())
            _dict['skipped_existing_external_ids'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateNewTransactions201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transactions": [TransactionObject.from_dict(_item) for _item in obj["transactions"]] if obj.get("transactions") is not None else None,
            "skipped_existing_external_ids": [SkippedExistingExternalIdObject.from_dict(_item) for _item in obj["skipped_existing_external_ids"]] if obj.get("skipped_existing_external_ids") is not None else None
        })
        return _obj


