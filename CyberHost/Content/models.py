from django.db import models

# Create your models here.


class ThreatPostLinks(models.Model):
    url = models.URLField(max_length=200)
    alt = models.CharField(max_length=200)

    def __str__(self):
        return self.alt

# EOF
