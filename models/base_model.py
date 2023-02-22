#!/usr/bin/python3
"""Define a class BaseModel to support other classes.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Represent support to other classes.
    """

    def init(self, id="", created_at=None, updated_at=None):
        """Constructor new instances of class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def str(self):
        """String representation of the instances.
        """
        str = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        return(str)

    def save(self):
        """Updates the public instance attributes.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values.
        """
        n_dict = self.dict.copy()
        if "created_at" in n_dict:
            n_dict["created_at"] = n_dict["created_at"].isoformat()
        if "updated_at" in n_dict:
            n_dict["updated_at"] = n_dict["updated_at"].isoformat()
        n_dict["class"] = self.__class__.__name__
        return n_dict

