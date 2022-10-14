#!/usr/bin/env python3
"""DataBase Storage Engine"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import os

classes = {
        "Amenity": Amenity,
        "City": City,
        "State": State,
        "Place": Place,
        "Review": Review,
        "User": User
        }

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        # dialect+driver://username:password@host:port/database
        self.__engine = create_engine("mysql+mysqldb://" +
                                      f"{os.getenv('HBNB_MYSQL_USER')}:" +
                                      f"{os.getenv('HBNB_MYSQL_PWD')}@" +
                                      f"{os.getenv('HBNB_MYSQL_HOST')}/" +
                                      f"{os.getenv('HBNB_MYSQL_DB')}",
                                      pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

        self.__session = Session(self.__engine)

    def all(self, cls=None):
        result = dict()

        for x in classes:
            if (cls is classes[x]) or (cls is x) or (cls is None):
                objs = self.__session.query(classes[x]).all()
                for obj in objs:
                    key = "{}.{}".format(obj.__class__, obj.id)
                    result[key] = obj

        return (result)
