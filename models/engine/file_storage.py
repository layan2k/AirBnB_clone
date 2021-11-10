"""File Storage"""
import json
from models.base_model import BaseModel

class FileStorage:
    """File Storage Class"""
    __objects = {}
    __file_path = 'file json'


    def all(self):
        """ returns the dictionary __objects"""
        return type(self).__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key= "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path"""
    json_objects = {}

    for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
    with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
            for key in json_objects:
                self.__objects[key] = BaseModel(**json_objects[key])
        except:
             pass



