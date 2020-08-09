from app import db
from helpers import PostHelper
from datetime import datetime

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(140))
	url = db.Column(db.String(140), unique=True)
	body = db.Column(db.Text)
	created = db.Column(db.DateTime, default = datetime.now())

	def __init__(self, *args, **kwargs):
		super(Post, self).__init__(*args, **kwargs)
		self.url = PostHelper.create_slug(self.title)

	def __repr__(self):
		return f'<Post title: {self.title}>'
		