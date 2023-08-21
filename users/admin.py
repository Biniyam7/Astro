from django.contrib import admin
from .models import Profile
from .models import Comment

admin.site.register(Profile)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user', 'body')
    # actions = ['approve_comments']

  #  def approve_comments(self, request, queryset):
   #     queryset.update(active=True)

