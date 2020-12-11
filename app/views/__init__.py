from flask import Blueprint, render_template, request, redirect, url_for
from app.services import list_all, create, find_one

bp = Blueprint('index_route', __name__)


@bp.route("/", methods=["GET"])
def list_posts():
    all_posts = list_all()
    if len(list_all()) == 0:
        return redirect('/post')
    else:
        return render_template("home.html", all_posts=all_posts)


@bp.route("/post", methods=["GET", "POST"])
def create_post():

    if request.method == "GET":
        return render_template("create_post.html")
    elif request.method == "POST":
        create(
            request.form["author"],
            request.form["date_post"],
            request.form["e-mail"],
            request.form["title"],
            request.form["text"]
        )
        
        all_posts = list_all()

        return render_template("home.html", all_posts=all_posts)


@bp.route("/posts/<post_id>", methods=["GET"])
def show_post(post_id):
    post_found = find_one(post_id)

    if post_found == None: 
        return redirect("/")
    else:
        return render_template("single_post.html", single_post=post_found)

    
    
