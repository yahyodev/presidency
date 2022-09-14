from django.core.exceptions import ValidationError


def validate_rating(value):
    if value < 1:
        raise ValidationError('Enter number bigger or equal to 1')
    if value > 5:
        raise ValidationError('Enter number smaller or equal to 5')
