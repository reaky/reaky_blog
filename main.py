#!/usr/bin/env python
import wsgiref.handlers

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
import os, urllib2, datetime
from google.appengine.ext.webapp import template

class Article(db.Model):
	title = db.StringProperty()
	tags = db.StringListProperty(default=None)
	content = db.TextProperty()
	date = db.DateTimeProperty(auto_now_add=True)

class Comment(db.Model):
	article_key = db.StringProperty()
	auth = db.StringProperty()
	email = db.StringProperty()
	content = db.TextProperty()
	date = db.DateTimeProperty(auto_now_add=True)

def check_user(self):
	if not users.is_current_user_admin():
		self.redirect('/norights')

class About(webapp.RequestHandler):
	def get(self, sth=None):
		template_values = {}
		path = os.path.join(os.path.dirname(__file__), 'templates/about.html')
		self.response.out.write(template.render(path, template_values))

class Getqq(webapp.RequestHandler):
	def get(self, sth=None):
		req = urllib2.Request('http://v.t.qq.com/cgi-bin/weiboshow?f=s&tweetflag=1&fansflag=0&fansnum=30&name=reaky_yf&sign=c68092733fb05b975c2d13df9a9c936b85bfc53c&jsonp=?')
		req.add_header('Referer', 'http://v.t.qq.com/')
		r = urllib2.urlopen(req)
		content = r.read()
		import re
		self.response.out.write('var qq='+content[2:-1]+';')

class Buzz(webapp.RequestHandler):
	def get(self, sth=None):
		template_values = {}
		path = os.path.join(os.path.dirname(__file__), 'templates/buzz.html')
		self.response.out.write(template.render(path, template_values))

class Export(webapp.RequestHandler):
	def get(self):
		articles = db.GqlQuery("SELECT * FROM Article ORDER BY date DESC")
		template_values = {
			'articles': articles.fetch(1000,0),
		}
		path = os.path.join(os.path.dirname(__file__), 'templates/export.html')
		self.response.out.write(template.render(path, template_values))
class Blog(webapp.RequestHandler):
	def get(self):
		topage=1
		size=5
		if self.request.get('p') != '':
			topage = int(self.request.get('p'))

		articles = db.GqlQuery("SELECT * FROM Article ORDER BY date DESC")
		num = articles.count()
		more = (1,0)[num%size==0]
		numlist = range(1,num/size+more+1)

		comments = None

		template_values = {
			'articles': articles.fetch(size,(topage-1)*size),
			'comments': comments,
			'topage': topage,
			'numlist': numlist,
			'num': num/size+more,
		}

		path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
		self.response.out.write(template.render(path, template_values))

class List_Comment(webapp.RequestHandler):
	def get(self):
		id = self.request.get('id')
		comments=None
		if id:
			try:
				comments = db.GqlQuery("SELECT * FROM Comment WHERE article_key=:1 ORDER BY date DESC", id)
			except:
				self.response.out.write('Sth wrong happened!')
			else:
				template_values = {
					'comments': comments,
				}
				path = os.path.join(os.path.dirname(__file__), 'templates/comments.html')
				self.response.out.write(template.render(path, template_values))
		else:
			self.response.out.write('id found!')

class Add_Comment(webapp.RequestHandler):
	def post(self):
		comment = Comment()
		comment.article_key = self.request.get('article_key')
		comment.auth = self.request.get('auth')
		comment.email = self.request.get('email')
		comment.content = self.request.get('content')
	#	article.date= self.request.get('date')
		comment.put()
	def get(self):
		self.response.out.write('post only!')

class Admin(webapp.RequestHandler):
	def get(self):
		check_user(self)
		topage=1
		size=30
		if self.request.get('p') != '':
			topage = int(self.request.get('p'))
		articles = Article.all().order('-date')
		num = articles.count()
		more = (1,0)[num%size==0]
		numlist = range(1,num/size+more+1)
		template_values = {
			'articles': articles.fetch(size,(topage-1)*size),
			'topage': topage,
			'numlist': numlist,
			'num': num/size+more
		}
		path = os.path.join(os.path.dirname(__file__), 'templates/admin.html')
		self.response.out.write(template.render(path, template_values))

class Add(webapp.RequestHandler):
	def post(self):
		check_user(self)
		self.response.out.write('Add post\n')
		if self.request.get('id'):
			article = db.get(self.request.get('id'))
		else:
			article = Article()
		article.title= self.request.get('title')
		article.content = self.request.get('postcontent')
		if self.request.get('date')!="":
			article.date= datetime.datetime.strptime(self.request.get('date'),"%Y-%m-%d")
		article.put()
		self.response.out.write('add successful!')
		self.redirect('/admin')
	def get(self):
		self.response.out.write('Nothing to get!')
		self.redirect('/')

class Dele(webapp.RequestHandler):
	def get(self):
		check_user(self)
		id = self.request.get('id')
		if id:
			check_user(self)
			try:
				article = db.get(id)
				article.delete()
			except:
				self.response.out.write('Something Wrong ,WE are sorry for that!')
			else:
				self.response.out.write('delete successful!')
				self.redirect('/admin')
		else:
			self.response.out.write('Nothing to dele!')
		
class Edit(webapp.RequestHandler):
	def get(self):
		check_user(self)
		id = self.request.get('id')
		if id:
			try:
				article = db.get(id)
			#	article = db.GqlQuery("SELECT * FROM Article WHERE key=:1 ORDER BY date DESC", id)
			except:
				self.response.out.write('Something Wrong ,WE are sorry for that!')
		else:
			article=None
		template_values = {
			'article': article,
		}

		path = os.path.join(os.path.dirname(__file__), 'templates/editor.html')
		self.response.out.write(template.render(path, template_values))

			
class Norights(webapp.RequestHandler):
	def gget(self):
		if users.get_current_user() == None:
			self.response.out.write("""
			<html>
			<body>
			Only admin can do so. You even havn;t loggin?
			<p><a href="""+users.create_login_url(self.request.uri)+""">Loggin</a>
			<p><a href="javascript:history.back()">Go Back</a>
			</body>
			</html>""")
		elif not users.is_current_user_admin():
			self.response.out.write("""
			<html>
			<body>
			You have no rights to do so!   """
			+users.get_current_user().nickname()+"""   """+users.get_current_user().email()
			+"""<p><a href="javascript:history.back()">Go Back</a>
			<a href="""+users.create_logout_url(self.request.uri)+""">Logout</a>
			</body>
			</html>""")
		else:
			self.redirect('/')
	def get(self):
		article = db.get("agVyZWFreXIPCxIHQXJ0aWNsZRjx_AQM")
		comments = None
		login_url = users.create_login_url(self.request.uri)
		template_values = {
			'article': article,
			'comments': comments,
			'login_url': login_url,
		}
		path = os.path.join(os.path.dirname(__file__), 'templates/norights.html')
		self.response.out.write(template.render(path, template_values))

def main():
	application = webapp.WSGIApplication(
		[('/', Blog),
			('/blog', Blog),
			('/about', About),
			('/buzz', Buzz),
			('/getqq', Getqq),
			('/listcomment', List_Comment),
			('/addcomment', Add_Comment),
			('/admin', Admin),
			('/add',Add),
			('/edit', Edit),
			('/dele', Dele),
			('/export', Export),
			('/norights', Norights)],
		debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
	main()
