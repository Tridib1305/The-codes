from django.db import models
from django.contrib.auth.models import User

# Create your models here.


Status_of_Product=(
    ("Lost", "Lost"),
    ("Found", "Found")
)

class Lost_Object(models.Model):
    Product_Name=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(unique=True, max_length=200)
    Name_and_Roll_no_of_Person=models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts_Lost_Object')
    Lost_on=models.DateField(auto_now_add=True)
    Description=models.TextField()
    Image=models.ImageField(upload_to='Images')
    Status=models.CharField(max_length=10, choices=Status_of_Product, default="Lost")

    class Meta:
        ordering=['-Lost_on']

    def _str_(self):
        return self.Product_Name