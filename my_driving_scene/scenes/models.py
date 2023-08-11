from django.db import models

class module(models.Model):
    name=models.CharField(max_length=255,null="111")
    describtion=models.CharField(max_length=255,null="111")
    def __str__(self):
        return f"{self.name}"


    
class Scene(models.Model):
    name=models.CharField(max_length=255,null=False)
    describtion=models.CharField(max_length=255,null=False)
    weather=models.CharField(max_length=255)
    road=models.CharField(max_length=255)
    action=models.CharField(max_length=255)
    objecter=models.CharField(max_length=255)
    action_objecter=models.CharField(max_length=255)
    image=models.ImageField(upload_to='img',null=True)
    file=models.FileField(upload_to='scenicFile',null=True)
    modules=models.ManyToManyField(module,blank=True)
    video=models.FileField(('视频'),upload_to='videos',null=True,blank='true')
    def module_list(self):
        return ','.join([i.name for i in self.modules.all()])
    def __str__(self):
        return f"{self.name}"

class report (models.Model):
    name=models.CharField(max_length=255)
    scenename=models.ForeignKey(Scene,on_delete=models.CASCADE,null=True)
    data = models.TextField(null=True)
    image = models.ImageField(upload_to='img',null=True)
    file = models.FileField(upload_to='scenicFile',null=True)
    def __str__(self):
        return f"{self.name}"



