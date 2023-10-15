from django.db  import models
from crawler.models.common_model import CommonModel

class Users(CommonModel):
    email = models.EmailField(blank=False, primary_key=True)
    name = models.CharField(max_length=124, blank=True)