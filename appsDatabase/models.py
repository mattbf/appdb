from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify
from datetime import datetime


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Tags(models.Model):
    tag = models.CharField("tag", max_length=255)


class AppsDatabase(models.Model):
    B2B = 'B2B'
    B2C = 'B2C'
    C2C = 'C2C'
    P2C = 'P2C'
    P2P = 'P2P'
    P2B = 'P2B'
    BUSINESS_TYPE_CHOICES = (
        (B2B, 'B2B'),
        (B2C, 'B2C'),
        (C2C, 'C2C'),
        (P2C, 'P2C'),
        (P2P, 'P2P'),
        (P2B, 'P2B'),
    )
    FREEMIUM = 'Freemium'
    SAAS = 'SaaS'
    PAAS = 'PaaS'
    BUSINESS_MODEL_CHOICES = (
        (FREEMIUM, 'Freemium'),
        (SAAS, 'SaaS'),
        (PAAS, 'PaaS'),
    )

    name = models.CharField("name", max_length=255)
    website = models.URLField("website", max_length=255)
    launchYear = models.IntegerField(
        "year_launched", validators=[MinValueValidator(1984), max_value_current_year])
    serviceType = models.CharField(
        max_length=3, choices=BUSINESS_TYPE_CHOICES, default='B2C')
    businessModel = models.CharField(
        max_length=10, choices=BUSINESS_MODEL_CHOICES, default='SAAS')
    description = models.TextField(blank=True, null=True)
    monitization = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tags)
    createdOn = models.DateTimeField("Created On", auto_now_add=True)

    def __str__(self):
        return self.name
