from email import message
from django.db import models
from core import models as core_models

# Create your models here.
class Conversation(core_models.TimeStampedModel):
    """converstion"""

    participants = models.ManyToManyField("users.User")

    def __str__(self):
        return str(self.create)


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} say: {self.text}"
