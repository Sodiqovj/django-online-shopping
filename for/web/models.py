from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    gif = models.ImageField(default='https://online-shopping-page.netlify.app/animation_500_ksx6wx13.gif')
    
    def __str__(self):
        return self.text
