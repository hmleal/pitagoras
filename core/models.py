from django.db import models


class PathWay(models.Model):
    """
    TODO: describe.
    """
    TYPE_CHOICES = (
        ('apoptosis', 'Apoptosis'),
    )
    name = models.CharField(max_length=140)
    acronym = models.CharField(max_length=75, blank=True)
    gmms = models.ManyToManyField('core.Gmm')
    type = models.CharField(
        max_length=75, choices=TYPE_CHOICES, default='apoptosis')

    # Audit fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pathway'
        verbose_name_plural = 'Pathways'

    def __str__(self):
        return self.name


class Gmm(models.Model):
    """
    TODO: describe.
    """
    approved_symbol = models.CharField(max_length=75, unique=True)
    active = models.BooleanField(default=True)

    # Audit fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'GMM'
        verbose_name_plural = 'GMM'

    def __str__(self):
        return self.approved_symbol
