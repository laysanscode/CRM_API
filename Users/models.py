from django.db import models
class Import_User(models.Model):
    user_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=1000)
    ProfilePic = models.ImageField(upload_to="ImportUser/")
    Address = models.CharField(max_length=1000)
    Country = models.CharField(max_length=1000)
    State = models.CharField(max_length=1000)
    City = models.CharField(max_length=1000)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

    @property
    def id(self):
        return self.user_id
