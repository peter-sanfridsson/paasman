# -*- coding: utf-8 -*-
"""
    authors
    =======
    mikhln-9
    sanpet-8
"""

# TODO: models

import sqlalchemy as sa
from paasman.director.db import Base

class Application(Base):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, index=True)
    status = sa.Column(sa.Enum("deployed", "undeployed", name="deployed_status"), nullable=False)
    # TODO: add auto-scaling, #processes, #instances etc
