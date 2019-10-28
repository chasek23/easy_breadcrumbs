from django.urls import reverse

class Breadcrumbs(object):

	Crumbs = []

	def make_crumb(self, url, name, *args, **kwargs):
		self.Crumbs.append(Crumb(url, name))

	def make_django_crumb(self, view_name, name, **kwargs):
		url = reverse(view_name, **kwargs)
		self.make_crumb()




class Crumb(object):
		
	def __init__(self, url, name):
		self.url = url
		self.name = name
