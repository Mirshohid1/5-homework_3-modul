from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from datetime import date

class Todo(models.Model):
    title = models.CharField(
        max_length=255,
        validators=MinLengthValidator(3, "The description must contain at least 12 characters")
    )
    description = models.TextField(
        validators=MinLengthValidator(12, "The description must contain at least 12 characters")
    )
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def clean(self):
        """
        Validation and Data Processing.
        """

        self.title = self.title.strip().title()
        self.description = self.description.strip()

        if self.due_date < date.today():
            raise ValidationError({'due_date': "The value of due_date cannot be earlier than the current time"})

    def __str__(self):
        return f"Todo {self.title}: -> ({self.due_date})"
