# Camera Login Practice Repo

This repository is a small practice workspace that mixes two things:

- a Flask login page with webcam capture and face detection
- a set of simple placeholder Python and text practice files

## How to run the app

1. Install the dependencies:

```bash
pip install -r requirements.txt
```

2. Start the app:

```bash
python run.py
```

3. Open the local address shown in the terminal, usually:

```text
http://127.0.0.1:5000/
```

4. Allow camera access in your browser.

Demo credentials:

- `student / practice123`
- `admin / camera456`

## Repository map

### Root files

| File | Purpose |
| --- | --- |
| `.gitignore` | Keeps Python cache files, bytecode, and the virtual environment out of git. |
| `app.py` | Flask entry point that creates the app and runs it. |
| `requirements.txt` | Lists the Python packages needed for the project. |
| `run.py` | Alternate app launcher that does the same job as `app.py`. |
| `README.md` | Explains the repository structure and how to use it. |

### Flask app package: `saturday_camera_login/`

| File | Purpose |
| --- | --- |
| `saturday_camera_login/__init__.py` | App factory that creates the Flask application and registers routes. |
| `saturday_camera_login/config.py` | App settings and demo login credentials. |
| `saturday_camera_login/auth/__init__.py` | Marks the authentication folder as a Python package. |
| `saturday_camera_login/auth/routes.py` | Main authentication routes: login, dashboard, and logout. |
| `saturday_camera_login/auth/service.py` | Simple credential verification logic. |
| `saturday_camera_login/camera/__init__.py` | Marks the camera folder as a Python package. |
| `saturday_camera_login/camera/detector.py` | Decodes the captured image and checks it for faces with OpenCV. |
| `saturday_camera_login/templates/base.html` | Shared layout used by the app pages. |
| `saturday_camera_login/templates/login.html` | Login page with username, password, and webcam capture. |
| `saturday_camera_login/templates/dashboard.html` | Post-login screen that shows the signed-in user. |
| `saturday_camera_login/static/css/style.css` | Styling for the full interface. |
| `saturday_camera_login/static/js/camera.js` | Browser-side camera access and frame capture script. |

### Practice Python files: `file1.py` to `file20.py`

These files are simple starter scripts for Python practice. They all currently contain the same basic structure:

```python
"""Starter Python file."""


def main():
    print("This is file placeholder")


if __name__ == "__main__":
    main()
```

You can use them to practice:

- functions
- conditionals
- loops
- importing modules
- small exercises

### Text practice folder: `today/`

The `today/` folder contains text practice files:

- `today/file1.txt` to `today/file15.txt`

These are plain text files you can use for notes, small exercises, or sample output.

## What the app does

The login page uses the browser camera to capture one image when you press the login button. That image is sent to the Flask backend, where OpenCV checks whether a face is visible. If the face check passes and the username/password are correct, the app opens the dashboard page.

## Notes

- This is a practice project, not production authentication.
- The camera check is a simple face-detection demo, not real identity verification.
- The placeholder `file*.py` and `today/*.txt` files are kept as learning material.
