from django.db import models

class User(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    username = models.CharField(max_length=15)
    
    def __unicode__(self):
        return self.username

    class Meta:
        db_table = 'users'

class Fillup(models.Model):
    user = models.ForeignKey('User')
    purchase_date = models.DateField()
    odometer = models.IntegerField()
    gallons = models.DecimalField(decimal_places=3, max_digits=5)
    price = models.DecimalField('Purchase Price', decimal_places=2, max_digits=5)
    octane_rating = models.IntegerField()
    
    class Meta:
        db_table = 'fillups'