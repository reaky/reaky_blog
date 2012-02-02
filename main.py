#!/usr/bin/env python
import os, urllib2, datetime
from bottle import route, view, response, run
import bottle
import markdown
import sqlite3

def db_execute(sql_command):
	conn = sqlite3.connect('./blog.db')
	c = conn.cursor()
	c.execute(sql_command)
	conn.commit()
	result = c.fetchall()
	conn.commit()
	c.close()
	return result
def init_blog():
	db_execute('''create table posts(
		id integer primary key,
		title text not null,
		tags text,
		date not null,
		content text not null)''')
	db_execute('''create table comments(
		id integer primary key,
		post_id not null,
		username text not null,
		email text,
		comment text, date)''')
	db_execute('''insert into posts values
			(null, 'title1', '', '2012-2-1', 'Hello World!')''')
def check_user():
	if not users.is_current_user_admin():
		redirect('/norights')

@route('/:filename#.+\.(css|js|ico|png|txt|html)#')
def static(filename):
	return bottle.static_file(filename, root='./static/')

@route('/')
@view('blog')
def bloglist():
	posts = db_execute('select * from posts order by date DESC')
	return dict(posts=posts)

@route('/rss.xml')
@view('rss')
def blogrss():
	posts = db_execute('select * from posts order by date DESC')
	response.content_type = 'xml/rss'
	return dict(posts=posts)

@route('list_comment')
def list_comment(post_id='1'):
	comments = db_execute('select * from comments where post_id=:1 order by date DESC', post_id)
	return dict(comments=comments)

@route('/add_comment')
def add_comment(self):
	return

@route('/admin')
@view('admin')
def admin():
	check_user()
	posts = db_execute('select * from posts order by date DESC')
	return dict(posts=posts)

@route('/addpost')
def addpost():
	check_user()
	post.title= request.get('title')
	post.content = request.get('postcontent')
	if request.get('date')!="":
		post.date= datetime.datetime.strptime(request.get('date'),"%Y-%m-%d")
	posts = db_execute('inser into posts values ()')
	redirect('/admin')

@route('/deletepost/postid')
def deletepost(post_id):
	check_user()
	id = request.get('id')
	if id = None:
		return
	posts = db_execute('select * from posts order by date DESC')
	redirect('/admin')
		
@route('/editpost')
@view('editor')
def editpost(post_id):
	check_user()
	id = request.get('id')
	if id = None:
		return
	posts = db_execute('select * from posts order by date DESC')
	redirect('/admin')
			
@route('/norights')
def nnorights(self):
	return 'Only admin can do so.  <p><a href="javascript:history.back()">Go Back</a>'

@route('/guestbook')
@view('blog')
def guestbook():
	posts = db_execute('select * from posts where id=1 order by date DESC')
	return dict(posts=posts)

@route('/about')
def about():
	return bottle.static_file('templates/about.html')

def getqq():
	req = urllib2.Request('http://v.t.qq.com/cgi-bin/weiboshow?f=s&tweetflag=1&fansflag=0&fansnum=30&name=reaky_yf&sign=c68092733fb05b975c2d13df9a9c936b85bfc53c&jsonp=?')
	req.add_header('Referer', 'http://v.t.qq.com/')
	r = urllib2.urlopen(req)
	content = r.read()
	import re
	response.out.write('var qq='+content[2:-1]+';')

@route('/buzz')
def buzz():
	return bottle.static_file('templates/buzz.html')

run(host='0.0.0.0', port=8080)
