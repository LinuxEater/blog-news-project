from django.contrib import admin
from .models import Category,Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'category', 'author', 'status', 'is_featured', 'created_at', 'author')
    search_fields = ('title', 'slug', 'category__category_name', 'author')
    list_editable = ('is_featured',)
    list_filter = ('status', 'category', 'created_at', 'author')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'updated_at')
    search_fields = ('category_name',)
    list_filter = ('created_at', 'updated_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)


