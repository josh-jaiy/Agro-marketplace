from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Seller

@receiver(post_save, sender=User)
def create_seller_for_new_user(sender, instance, created, **kwargs):
    if created:
        Seller.objects.create(user=instance)
