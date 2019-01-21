from django.core.exceptions import ValidationError


def validate_file_size(self, value):
    if value.size > 5245760:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
