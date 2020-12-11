from app.models import Post
import csv
from environs import Env

env = Env()
env.read_env()


def create(author, date_post, email, title, text):
    new_post = Post(id, author, date_post, email, title, text)
    new_post.save()


def list_all():
    posts_list = list()
    with open(env("POSTS_CSV")) as f:
        reader = csv.DictReader(f)

        for line in reader:
            posts_list.append(line)

        return posts_list


def find_one(post_id):
    with open(env("POSTS_CSV")) as f:
        reader = csv.DictReader(f)

        for line in reader:
            if int(line['id']) == int(post_id):
                return line
