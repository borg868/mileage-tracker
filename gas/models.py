from django.db import models

class Fillup(models.Model):
    odometer = models.DecimalField(decimal_places=1, max_digits=8)
    purchase_date = models.DateField()
    price = models.DecimalField(name='Purchase Price', decimal_places=2, max_digits=5)
    octane_rating = models.IntegerField(max_digits=2)
    
    class Meta:
        db_table = 'fillups'