
import cv2
import streamlit as st

st.title("QRコード読みとり")
option = st.selectbox(
     '入室　退室',
     ('入室', '退室'))
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
inroom = set()
outroom = set()
while option == "入室": 
    _, frame = camera.read()
    data = detector.detectAndDecode(frame)
    if data[0] != "":
        inroom.add(data[0])
        st.write(data[0])
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
while option == "退室": 
    _, frame = camera.read()
    data = detector.detectAndDecode(frame)
    if data[0] != "":
        outroom.add(data[0])
        st.write(data[0])
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
