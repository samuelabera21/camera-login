const form = document.querySelector("[data-login-form]");
const video = document.querySelector("[data-camera-video]");
const preview = document.querySelector("[data-camera-preview]");
const statusText = document.querySelector("[data-camera-status]");
const cameraInput = document.querySelector("[data-camera-input]");

let stream = null;
let submissionTriggered = false;

async function startCamera() {
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    statusText.textContent = "This browser does not support camera access.";
    return;
  }

  try {
    stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" }, audio: false });
    video.srcObject = stream;
    statusText.textContent = "Camera ready. Center your face before signing in.";
  } catch (error) {
    statusText.textContent = "Camera permission is blocked. Allow access and refresh the page.";
  }
}

function captureFrame() {
  if (!video.videoWidth || !video.videoHeight) {
    throw new Error("Camera is still starting. Wait a moment and try again.");
  }

  const canvas = document.createElement("canvas");
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;

  const context = canvas.getContext("2d");
  context.drawImage(video, 0, 0, canvas.width, canvas.height);

  const imageData = canvas.toDataURL("image/jpeg", 0.92);
  cameraInput.value = imageData;
  preview.src = imageData;
}

form.addEventListener("submit", (event) => {
  if (submissionTriggered) {
    return;
  }

  event.preventDefault();

  try {
    captureFrame();
    submissionTriggered = true;
    statusText.textContent = "Submitting login with a fresh camera snapshot...";
    form.submit();
  } catch (error) {
    statusText.textContent = error.message;
  }
});

window.addEventListener("beforeunload", () => {
  if (stream) {
    stream.getTracks().forEach((track) => track.stop());
  }
});

startCamera();
