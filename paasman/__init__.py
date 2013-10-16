# -*- coding: utf-8 -*-
"""
    authors
    =======
    mikhln-9
    sanpet-8
"""

try:
    # we don't store local_config.py in our git repo to hide our secret keys
    import local_config as config
except:
    import config # we assume we have this?
