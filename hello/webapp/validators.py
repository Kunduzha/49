from django.core.validators import BaseValidator, ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MinLengthValidators(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)s! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)



def str_value(string):
    try:
        if type(int(string)) is int:
            raise ValidationError("The value can't be the integer")
    except ValidationError as e:
        raise e
    except ValueError:
        pass
