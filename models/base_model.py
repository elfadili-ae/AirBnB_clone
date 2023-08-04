#!/usr/bin/env python3
""" BaseModel's Module
"""
import json
import uuid
from datetime import datetime

class BaseModel:
    """BaseModel's class"""

    def __init__(self):
        """Initialize the model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """update update_at datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """keys/values of __doc__ in the instance

        Returns:
            dictionary format
        """
        pass

    def __str__(self):
        """print model's representation:
        [<class name>] (<self.id>) <self.__dict__>
        """
        pass
