from django.db import models
import uuid

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    likes = models.IntegerField(default=0)  # Agregar campo de likes

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=64)
    customer_email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.customer_name
