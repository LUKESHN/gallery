from django.db import models

# Create your models here.
class CatagoryModels(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ImageModel(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    uploaded_by=models.CharField(max_length=100)
    uploaded_at=models.DateTimeField(auto_now_add=True)
    cat=models.ForeignKey(CatagoryModels,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='uploaded_Image/')
    def __str__(self):
        return f'{self.title}\t{self.uploaded_by}\t{self.cat}\t{self.image}'