#!/usr/bin/env python3
""" Test cases for base_model
"""
import unittest
import inspect
import ast
import uuid
import time
from datetime import datetime
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
        """check if id is null"""
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

# --Public attribute created_at-----------------------------
    def test_BaseModel_createdAt_not_null(self):
        """check if created_at is null"""
        obj1 = BaseModel()
        self.assertNotEqual(obj1.created_at, None)

    def test_BaseModel_createdAt_is_datetime(self):
        """check if created_at is datetime"""
        obj1 = BaseModel()
        self.assertTrue(type(obj1.created_at), datetime)

    def test_BaseModel_createdAt_is_diffrent(self):
        """check that created_at keeps increasing"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertTrue(obj1.created_at < obj2.created_at)

# --Public attribute updated_at-----------------------------
    def test_BaseModel_updatedAt_not_null(self):
        """check if updated_at is null"""
        obj1 = BaseModel()
        self.assertNotEqual(obj1.updated_at, None)

    def test_BaseModel_updatedAt_is_datetime(self):
        """check if updatedd_at is datetime"""
        obj1 = BaseModel()
        self.assertTrue(type(obj1.updated_at), datetime)

    def test_BaseModel_updatedAt_is_createdAt(self):
        """check that updated_at equals to created_at when first created"""
        obj1 = BaseModel()
        self.assertEqual(obj1.created_at, obj1.updated_at)

# --Object initialization ------------------------------
    def test_BaseModel_init_with_args_no_kwargs(self):
        """check that __dict__ remains unchanged with args provided"""
        obj1 = BaseModel("arg1", "arg2")
        dictLen = len(obj1.__dict__)
        self.assertEqual(dictLen, 3)

    def test_BaseModel_init_unused_args(self):
        """check that args are not used"""
        obj1 = BaseModel("val")
        self.assertNotIn("val", obj1.__dict__.values())

    def test_BaseModel_init_with_args_one_Kwargs(self):
        """check that kwarg has been added"""
        obj1 = BaseModel("arg1", "arg2", name="john")
        dictLen = len(obj1.__dict__)
        self.assertEqual(dictLen, 4)
        self.assertEqual(obj1.__dict__["name"], "john")

    def test_BaseModel_init_with_args_multiple_Kwargs(self):
        """check that kwargs have been added"""
        obj1 = BaseModel("arg1", "arg2", name="john", lastname="doe")
        dictLen = len(obj1.__dict__)
        self.assertEqual(dictLen, 5)
        self.assertEqual(obj1.__dict__["name"], "john")
        self.assertEqual(obj1.__dict__["lastname"], "doe")

    def test_BaseModel_init_with_class_Kwarg(self):
        """check that __class__ is not added"""
        obj1 = BaseModel(__class__=str)
        dictLen = len(obj1.__dict__)
        self.assertEqual(dictLen, 3)

    def test_BaseModel_init_with_Kwarg(self):
        """check that __class__ is not added"""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        _id = "2023"
        obj1 = BaseModel(id=_id, created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(obj1.created_at, dt)
        self.assertEqual(obj1.updated_at, dt)
        self.assertEqual(obj1.id, "2023")

    def test_BaseModel_init_Kwargs_noneVal(self):
        """check init kwargs values equal to None"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

# -- method save() -----------------------------
class BaseModelSaveTest(unittest.TestCase):
    """test cases for BaseModel.save method"""
    def test_BaseModel_save_updatedAt_is_date(self):
        """check if save() saves a datetime"""
        obj1 = BaseModel()
        self.assertEqual(type(obj1.updated_at), datetime)

    def test_BaseModel_save_updatedAt_changed(self):
        """check if save() changes the updated_at"""
        obj1 = BaseModel()
        oldDate = obj1.updated_at
        obj1.save()
        newDate = obj1.updated_at
        self.assertNotEqual(oldDate, newDate)

    def test_BaseModel_save_updatedAt_is_newer(self):
        """check new saved update_at is greater than the old"""
        obj1 = BaseModel()
        oldDate = obj1.updated_at
        obj1.save()
        newDate = obj1.updated_at
        self.assertTrue(oldDate < newDate)

# --method to_dict() -----------------------------
