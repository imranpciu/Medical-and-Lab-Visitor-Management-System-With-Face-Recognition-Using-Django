import base64
import cv2
import os
import numpy as np
from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView
import dlib
import face_recognition
from user_details.models import User


class VerifyUserView(TemplateView):
    template_name = "verify_user.html"

    def post(self, request):
        sphoto = request.POST.get("sphoto")
        recognition_result, user_id = perform_face_recognition(sphoto)
        if recognition_result:
            try:
                user = User.objects.get(user_id=user_id)
                return render(request, "verify_user_success.html", {"user": user})
            except User.DoesNotExist:
                # Handle the case where the user is not found in the database
                return render(request, "verify_user_failed.html")
        else:
            return render(request, "verify_user_failed.html")


def perform_face_recognition(image_data):
    media_root = settings.MEDIA_ROOT

    user_images_dir = os.path.join(media_root, "users")
    temp_images_dir = os.path.join(media_root, "temp")

    img = cv2.imdecode(
        np.fromstring(base64.b64decode(image_data.split(",")[1]), np.uint8),
        cv2.IMREAD_COLOR,
    )

    resized_img = cv2.resize(img, (300, 300))

    temp_image_path = os.path.join(temp_images_dir, "captured_image.png")

    cv2.imwrite(temp_image_path, resized_img)

    face_detector = dlib.get_frontal_face_detector()
    shape_predictor = dlib.shape_predictor(
        os.path.join(os.path.dirname(__file__), "shape_predictor_68_face_landmarks.dat")
    )
    face_recognizer = dlib.face_recognition_model_v1(
        os.path.join(
            os.path.dirname(__file__), "dlib_face_recognition_resnet_model_v1.dat"
        )
    )

    dlib_img = dlib.load_rgb_image(temp_image_path)

    face_rects = face_detector(dlib_img)

    if len(face_rects) == 0:
        return False, None

    dlib_faces = dlib.full_object_detections()

    for face_rect in face_rects:
        dlib_faces.append(shape_predictor(dlib_img, face_rect))

    captured_face_descriptors = [
        np.array(face_recognizer.compute_face_descriptor(dlib_img, face_landmarks))
        for face_landmarks in dlib_faces
    ]

    for filename in os.listdir(user_images_dir):
        user_image_path = os.path.join(user_images_dir, filename)
        user_img = dlib.load_rgb_image(user_image_path)

        user_face_rects = face_detector(user_img)
        user_face_landmarks = [
            shape_predictor(user_img, face_rect) for face_rect in user_face_rects
        ]
        user_face_descriptors = [
            np.array(face_recognizer.compute_face_descriptor(user_img, landmarks))
            for landmarks in user_face_landmarks
        ]

        for captured_descriptor in captured_face_descriptors:
            distances = [
                np.linalg.norm(captured_descriptor - user_descriptor)
                for user_descriptor in user_face_descriptors
            ]
            min_distance = min(distances)
            if min_distance < 0.5:  # Adjust the distance threshold to improve accuracy
                # Perform liveness detection
                liveness_result = perform_liveness_detection(img)
                if liveness_result:
                    user_id = os.path.splitext(filename)[
                        0
                    ]  # Extract the user ID from the image filename
                    return True, user_id

    return False, None


def perform_liveness_detection(image):
    # Load the face detector model
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    for x, y, w, h in faces:
        # Extract the face ROI
        face_roi = gray[y : y + h, x : x + w]

        # Resize the face ROI to a fixed size
        face_roi = cv2.resize(face_roi, (100, 100))

        # Normalize the face ROI
        face_roi = face_roi.astype("float") / 255.0
        face_roi = np.expand_dims(face_roi, axis=0)
        face_roi = np.expand_dims(face_roi, axis=-1)

        # Perform liveness detection using face_recognition library
        encodings = face_recognition.face_encodings(image, [(y, x + w, y + h, x)])[0]
        matches = face_recognition.compare_faces([encodings], encodings, tolerance=0.9)

        # Check if any matches are found, indicating a live face
        if any(matches):
            return True

    return False
