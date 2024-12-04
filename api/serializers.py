from rest_framework import serializers
from .models import Todo
from .mixins import DueDateValidationMixin
from datetime import date


class TodoSerializer(serializers.ModelSerializer, DueDateValidationMixin):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'due_date', 'is_completed']

    def validate_due_date(self, value: date) -> date:
        """
        due_date validation with the True flag (for the serializer)
        Args:
            value: This parameter accepts the due_date field

        Returns: Returns the value after validation
        """

        return self.validate_due_date_mixin_method(value, True)
