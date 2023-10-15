from django.db  import models
from crawler.models.common_model import CommonModel

class Product(CommonModel):
    url = models.CharField(max_length=524, blank=False)
    name = models.CharField(max_length=124, blank=False)
    current_price = models.CharField(max_length=54, blank=True)
    lowest_price = models.CharField(max_length=54, blank=True)
    highest_price = models.CharField(max_length=54, blank=True)
    img_url = models.CharField(max_length=124, blank=True)


