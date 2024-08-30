from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import PeopleProfile, PeopleCategory

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Get or create a default category
        default_category, created = PeopleCategory.objects.get_or_create(category="Default Category")
        PeopleProfile.objects.create(user=instance, category=default_category)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.peopleprofile.save()
