from enum import Enum


class DocumentType(Enum):
    DNI = 1
    PASSPORT = 2

class PersonType(Enum):
    NATURAL = 1
    LEGAL= 2

class Role(Enum):
    ADMIN = 1
    USER = 2
    DRIVER = 3
    
