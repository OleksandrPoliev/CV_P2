from django.db import models



class Contact(models.Model):
    Company = models.CharField(max_length=50)
    Email = models.EmailField()
    Title = models.CharField(max_length=255)
    Message = models.TextField(max_length=500)

    def __str__(self):
        return self.Email

#  for media and img in future
class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to='media')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Techskils(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=50)
    texts = models.TextField(max_length=2000)

    def __str__(self):
        return self.title


class FRAMEWORK(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=50)
    texts = models.TextField(max_length=2000)

    def __str__(self):
        return self.title


class TOOLS(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=50)
    texts = models.TextField(max_length=2000)

    def __str__(self):
        return self.title
