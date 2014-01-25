#!/usr/bin/env python
# coding: utf-8
import web
from web import form

urls = (
	'/','Index',
	'/test','Test',
	'/login','Login',
	'/logout','Logout',
)

render = web.template.render("/opt/py/login")

allowed = (
	('admin','123123'),
)

web.config.debug = False
app = web.application(urls, locals())
session = web.session.Session(app, web.session.DiskStore('sessions'))

class Index:
	def GET(self):
		if session.get('logged_in',False):
			return '<h1>Login Success!!!</h1><a href="/test">test</a></br><a href="/logout">Logout</a>'
		raise web.seeother('/login')

class Login:
	def GET(self):
		return render.login()
	def POST(self):
		i = web.input()
		username = i.get('username')
		passwd = i.get('passwd')
		if (username,passwd) in allowed:
			session.logged_in = True
			web.setcookie('system_mangement', '', 60)
			raise web.seeother('/')
		else:
			return '<h1>Login Error!!!</h1></br><a href="/login">Login</a>'

class Logout:
	def GET(self):
		session.logged_in = False
		raise web.seeother("/login")

class Test:
	def GET(self):
		if session.get('logged_in',False):
			return '<h1> test login success!!!</h1></br><a href="/logout">Logout</a>'
		return '<h1>logout now</h1></br><a href="/login">Login</a>'

if __name__ == '__main__':
	app.run()


