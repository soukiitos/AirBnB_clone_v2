
#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models



place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True,
                                 nullable=False),
                      Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))



class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity",
                             secondary="place_amenity",
                             viewonly=False)

   # @property
   # def amenities(self):
   #     """ returns the list of Amenity instances based on
   #         the attribute amenity_ids that contains all Amenity.id
   #         linked to the Place.
   #     """
   #     amenities_list = []
   #     for amenity in models.storage.all(Amenity).values():
   #         if amenity.id in self.amenity_ids:
   #             amenities_list.append(amenity)
   #     return amenities_list
    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def amenities(self):
            """Get/set linked Amenities."""
            return [
                amenity
                for amenity in list(models.storage.all(Amenity).values())
                if amenity.id in self.amenity_ids
            ]

    # @amenities.setter
    # def amenities(self, value):
   #     if isinstance(self, value, Amenity):
   #         self.amenity_ids.append(value.id)
        @amenities.setter
        def amenities(self, value):
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)

        @property
        def reviews(self):
            """ returns the list of Review instances with
            place_id equals to the current Place.id"""
            reviews_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
