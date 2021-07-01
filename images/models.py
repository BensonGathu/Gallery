from django.db import models
import datetime as dt
# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    # @classmethod
    # def update_location(cls,location):
    #     cls.objects.filter(location.id = location.id).update(name=)
    #     Editor.objects.filter(id = 2).update(first_name ='Kim')



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    
class Image(models.Model):
    image = models.ImageField(upload_to='image/',default="image")
    name = models.CharField(max_length=100)
    desc = models.TextField()
    loc =  models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # uploaded_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls,image_id):
        image = cls.objects.get(id=image_id)
        return image.url

    @classmethod
    def search_image(cls,category):
        images = cls.objects.filter(category=category).all()
        return images.url
    
    @classmethod
    def filter_by_location(cls,location):
        images = Image.objects.filter(location=location).all()
        return images.url
