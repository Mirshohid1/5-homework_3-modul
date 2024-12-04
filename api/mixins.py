from datetime import date, timedelta
from django.core.exceptions import ValidationError
from rest_framework import serializers


class DueDateValidationMixin:
    @staticmethod
    def validate_due_date_mixin_method(due_date, use_serializer_error=False):
        today = date.today()
        max_due_date = today + timedelta(days=365)

        if due_date < today:
            message = "The due date cannot be in the past."
        elif due_date > max_due_date:
            message = "The due date cannot be more than one year from today."
        else:
            return due_date

        if use_serializer_error:
            raise serializers.ValidationError(message)
        else:
            raise ValidationError({'due_date': message})