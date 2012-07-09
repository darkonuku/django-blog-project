# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    
    return HttpResponse(post_list)



def post_detail(request, id, showComments = False):
    post_value = Post.objects.get(pk = id)
    comment = ''
    if showComments != False:
        for i in Comment.objects.filter(id=id):
            comment = i.body
    else:
        pass
    html = "<html><body><b>Post:</b><br/> %s <br/><b>Comment:</b> <br/>%s</body></html>"%(post_value,comment)
    return HttpResponse(html)
    
def post_search(request, term):
    found = ''
    found_posts = Post.objects.filter(body__contains = term)
    for i in found_posts:
        found += str(i.title) 
    return HttpResponse(found)       

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
