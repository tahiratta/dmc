from django.db import models

# Create your models here.
class Menu_items(models.Model):
    class Meta:
        verbose_name_plural = "menu_items"

    menu_item_id = models.CharField(primary_key=True,max_length=20)
    menu_item_title = models.CharField(max_length=200)
    menu_item_description = models.CharField(max_length=2000)
    menu_item_image = models.ImageField()
    show_in_menu = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add =True)
    # updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.menu_item_title

class Sub_items(models.Model):
    class Meta:
        verbose_name_plural = "sub_items"

    sub_item_id = models.CharField(primary_key=True,max_length=20)
    menu_item = models.ForeignKey(Menu_items, on_delete = models.CASCADE)
    sub_item_title = models.CharField(max_length=200)
    sub_item_description = models.CharField(max_length=2000)
    sub_item_image = models.ImageField()
    # created_at = models.DateTimeField(auto_now_add =True)
    # updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.sub_item_title

class Sub_of_sub_items(models.Model):
    class Meta:
        verbose_name_plural = "sub_of_sub_items"

    sub_of_sub_item_id = models.CharField(primary_key=True,max_length=20)
    sub_item = models.ForeignKey(Sub_items, on_delete = models.CASCADE)
    sub_of_sub_item_title = models.CharField(max_length=200)
    sub_of_sub_item_description = models.CharField(max_length=2000)
    sub_of_sub_item_image = models.ImageField()
    # created_at = models.DateTimeField(auto_now_add =True)
    # updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.sub_of_sub_item_title      

class Slider(models.Model):
    class Meta:
        verbose_name_plural = "slider"

    slider_id = models.CharField(primary_key=True,max_length=20)
    slider_title = models.CharField(max_length=200)
    slider_description = models.CharField(max_length=200)
    slider_image = models.ImageField()
    # created_at = models.DateTimeField(auto_now_add =True)
    # updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.slider_title 

class Research(models.Model):
    class Meta:
        verbose_name_plural = "research"

    research_id = models.CharField(primary_key=True,max_length=20)
    research_title = models.CharField(max_length=200)
    research_description = models.CharField(max_length=200)
    research_image = models.ImageField()
    # created_at = models.DateTimeField(auto_now_add =True)
    # updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.research_title        
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


