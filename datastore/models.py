from django.db import models

class StkEk(models.Model):
    inspection_id = models.AutoField(primary_key=True)
    vin = models.CharField(max_length=17)
    inspection_date = models.DateField()
    valid_to = models.DateField()
    service_address = models.CharField(max_length=255)
    inspection_type = models.CharField(max_length=10)
    protocol = models.CharField(max_length=255)
    result = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'stk_ek'

class Insurance(models.Model):
    insurance_id = models.AutoField(primary_key=True)
    vin = models.CharField(max_length=17)
    insurance_date = models.DateField()
    valid_to = models.DateField()
    insurance_company = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'insurance'

class Vignette(models.Model):
    vignette_id = models.AutoField(primary_key=True)
    vin = models.CharField(max_length=17)
    type = models.CharField(max_length=50)
    valid_from = models.DateField()
    valid_to = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'vignette'

class Mileage(models.Model):
    vin = models.CharField(max_length=17)
    kilometers = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mileage'
