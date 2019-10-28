from django.urls import reverse

class Breadcrumbs(object):

	Crumbs = []

	def add_crumb(self, url, name, *args, **kwargs):
		self.Crumbs.append(self.make_crumb(url, name, *args, **kwargs))

	def make_crumb(self, url, name, *args, **kwargs):
		return Crumb(url, name, *args, **kwargs)

	def make_django_crumb(self, view_name, name, **kwargs):
		url = reverse(view_name, **kwargs)
		self.make_crumb()


class Crumb(object):
		
	def __init__(self, url, name, *args, **kwargs):
		self.url = url
		self.name = name
		self.args = args
		self.kwargs = kwargs
