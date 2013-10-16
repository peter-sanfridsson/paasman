# -*- coding: utf-8 -*-

from paasman.director.db import Base, engine
from paasman.director.models import Node

if __name__ == "__main__":
    Base.metadata.create_all(engine)