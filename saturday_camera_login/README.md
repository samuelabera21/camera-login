# saturday_camera_login

This folder contains the Flask app for the camera login practice project.

## What is here

- `__init__.py` creates the Flask app.
- `config.py` stores app settings and demo credentials.
- `auth/` contains the login, dashboard, and logout routes.
- `camera/` contains the face-detection helper.
- `templates/` contains the HTML pages.
- `static/` contains the CSS and JavaScript assets.

## How it works

The browser captures a webcam image, sends it to Flask, and Flask checks whether a face is visible before allowing login.
