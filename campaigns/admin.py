from django.contrib import admin
from .models import UserProfile, Campaign, Donation

admin.site.register(UserProfile)
admin.site.register(Campaign)
admin.site.register(Donation)