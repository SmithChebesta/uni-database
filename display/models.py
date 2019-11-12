from django.db import models

import datetime


class Tag(models.Model):
    tag = models.TextField(primary_key=True)
    description = models.TextField(null=True)


class Customer(models.Model):
    customer_name = models.TextField()
    customer_id = models.TextField(primary_key=True)
    accounting_name = models.TextField(blank=True, default='-')
    accounting_contact = models.TextField(blank=True, default='-')
    technical_name = models.TextField(blank=True, default='-')
    technical_contact = models.TextField(blank=True, default='-')
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)
    distributor_name = models.TextField(blank=True, default='-')


class Webapp (models.Model):
    system_name = models.TextField(primary_key=True)
    customer_id = models.ForeignKey("Customer", on_delete=models.CASCADE)
    product = models.TextField()
    super_admin_id = models.TextField()
    super_admin_password = models.TextField()
    url = models.URLField(max_length=200)
    drive = models.URLField(max_length=200, blank=True, default='-')
    max_users = models.IntegerField()
    organizationID = models.TextField()
    status = models.BooleanField(default=False)


class service(models.Model):
    customer_id = models.ForeignKey("Customer", on_delete=models.CASCADE)
    system_name = models.OneToOneField("Webapp", on_delete=models.CASCADE)
    SKU = models.TextField(default='Some generated text')
    service_start_date = models.DateField()
    service_end_date = models.DateField()
    product_type = models.TextField()
    service_type = models.TextField()

    @property
    def status(self):
        now = datetime.date.today()
        return self.service_start_date < now and now < self.service_end_date

    @property
    def calculate_duration(self):
        return f'{(self.service_end_date - self.service_start_date).days} days'


class Gateway(models.Model):
    gateway_id = models.TextField(primary_key=True)
    customer_id = models.ForeignKey("Customer", on_delete=models.CASCADE)

    refresh_rate = models.FloatField(blank=True, default=0)
    uid_list = models.TextField(blank=True, default='-')
    system = models.TextField(blank=True, default='-')
    IMEI_MAC = models.TextField(blank=True, default='-')
    firmware_upgrade = models.TextField(blank=True, default='-')
    moblie_number = models.TextField(blank=True, default='-')
    max_sms = models.IntegerField(blank=True, default=0)
