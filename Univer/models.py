from django.db import models


class Kompaniya(models.Model):
    title = models.CharField(max_length=50)
    birth_date = models.DateTimeField(auto_now=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "KOMPANIYA"
        verbose_name_plural = "KOMPANIYALAR"
        ordering = ['-created_ed']


class Avtomabil(models.Model):
    title = models.CharField(max_length=50, verbose_name='model')
    color = models.CharField(max_length=50)
    kuchi = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    context = models.TextField(blank=True)
    kompaniya = models.ForeignKey(Kompaniya, on_delete=models.CASCADE)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "AVTOMABIL"
        verbose_name_plural = "AVTOMABILLAR"
        ordering = ['-created_ed']