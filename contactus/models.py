from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.TextField(null=True)
    message = models.TextField()

    class Meta:
        db_table = 'contacts'

    def __str__(self):
        return self.first_name