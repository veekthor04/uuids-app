from django.db import models

# Create your models here.
class UUIDStamp(models.Model):
    uuid_obj = models.UUIDField()
    datetime = models.DateTimeField(auto_now_add=True)

    # latest come first
    class Meta:
        ordering = ['-datetime']

    # method to generate a dictionary of key as uuid_obj and value as datetime
    def get_uuid_stamp_dic(self):
        return {str(self.datetime.replace(tzinfo=None)): self.uuid_obj.hex}
        
