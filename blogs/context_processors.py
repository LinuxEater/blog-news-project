from .models import Category
from assignments.models import SocialLink

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


