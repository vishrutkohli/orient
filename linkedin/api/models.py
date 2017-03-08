from django.db import models


# Create your models here.

class Users(models.Model):
    idn = models.CharField(max_length = 250)

    def __unicode__(self):
        return self.idn


class data(models.Model):
    mac_address = models.CharField(max_length = 250,null=True)
    idm = models.ForeignKey(Users , null=True)
    first_name = models.CharField(max_length = 100 , null=True)
    last_name = models.CharField(max_length = 1000 , null=True)
    headline= models.CharField(max_length = 1000,null=True)
    location= models.CharField(max_length = 10000, null=True)
    summary= models.CharField(max_length = 1000, null=True)
    specialties= models.CharField(max_length = 1000, null=True)
    position = models.CharField(max_length = 250, null=True)
    picture_url = models.CharField(max_length = 250, null=True)
    public_profile_url = models.CharField(max_length = 11250, null=True)
    email_address = models.CharField(max_length = 250, null=True)
    
    def __unicode__(self):
        return self.email_address

class login(models.Model):
    email = models.EmailField(max_length = 250)
    password1 = models.CharField(max_length = 25)


    def __unicode__(self):
        return self.email


class Saved(models.Model):
    idx = models.ForeignKey(Users)


    saved_id = models.CharField(max_length = 250)
    
    def __unicode__(self):
        return self.saved_id     

     


