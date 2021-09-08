from django.db import models

# Create your models here.
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )

    def data(self):
        return {"title": self.title, 'text': self.text, 'created_at': self.created_at.strftime("%d-%m-%y"), 'id': self.id}
