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

from sqlalchemy import create_engine, select, text, MetaData
from sqlalchemy.orm import Session, scoped_session, sessionmaker
import os

classes = {
        # "amenities": Amenity,
        "cities": City,
        "states": State,
        # "places": Place,
        # "reviews": Review,
        "users": User
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
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    result[key] = obj

        return (result)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()
