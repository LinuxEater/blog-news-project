from django.db import models

# Create your models here.


class AboutUs(models.Model):
    title_about = models.CharField(max_length=100)
    description_about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_about
    
    class Meta:
        verbose_name_plural = "AboutUs"


class ContactsFunction(models.Model):
    name_url = models.CharField(max_length=100)
    url_link = models.URLField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_url
    
    class Meta:
        verbose_name_plural = "Contacts"        