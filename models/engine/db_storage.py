#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel, Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                getenv("HBNB_MYSQL_USER"),
                                getenv("HBNB_MYSQL_PWD"),
                                getenv("HBNB_MYSQL_HOST"),
                                getenv("HBNB_MYSQL_DB")),
                                pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        object_list = []
        my_dict = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            classes_to_query = [cls]
        else:
            classes_to_query = [User, State, City, Amenity, Place, Review]
        for class_to_query in classes_to_query:
            object_list.extend(self.__session.query(class_to_query).all())

        for val in object_list:
            key = f"{val.__class__.__name__}.{val.id}"
            my_dict[key] = val
        return my_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload method"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine,
                expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        '''close session'''
        self.__session.close()
