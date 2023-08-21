from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default1.jpg', upload_to='profile_pics')
    zodiac = models.TextField()

    def __str__(self):
     return f'{self.user.username} Profile'
    
    def save(self, ** kwargs):
       super().save()

       img = Image.open(self.image.path)
       
       if img.height > 300 and img.width > 300:
          output_size = (300, 300)
          img.thumbnail(output_size)
          img.save(self.image.path)



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)


