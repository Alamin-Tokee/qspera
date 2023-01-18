from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='profile-pic-default.jpg', upload_to='profile_pics')
    banner_image = models.ImageField(
        default='slider-1.jpg', upload_to='banner')
    job_title = models.CharField(max_length=100)
    bio = models.CharField(
        max_length=100, help_text='Short Bio (eg. I love cats and games)')
    address = models.CharField(max_length=100, help_text="Enter Your address")
    city = models.CharField(max_length=100, help_text="Enter your city")
    country = models.CharField(max_length=100, help_text="Enter your country")
    zip_code = models.CharField(
        max_length=100, help_text="Enter your zip code")
    twitter_url = models.CharField(max_length=250, default='#', blank=True,
                                   null=True, help_text="Enter # If you dont have an account")
    instagram_url = models.CharField(
        max_length=250, default="#", blank=True, null=True, help_text="Enter # If you dont have an account")

    facebook_url = models.CharField(
        max_length=250, default="#", blank=True, null=True, help_text="Enter # If you dont have an account")

    github_url = models.CharField(
        max_length=250, default="#", blank=True, null=True, help_text="Enter # If you dont have an account")

    email_confirmed = models.BooleanField(default=False)

    created_on = models.DateTimeField(default=timezone.now)

    updated_on = models.DateTimeField(auto_now=True)

    def str__(self):
        return f"{self.user.username}'s Profile"
