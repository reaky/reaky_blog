#!/usr/bin/env python
import os, sys, urllib2, re
import sqlite3
import markdown2
from datetime import datetime
from bottle import route, post, view, template, response, request, run, redirect, error, static_file

post_per_page=5;

def db_execute(sql_command, sql_parameter=''):
	conn = sqlite3.connect('./blog.db')
	conn.text_factory = str
	c = conn.cursor()
	try:
		c.execute(sql_command, sql_parameter)
	except sqlite3.OperationalError, msg:
		print msg
		return
	conn.commit()
	result = c.fetchall()
	conn.commit()
	c.close()
	return result
def init_blog():
	if os.path.isfile('./blog.db'):
		print 'file exist!'
		return
	db_execute('''CREATE TABLE posts(
		id INTEGER PRIMARY KEY,
		title TEXT NOT NULL,
		tags TEXT,
		date DATE NOT NULL,
		content TEXT NOT NULL)''')
	db_execute('''CREATE TABLE comments(
		id INTEGER PRIMARY KEY,
		post_id INTEGER NOT NULL,
		username TEXT NOT NULL,
		email TEXT,
		comment TEXT NOT NULL,
		date DATE NOT NULL)''')
	db_execute('''INSERT INTO posts (title, date, content) VALUES
			('title1', datetime('now'), 'Hello World!')''')
def check_user():
	if True:
		return
	else:
		redirect('/norights')

@route('/')
@route('/show/<num:int>')
def bloglist(num=0):
#	if post_id == 0:
#		posts = db_execute("SELECT * FROM (SELECT * FROM posts WHERE id > ? ORDER BY date DESC) LIMIT 5", (post_id,))
#	else:
	posts = db_execute("SELECT * FROM (SELECT * FROM posts ORDER BY date DESC) LIMIT '%d', '%d'"%(num, post_per_page))
#	return dict(posts=posts)
	user_agent = request.get_header('User-Agent')
	reStr = 'iPhone|iPod|iPad|Android|Windows Mobile|SymbianOS|NOKIA|SAMSUNG'
	if (re.search(reStr, user_agent)):
		return template('blog_mobile', posts=posts, template_settings={'noescape':True})
	else:
		return template('blog', posts=posts, template_settings={'noescape':True})

@route('/sally')
@route('/sally/show/<post_id:int>')
@view('blog', template_settings={'noescape':True})
def bloglist(num=0):
	user_agent = request.get_header('User-Agent')
	reStr = 'iPhone|iPod|iPad|Android|Windows Mobile|SymbianOS|NOKIA|SAMSUNG'
	if (re.search(reStr, user_agent)):
		print "mobile user"
	else:
		posts = db_execute("SELECT * FROM (SELECT * FROM posts ORDER BY date DESC) LIMIT '%d', '%d'"%(num, post_per_page))
		return dict(posts=posts)
#	if post_id == 0:
#		posts = db_execute("SELECT * FROM (SELECT * FROM posts WHERE id > ? ORDER BY date DESC) LIMIT 5", (post_id,))
#	else:

@route('/rss.xml')
@view('rss')
def blogrss():
	posts = db_execute("SELECT * FROM (SELECT * FROM posts ORDER BY date DESC) LIMIT 50")
	response.content_type = 'xml/rss'
	return dict(posts=posts)

@route('/listcomment/<post_id:int>')
@view('comments')
def listcomment(post_id=1):
	comments = db_execute('SELECT * FROM comments WHERE post_id=? ORDER BY date DESC', (post_id,))
	return dict(comments=comments)

@post('/addcomment/<post_id:int>')
def addcomment(post_id=1):
		username = request.forms.get('username')
		email = request.forms.get('email')
		comment = request.forms.get('comment')
		comments = db_execute("INSERT INTO comments (post_id, username, email, comment, date) VALUES ('%d', '%s', '%s', '%s', datetime('now'))"%(post_id, username, email, comment))
		return "add ok"

@route('/admin')
@view('admin')
def admin():
	check_user()
	posts = db_execute('SELECT * FROM posts ORDER BY date DESC')
	return dict(posts=posts)

@route('/addpost')
@route('/editpost/<post_id:int>')
@view('editor')
def editpost(post_id=0):
	check_user()
	if post_id == 0:
		return dict(post=('','','','',''))
	posts = db_execute('SELECT * FROM posts WHERE id = ?', (post_id,))
	#posts[0][3] = datetime.strptime(posts[0][3],"%Y-%m-%d %H:%M:%S")
	return dict(post=posts[0])
			
@post('/updatepost/')
@post('/updatepost/<post_id:int>')
def updatepost(post_id=0):
	check_user()
	title = request.forms.get('title')
	content = markdown2.markdown(request.forms.get('postcontent'))
	date = request.forms.get('date')
	if date == '':
		date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	#else:
		#prevent wrong input
		#date= datetime.strptime(date,"%Y-%m-%d")
	if post_id == 0:
		posts = db_execute("INSERT INTO posts (title, content, date) VALUES ('%s', '%s', datetime('%s'))"%(title, content, date))
	else:
		posts = db_execute("UPDATE posts SET title='%s', content='%s', date=datetime('%s') WHERE id='%d'"%(title, content, date, post_id))
	redirect('/admin')
	return "update ok"

@route('/deletepost/<post_id:int>')
def deletepost(post_id=0):
	check_user()
	posts = db_execute('DELETE FROM posts WHERE id = ?', (post_id,))
	redirect('/admin')
	return "del ok"
		
@route('/norights')
def nnorights(self):
	return 'Only admin can do so.  <p><a href="javascript:history.back()">Go Back</a>'

@route('/guestbook')
@view('blog')
def guestbook():
	posts = db_execute('SELECT * FROM posts WHERE id=1')
	return dict(posts=posts)

@route('/about')
@view('about')
def about():
	return dict()
	return static_file('about.tpl', root='./views/')

def getqq():
	req = urllib2.Request('http://v.t.qq.com/cgi-bin/weiboshow?f=s&tweetflag=1&fansflag=0&fansnum=30&name=reaky_yf&sign=c68092733fb05b975c2d13df9a9c936b85bfc53c&jsonp=?')
	req.add_header('Referer', 'http://v.t.qq.com/')
	r = urllib2.urlopen(req)
	content = r.read()
	import re
	response.out.write('var qq='+content[2:-1]+';')

@route('/static/<filename:path:re:.*\.(css|js|ico|png|txt|html)>')
def server_static(filename):
	return static_file(filename, root='./static/')

@error(404)
def error404(error):
	return 'Nothing here, sorry'

if __name__ == '__main__':
	init_blog()
	#port = int(os.environ.get('PORT', 8080))
	run(host='0.0.0.0', port=int(sys.argv[1] if len(sys.argv) > 1 else 8080))
