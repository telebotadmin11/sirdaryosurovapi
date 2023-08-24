from django.db import models
# Create your models here.
class Sorov(models.Model):
    fish = models.CharField(max_length=500)
    idpassport = models.CharField(max_length=500)
    Yashashmanzili = models.CharField(max_length=500)
    mfynomi = models.CharField(max_length=500)
    kochanomi = models.CharField(max_length=500)
    telefonraqami = models.CharField(max_length=500)
    rasmvavidio = models.FileField()
    matn = models.TextField()

    def __str__(self) -> str:
        return self.fish