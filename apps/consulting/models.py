from django.db import models
from django.utils.text import slugify
from apps.authentication.models import User

class Practice(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    description = models.TextField()
    #image = models.ImageField(upload_to='practice_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Practice,self).save(*args,**kwargs)


class Service(models.Model):
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Slot(models.Model):
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    status = models.CharField(max_length=100) # Available, Unavailable, Booked # A virer
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Billing(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100) # Stripe ID de la trasaction
    status = models.CharField(max_length=100) # Stripe status de la trasaction
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
