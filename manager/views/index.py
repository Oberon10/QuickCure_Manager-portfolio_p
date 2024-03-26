from flask import Blueprint, render_template

bp = Blueprint("index", __name__, url_prefix="/")

# Create a Home route 
@bp.route("/")
def index():
  return render_template("index.html")