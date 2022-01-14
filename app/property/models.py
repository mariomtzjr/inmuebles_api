from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy_serializer import SerializerMixin

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Property(Base, SerializerMixin):
    """Property Model

    fields:
        - id: Unique identifier
        - address: Property address
        - state: Property location
        - city: Property location into state
        - price: Property price
        - description: Property description
        - year: When property was builded
    """

    __tablename__ = 'property'

    id = Column(Integer, primary_key=True)
    address = Column(String(255))
    # state = Column(String(50))  # Does not exist this field into database
    city = Column(String(36))
    price = Column(Integer)
    description = Column(String(500))
    year = Column(Integer)
    # status_history = relationship("StatusHistory", back_populates="property")
    status_history = relationship("StatusHistory", backref="property")

    def __repr__(self):
        return f'<Property id={self.id}>'

    
class Status(Base, SerializerMixin):
    """Status Model

    fields:
        - id: Unique identifier
        - name: Status name
        - label: Status name description
    """

    __tablename__ = 'status'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    label = Column(String(255))
    # status_history = relationship("StatusHistory", back_populates="status")
    status_history = relationship("StatusHistory", backref="Status")

    def __repr__(self):
        return f'{self.name}'


class StatusHistory(Base, SerializerMixin):
    """StatusHistory Model

    fields:
        - id: Unique identifier
        - property_id: Property unique identifier (ForeignKey relationship)
        - status_id: Status unique identifier (ForeignKey relationship)
        - update_date: Date when the last property status was updated
    """

    __tablename__ = 'status_history'

    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('property.id'))
    status_id = Column(Integer, ForeignKey('status.id'))
    update_date = Column(DateTime)

    def __repr__(self):
        return f'{self.property_id}'