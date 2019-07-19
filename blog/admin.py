from django.contrib import admin
from .models import Post

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status', 'created_at', 'updated_at']
    actions=['make_draft','make_published']

    def content_size(self, post):
        return '{}글자'.format(len(post.content))
    content_size.short_description ='글자'

    def make_draft(self, request, queryset):
        updated_count=queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 draft상태로 변경'.format(updated_count))


    def make_published(self, request, queryset):
        updated_count=queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 published상태로 변경'.format(updated_count))
