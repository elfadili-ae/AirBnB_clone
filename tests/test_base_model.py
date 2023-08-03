#!/usr/bin/env python3
""" Test cases for base_model
"""
import unittest
import uuid
import time
from models.base_model import BaseModel

class BaseModelTest(unittest.TestCase):
    """BaseModel test cases"""


# --Doc section-----------------------------------
    def test_BaseModule_doc(self):
        """check the module's doc"""
        doc = BaseModel.__doc__
        self.assertTrue(len(doc) > 1)

    def test_BaseModel_str_doc(self):
        """check __str__ doc"""
        doc = BaseModel.__str__.__doc__
        self.assertTrue(len(doc) > 1)

    def test_BaseModel_save_doc(self):
        """check save doc"""
        doc = BaseModel.save.__doc__
        self.assertTrue(len(doc) > 1)

    def test_BaseModel_to_dict_doc(self):
        """check to_dict doc"""
        doc = BaseModel.to_dict.__doc__
        self.assertTrue(len(doc) > 1)

# --Public attribute id-----------------------------
    def test_BaseModel_id_not_null(self):
        """check if id is not null"""
        obj = BaseModel()
        self.assertNotEqual(obj.id, None)

    def test_BaseModel_id_is_string(self):
        """check if id is a string"""
        obj1 = BaseModel()
        self.assertTrue(type(obj1.id), str)

    def test_BaseModel_id_is_uuid(self):
        """check if id is a UUID """
        obj = BaseModel()
        self.assertTrue(uuid.UUID(obj.id))

    def test_BaseModel_ids_not_equal(self):
        """check if id is not null"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
