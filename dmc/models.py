from django.db import models

# Create your models here.
class home(models.Model):
	top_content = models.CharField(max_length=200)
	top_phone = models.CharField(max_length=200)
	top_email = models.CharField(max_length=200)
	logo = models.ImageField()
    full_pager_img = models.ImageField()
    bold_content1_on_img = models.CharField(max_length=200)
    bold_content2_on_img = models.CharField(max_length=200)
    paragraph_on_img = models.CharField(max_length=200)
    '''
    product2 = models.ImageField()
    product3 = models.ImageField()
    product4 = models.ImageField()
    product5 = models.ImageField()
    product6 = models.ImageField()
    product1_name = models.CharField(max_length=200)
    product1_image = models.ImageField()
    product1_content = models.CharField(max_length=2000)
    product2_name = models.CharField(max_length=200)
    product2_image = models.ImageField()
    product2_content = models.CharField(max_length=2000)
    product3_name = models.CharField(max_length=200)
    product3_image = models.ImageField()
    product3_content = models.CharField(max_length=2000)
    product4_name = models.CharField(max_length=200)
    product4_image = models.ImageField()
    product4_content = models.CharField(max_length=2000)
    product5_name = models.CharField(max_length=200)
    product5_image = models.ImageField()
    product5_content = models.CharField(max_length=2000)
    product6_name = models.CharField(max_length=200)
    product6_image = models.ImageField()
    product6_content = models.CharField(max_length=2000)
'''