from django.contrib.auth.hashers import make_password
from .accessor import get_user_by_username_or_email, get_user_by_id


def validate_data(data, required_fields, optional_fields, is_create=False):
    validated_data = {}
    data_keys = data.keys()
    for field in required_fields:
        if field not in data_keys:
            return False
        validated_data[field] = data[field]
    if is_create:
        if validated_data['password']:
            validated_data['password'] = make_password(validated_data['password'])
        user_exists = get_user_by_username_or_email(
            validated_data['username'], validated_data['email']
        )
        if user_exists:
            return False
    for opt_field in optional_fields:
        try:
            validated_data[opt_field] = data[opt_field]
        except:
            pass
    return validated_data


def validate_data_signup(data):
    required_fields = ['username', 'password', 'email', 'first_name', 'last_name']
    optional_fields = ['bio']
    return validate_data(data, required_fields, optional_fields, is_create=True)


def validate_data_update(data, id):
    required_fields = []
    optional_fields = ['first_name', 'last_name', 'bio']
    user_exists = get_user_by_id(id)
    if not user_exists:
        return False
    return validate_data(data, required_fields, optional_fields)
