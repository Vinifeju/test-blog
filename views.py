from flask import render_template
from models import Post
from app import app

@app.route('/')
def index():
	return render_template('index.html'), 200

@app.route('/post-list')
def posts():
	post_list = Post.query.all()
	return render_template('posts.html', posts=post_list), 200

# === Post ===
@app.route('/post-list/<postQ>')
def post_page(postQ):
	post = Post.query.filter(Post.url == postQ).first()
	print(post)
	return render_template('post.html', post=post), 200