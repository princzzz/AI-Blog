from django.contrib import admin
from .models import Contact , PreEvent, Blog, PostEvent, Email

admin.site.register(Contact)

@admin.register(PreEvent)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)

@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)

@admin.register(PostEvent)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)

admin.site.register(Email)