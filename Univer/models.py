from django.db import models

class Kurs(models.Model):
    title = models.CharField(max_length=30)
    start = models.TimeField(blank=True)
    stop = models.TimeField(blank=True)
    totalStudent = models.IntegerField(default=0)
    discription = models.CharField(max_length=255,blank=True)
    create_ed = models.DateTimeField(auto_now_add=True)
    update_ed = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "KURS"
        verbose_name_plural = "Kurslar"
        ordering = ['-create_ed']

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50,blank=True)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    create_ed = models.DateTimeField(auto_now_add=True)
    update_ed = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"
        ordering = ['-create_ed']

    def __str__(self):
        return self.fullname

