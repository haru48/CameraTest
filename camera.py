import cv2
import streamlit as st
st.title("QRコード読みとり")
FRAME_WINDOW = st.image([])
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    ret, frame = cap.read()
    data = detector.detectAndDecode(frame)
    if data[0] != "":
        st.write(data[0])
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)

