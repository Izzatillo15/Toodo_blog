from django.db import models


class Maqola(models.Model):
    title = models.CharField(max_length=200)
    matn = models.TextField()
    def __str__(self):
        return self.title

class Rasmlar(models.Model):
    Maqola = models.ForeignKey(Maqola, on_delete=models.CASCADE)
    Rasm = models.FileField(upload_to='rasmlar/')
    def __str__(self):
        return self.Maqola.title