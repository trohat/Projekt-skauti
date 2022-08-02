from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Skaut(models.Model):
    jmeno = models.CharField(max_length=60)
    prezdivka = models.CharField(max_length=100)
    vek = models.IntegerField()
    slozil_zkousku = models.BooleanField()

    def get_absolute_url(self):
        return reverse("detail", args=[self.jmeno])

    def __str__(self):
        return f"{self.jmeno} ({self.prezdivka})"

    class Meta:
        verbose_name_plural = "Skauti"