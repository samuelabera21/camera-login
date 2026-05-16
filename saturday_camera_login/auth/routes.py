from functools import wraps

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from .service import verify_credentials
from ..camera.detector import inspect_capture

auth_bp = Blueprint("auth", __name__)


def login_required(view_function):
    @wraps(view_function)
    def wrapped_view(*args, **kwargs):
        if not session.get("username"):
            return redirect(url_for("auth.login"))
        return view_function(*args, **kwargs)

    return wrapped_view


@auth_bp.route("/", methods=["GET"])
def login():
    return render_template("login.html")


@auth_bp.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")
    camera_frame = request.form.get("camera_frame", "")

    if not username or not password:
        flash("Enter both username and password.", "error")
        return redirect(url_for("auth.login"))

    if not camera_frame:
        flash("Camera capture is required before login.", "error")
        return redirect(url_for("auth.login"))

    try:
        detection = inspect_capture(camera_frame)
    except ValueError as exc:
        flash(str(exc), "error")
        return redirect(url_for("auth.login"))

    if not detection.detected:
        flash("Face not detected. Center your face in the camera and try again.", "error")
        return redirect(url_for("auth.login"))

    if not verify_credentials(username, password):
        flash("Invalid username or password.", "error")
        return redirect(url_for("auth.login"))

    session["username"] = username
    session["faces_seen"] = detection.faces
    flash("Login successful.", "success")
    return redirect(url_for("auth.dashboard"))


@auth_bp.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    return render_template(
        "dashboard.html",
        username=session.get("username"),
        faces_seen=session.get("faces_seen", 0),
    )


@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("auth.login"))
