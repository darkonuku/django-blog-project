
from django.db import models
from django.contrib import admin
import datetime

class Post(models.Model):
	title = models.CharField(max_length = 60)
	body = models.TextField()
	created = models.DateField(auto_now_add = True)
	updated = models.DateField(auto_now = True)
	def __unicode__(self):
		return self.title
	def body_first_60(self):
		return self.body[:60]

	@models.permalink
	def get_absolute_url(self):
		return ('post_detail',(), {'id':self.id,'showComments':'true/'})


class Comment(models.Model):
	body = models.TextField()
	author = models.CharField(max_length = 60)
	created = models.DateField(auto_now_add = True)
	updated = models.DateField(auto_now = True)
	post = models.ForeignKey(Post,related_name = 'message posted')

	def __unicode__(self):
		return self.author

class CommentInline(admin.TabularInline):
	model = Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','body_first_60','created')
	list_filter = ('title','created')
	search_fields = ('title','created')
	ordering = ('title','-created')
	inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
	list_display = ('body','author','created','updated')



admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)


