import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
st.title("QRコード読みとり")
FRAME_WINDOW = st.image([])
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
# class VideoProcessor:
#     def recv(self, frame):
#         img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         data = detector.detectAndDecode(frame)
#         if data[0] != "":
#             st.write(data[0])
# webrtc_streamer(key="example", video_processor_factory=VideoProcessor)
while True:
    ret, frame = cap.read()
    data = detector.detectAndDecode(frame)
    if data[0] != "":
        st.write(data[0])
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # FRAME_WINDOW.image(frame)