from django.contrib import admin
from .models import Category,Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'author', 'status', 'is_featured', 'created_at', 'author')
    search_fields = ('title', 'slug', 'category__category_name', 'author__username')
    list_filter = ('id','title','status', 'is_featured', 'category_name','category')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)


