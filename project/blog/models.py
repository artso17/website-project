from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.


class About(models.Model):
    judul = models.CharField(max_length=200)
    gambar = models.ImageField(null=True, blank=True, upload_to='images/')
    about = models.CharField(max_length=200)
    birthday = models.DateField()
    website = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=200)
    age = models.IntegerField()
    degree = models.CharField(max_length=200)
    email = models.EmailField()
    freelancer = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return '{}.{}'.format(self.id, self.judul)


class Kategori(models.Model):
    judul = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super(Kategori, self).save()

    def __str__(self):
        return '{}'.format(self.judul)


class Skill(models.Model):
    judul = models.CharField(max_length=50)
    nilai = models.PositiveSmallIntegerField()
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super(Skill, self).save()

    def __str__(self):
        return '{}'.format(self.judul)


class Service(models.Model):
    judul = models.CharField(max_length=100)
    icon = models.ImageField(null=True, blank=True, upload_to='images/')
    deskripsi = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.judul)


class Portfolio(models.Model):
    judul = models.CharField(max_length=100)
    published = models.DateTimeField(auto_now_add=True)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    gambar1 = models.ImageField(null=True, blank=True, upload_to='images/')
    gambar2 = models.ImageField(null=True, blank=True, upload_to="images/")
    deskripsi1 = RichTextField(blank=True, null=True)

    deskripsi2 = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.skill)
        super(Portfolio, self).save()

    def __str__(self):
        return '{}. {}'.format(self.id, self.judul)


class Blog(models.Model):
    judul = models.CharField(max_length=200)
    published = models.DateTimeField(auto_now_add=True)
    gambar1 = models.ImageField(null=True, blank=True, upload_to='images/')
    gambar2 = models.ImageField(null=True, blank=True, upload_to='images/')
    deskripsi = RichTextField()
    deskripsi2 = RichTextField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    kategori = models.ForeignKey(
        Kategori, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.kategori)
        super(Blog, self).save()

    def __str__(self):
        return '{}.{}'.format(self.id, self.judul)


class Contact(models.Model):
    subject = models.CharField(max_length=200)
    published = models.DateTimeField(auto_now_add=True)
    pengirim = models.CharField(max_length=200)
    email = models.EmailField()
    deskripsi = models.TextField()

    def __str__(self):
        return '{}.{}'.format(self.pengirim, self.subject)
