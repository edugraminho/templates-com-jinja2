from datetime import date
import csv
import os


class Post:
    def __init__(self, id, author, date_post, email, title, text):
        self.id = id
        self.author = author
        self.date_post = date_post
        self.email = email
        self.title = title
        self.text = text


    def get_last_id(self):
        posts = {'id': 0}
        with open("data/posts.csv") as f:
            for posts in csv.DictReader(f):
                pass

            return int(posts.get('id'))


    def save(self):
        filename = "data/posts.csv"
        fieldnames = ["id", "author", "date_post", "email", "title", "text"]

        new_id = Post.get_last_id(self) + 1

        valid_date_post = 0

        if len(self.date_post) == 0:
            valid_date_post = date.today()
        else:
            valid_date_post = self.date_post

        with open(filename, 'a') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if (os.stat(filename).st_size == 0):
                writer.writeheader()
            
            writer.writerow({
                "id": new_id,
                "author": self.author,
                "date_post": valid_date_post,
                "email": self.email,
                "title": self.title,
                "text": self.text
            })