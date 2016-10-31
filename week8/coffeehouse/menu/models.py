from django.db import models


class Special(models.Model):
    created_user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    picture = models.FileField()

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return "http://www.brian-coffee-spot.com/wp-content/uploads/2016/07/Thumbnail-World-of-Coffee-2016-DSC_2475t.jpg"
