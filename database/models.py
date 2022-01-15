from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy_serializer import SerializerMixin

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Property(Base, SerializerMixin):

    __tablename__ = 'property'

    #: Unique identifier of Property
    id = Column(Integer, primary_key=True)
    #: Address where property is located
    address = Column(String(255))
    # state = Column(String(50))  # Does not exist this field into database
    #: Property location into state
    city = Column(String(36))
    #: Property price
    price = Column(Integer)
    #: Property description
    description = Column(String(500))
    #: When property was builded
    year = Column(Integer)
    # status_history = relationship("StatusHistory", back_populates="property")
    #: Reference to parent model (StatusHistory)
    status_history = relationship("StatusHistory", backref="property")

    def __repr__(self):
        return f'<Property id={self.id}>'

    
class Status(Base, SerializerMixin):

    __tablename__ = 'status'

    #: Unique identifier of Status
    id = Column(Integer, primary_key=True)
    #: Status name
    name = Column(String(30))
    #: Status name description
    label = Column(String(255))
    #: Reference to parent model (StatusHistory)
    status_history = relationship("StatusHistory", backref="Status")

    def __repr__(self):
        return f'{self.name}'


class StatusHistory(Base, SerializerMixin):

    __tablename__ = 'status_history'

    #: Unique identifier (int)
    id = Column(Integer, primary_key=True)
    #: Property unique identifier (ForeignKey relationship with Property model)
    property_id = Column(Integer, ForeignKey('property.id'))
    #: Status unique identifier (ForeignKey relationship with Status model)
    status_id = Column(Integer, ForeignKey('status.id'))
    #: Date when the last property status was updated
    update_date = Column(DateTime)

    def __repr__(self):
        return f'{self.property_id}'