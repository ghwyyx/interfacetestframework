# from django.db import models
import mongoengine

# Create your models here.
class InterfaceModel(mongoengine.Document):
    http_method = mongoengine.StringField(max_length=30)
    url = mongoengine.URLField()
    request_body = mongoengine.StringField()
    expect_num = mongoengine.StringField()

    # class Meta:
    #     db_table = 'gh_save'

