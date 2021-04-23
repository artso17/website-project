from django.db import models

# Create your models here.


class About(models.Model):
    judul = models.CharField(max_length=200)
    gambar = models.ImageField(null=True, blank=True, upload_to='images/')
    about = models.CharField(max_length=200)
    birthday = models.DateField()
    website = models.CharField(max_length=200)
    phone = models.IntegerField()
    city = models.CharField(max_length=200)
    age = models.IntegerField()
    degree = models.CharField(max_length=200)
    mail = models.EmailField()
    freelancer = models.BooleanField(default=False)

    def __str__(self):
        return '{}.{}'.format(self.id, self.judul)


class Skill(models.Model):
    judul = models.CharField(max_length=50)
    nilai = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{}.{}'.format(self.id, self.judul)
