#!/usr/bin/python3
from datetime import datetime
from models import storage
import uuid
class BaseModel:
    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = (type(self).__name__)
        my_dict["created_at"] = my_dict["created_at"].isoformat
        my_dict["updated_at"] = my_dict["updated_at"].isoformat
        return my_dict
    def save(self):
        self.updated_at = datetime.now()
        storage.save()#method of storage
    def __init__(self,*args, **kwargs):
        """Initializes a new BaseModel
        Args:
            *args (any): Unused
            **kwargs (dict): Key/value pairs of attributes
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == ["created_at"]:
                    self.__dict__[key] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == ["updated_at"]:
                    self.__dict__[key] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__["key"] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            storage.new(self)#add a call to the method