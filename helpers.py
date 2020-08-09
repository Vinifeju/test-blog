# == Helpers ==

import re

class PostHelper:
	def create_slug(str):
		str_arr = str.split(' ')
		slug = re.sub(r'[(.|,|!|?|;|@|#|$|%)]', '', '-'.join(list(filter(None, str_arr))).lower())

		return slug