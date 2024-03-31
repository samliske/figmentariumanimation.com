from flask import Blueprint, render_template, request
from website import figment_code

views = Blueprint('views', __name__)

# these are my server-side routes

@views.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@views.route("/music")
def music():
    return render_template("music.html")

@views.route("/fieldrecordings")
def field_recordings():
    return render_template("fieldrecordings.html")

@views.route("/animation")
def animation():
    return render_template("animation.html")

@views.route("/figment", methods=['GET', 'POST'])
def figment():
    if request.method=='POST':
        message = request.form.get("message")
        
        bot_response = figment_code.figment_bot(message)
        return render_template("figment.html", user_input=message, bot_response=bot_response)
    else:
        return render_template("figment.html")

    
