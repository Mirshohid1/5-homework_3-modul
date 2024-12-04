from django.db import models
from django.core.validators import MinLengthValidator
from .mixins import DueDateValidationMixin


class Todo(models.Model, DueDateValidationMixin):
    title = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(3, "The description must contain at least 3 characters")]
    )
    description = models.TextField(
        validators=[MinLengthValidator(12, "The description must contain at least 12 characters")]
    )
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def clean(self):
        """
        Validation and Data Processing.
        due_date validation with the False flag (for the model)
        """

        self.title = self.title.strip().title()
        self.description = self.description.strip()
        self.due_date = self.validate_due_date_mixin_method(self.due_date)

    def __str__(self):
        return f"Todo {self.title}: -> ({self.due_date})"
