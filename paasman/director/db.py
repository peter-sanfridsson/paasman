# -*- coding: utf-8 -*-
"""
    authors
    =======
    mikhln-9
    sanpet-8
"""

# TODO: or use redis for all persistence instead?

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql+psycopg2://root:paasman123@10.10.10.2:5432/airsoftdb_dev_v2",
    convert_unicode=True,
    pool_size=8, # change to what?
    max_overflow=0
)

metadata = MetaData()
session = scoped_session(sessionmaker(autocommit=False,
    autoflush=False,
    bind=engine)
)

Base = declarative_base(metadata=metadata)
Base.query = session.query_property()
