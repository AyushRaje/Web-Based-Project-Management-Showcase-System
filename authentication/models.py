from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ORG_TYPE = [('Government','Government'),
            ('Private','Private'),
            ('Autonomous','Autonomous'),
            ('University','University')]


class ReferralCode(models.Model):
    code = models.CharField(max_length=10,unique=True,null=True)
    referral_count  = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
class Organization(models.Model):
    name = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    type = models.CharField(max_length=100,choices=ORG_TYPE,default='Private')
    referral = models.ForeignKey(ReferralCode,on_delete=models.CASCADE,null=True)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name   
class ApiKey(models.Model):
    key = models.CharField(max_length=50,unique=True,null=True)
    request_count = models.IntegerField(default=0)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.organization.name