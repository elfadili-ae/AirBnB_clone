#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as file:
                for key, value in json.load(file).items():
                    attr_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attr_value
        except FileNotFoundError:
            pass
