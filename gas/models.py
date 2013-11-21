from django.db import models

class Fillup(models.Model):
    purchase_date = models.DateField()
    odometer = models.IntegerField()
    gallons = models.DecimalField(decimal_places=3, max_digits=5)
    price = models.DecimalField(name='Purchase Price', decimal_places=2, max_digits=5)
    octane_rating = models.IntegerField(max_digits=2)
    
    class Meta:
        db_table = 'fillups'