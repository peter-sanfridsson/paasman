# -*- coding: utf-8 -*-
"""
    authors
    =======
    mikhln-9
    sanpet-8
"""

import os
import sys
import datetime
from werkzeug import secure_filename

class DirectorManager(object):
	"""DirectorManager is responsible for handle the deployment of
	applications and manage the deployed instances.
	"""

	def __init__(self, storage_path):
		self.storage_path = storage_path

	def store_application(self, name, blob):
		return self.storage_path

	def _get_deploy_dir(self, name, blob):
		release_name = datetime.datetime.utcnow().strftime("%Y%m%d%H%M")
		return os.path.join(self.storage_path, name, release_name)

	@property
	def filename(self):
		return self.storage_path
