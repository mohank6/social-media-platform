from app.models import UserProfile
from django.db.models import Q


def create_user(data):
    user = UserProfile.objects.create(**data)
    user_data = (
        UserProfile.objects.filter(id=user.id)
        .values('id', 'username', 'email', 'first_name', 'last_name', 'bio')
        .first()
    )
    return user_data


def get_user_by_username(username):
    user = (
        UserProfile.objects.filter(username=username)
        .values('id', 'username', 'email', 'first_name', 'last_name', 'bio')
        .first()
    )
    return user


def get_user_by_email(email):
    user = (
        UserProfile.objects.filter(email=email)
        .values('id', 'username', 'email', 'first_name', 'last_name', 'bio')
        .first()
    )
    return user


def get_user_by_id(id):
    user = (
        UserProfile.objects.filter(id=id)
        .values('id', 'username', 'email', 'first_name', 'last_name', 'bio')
        .first()
    )
    return user


def get_user_by_username_or_email(username, email):
    user = (
        UserProfile.objects.filter(Q(username=username) | Q(email=email))
        .values('id', 'username', 'email', 'first_name', 'last_name', 'bio')
        .first()
    )
    return user


def update_user(data, id):
    UserProfile.objects.filter(id=id).update(**data)
    user = (
        UserProfile.objects.filter(id=id)
        .values('id', 'username', 'email', 'first_name', 'last_name', 'bio')
        .first()
    )
    return user


def delete_user(id):
    user = UserProfile.objects.get(id=id)
    user.delete()
