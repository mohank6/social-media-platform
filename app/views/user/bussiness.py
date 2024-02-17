from django.contrib.auth.hashers import make_password
from django.forms.models import model_to_dict
from .accessor import (
    get_user_by_username_or_email,
    get_user_by_id,
    create_user,
    update_user,
    get_user_by_username,
    delete_user,
)


def get_user_data(user):
    user_data = model_to_dict(
        user, fields=['id', 'username', 'email', 'first_name', 'last_name', 'bio']
    )
    return user_data


def create_user_profile(data):
    user = create_user(data)
    return get_user_data(user)


def update_user_profile(data, id):
    user = update_user(data, id)
    return get_user_data(user)


def fetch_user(id=None, username=None):
    if id:
        user = get_user_by_id(id)
    if username:
        user = get_user_by_username(username)
    return get_user_data(user)


def try_delete(id):
    user = get_user_by_id(id)
    if not user:
        return False
    delete_user(user.id)
    return True


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
