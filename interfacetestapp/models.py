# from django.db import models
# @author='guhao'
# @time:2019/09/03 19:30:00

import mongoengine

# Create your models here.
class InterfaceModel(mongoengine.Document):
    http_method = mongoengine.StringField(max_length=30)
    url = mongoengine.URLField()
    request_body = mongoengine.StringField()
    interface_name = mongoengine.StringField()

    # class Meta:
    #     db_table = 'gh_save'

