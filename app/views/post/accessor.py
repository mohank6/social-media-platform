from app.models import Post, Comment, Like


def create_post(data):
    post = Post.objects.create(**data)
    return post


def update_post(data, id):
    post = Post.objects.filter(id=id).first()
    for key, value in data.items():
        setattr(post, key, value)
    post.save()
    return post


def delete_post(id):
    user = Post.objects.get(id=id)
    user.delete()


def get_posts():
    posts = Post.objects.all()
    return posts


def get_post_by_id(id):
    post = Post.objects.filter(id=id).first()
    return post


def get_comments_of_post(post):
    comments = Comment.objects.filter(post=post).all()
    return comments


def get_posts_by_user(user):
    posts = Post.objects.filter(user=user).all()
    return posts


def like_post(post, user):
    Like.objects.create(post=post, user=user)


def get_like(post, user):
    like = Like.objects.filter(post=post, user=user).first()
    return like


def comment_post(post, user, text):
    comment = Comment.objects.create(post=post, user=user, text=text)
    return comment
