from django.shortcuts import render_to_response
from blog.models import Blog
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import *
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def archive(request):
	return render_to_response('archive.html',context_instance=RequestContext(request))

def login(request):
	return render_to_response('login.html',context_instance=RequestContext(request))

def register(request):
	return render_to_response('register.html',context_instance=RequestContext(request))

def taken(request):
	return render_to_response('taken.html',context_instance=RequestContext(request))
