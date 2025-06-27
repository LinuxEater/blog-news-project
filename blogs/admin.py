from django.contrib import admin
from .models import Category,Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'category', 'author', 'status', 'is_featured', 'created_at', 'author')
    search_fields = ('title', 'slug', 'category__category_name', 'author')
    list_editable = ('is_featured',)


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)


