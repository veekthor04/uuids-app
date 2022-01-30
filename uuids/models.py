from django.db import models


class UUIDStamp(models.Model):
    uuid_obj = models.UUIDField()
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-datetime"]  # latest come first

    def get_uuid_stamp_dic(self) -> dict:
        """Generates a dictionary of key as uuid_obj and value as datetime

        Returns:
            dict: [description]
        """
        return {str(self.datetime.replace(tzinfo=None)): self.uuid_obj.hex}
