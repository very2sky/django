from django.contrib import admin
from .models import Post, Category, Tag

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
admin.site.register(Category, CategoryAdmin)
class TagAdmin(admin.ModelAdmin):
    prepopulated_field ={'slug', ('name',)}

admin.site.register(Post)
admin.site.register(Tag,TagAdmin)