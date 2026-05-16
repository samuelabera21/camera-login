from dataclasses import dataclass
import base64

import cv2
import numpy as np


@dataclass(frozen=True)
class DetectionResult:
    detected: bool
    faces: int


def _decode_data_url(data_url: str) -> bytes:
    if not isinstance(data_url, str) or "," not in data_url:
        raise ValueError("Camera image is not in a valid data URL format.")

    header, encoded = data_url.split(",", 1)
    if "base64" not in header:
        raise ValueError("Camera image must be base64 encoded.")

    try:
        return base64.b64decode(encoded)
    except Exception as exc:  # pragma: no cover - defensive guard
        raise ValueError("Camera image could not be decoded.") from exc


def inspect_capture(data_url: str) -> DetectionResult:
    image_bytes = _decode_data_url(data_url)
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    if image is None:
        raise ValueError("Camera image could not be read.")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_detector = cv2.CascadeClassifier(cascade_path)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80))

    face_count = len(faces)
    return DetectionResult(detected=face_count > 0, faces=face_count)
