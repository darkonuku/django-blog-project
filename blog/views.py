# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
	posts = Post.objects.all()
	t = loader.get_template('blog/post_list.html')
	c = Context({'posts':posts })
	return HttpResponse(t.render(c))


def post_detail(request, id, showComments = False):
    post_value = Post.objects.get(pk = id)
    comment = ''
    if showComments != False:
        for i in Comment.objects.filter(id=id):
            comment = i.body
    else:
        pass
    #html = "<html><body><b>Post:</b><br/> %s <br/><b>Comment:</b> <br/>%s</body></html>"%(post_value,comment)
    return render_to_response('blog/.post_detail.html',{'post': post, 'comments':comments})

    
def post_search(request, term):
    found = ''
    found_posts = Post.objects.filter(body__contains = term)
    for i in found_posts:
        found += str(i.title) 
    return render_to_response('blog/post_search.html',{'posts': found, 'term':term })        

def home(request):
    return render_to_response('blog/base.html',{}) 
