from django.contrib import admin
from authentication import models
# Register your models here.
admin.site.register([
    models.Organization,
    models.ReferralCode,
    models.ApiKey
])
