from django.db import models

# Create your models here.

class Users(models.Model):
    uid = models.CharField(max_length = 250)

    def __unicode__(self):
        return self.uid


class data(models.Model):
    uid = models.ForeignKey(Users , null=True)
    typeof = models.CharField(max_length = 100 , null=True)
    date = models.CharField(max_length = 1000 , null=True)
    # time= models.CharField(max_length = 1000,null=True)
    duration= models.CharField(max_length = 10000, null=True)
    severity= models.CharField(max_length = 1000, null=True)
    review = models.CharField(max_length = 1000, null=True , default = 'NULL')
    medicine = models.CharField(max_length = 1000, null=True , default = 'NULL')
    
    def __unicode__(self):
        return unicode(self.typeof) or u''