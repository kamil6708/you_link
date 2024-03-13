import streamlit as st
from pytube import YouTube
import os
from io import BytesIO
import base64

def sanitize_filename(filename):
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def download_video(link):
    try:
        yt = YouTube(link)
        st.write("Title:", yt.title)
        st.write("Views:", yt.views)

        yd = yt.streams.get_highest_resolution()
        sanitized_title = sanitize_filename("telechargement_youtube")
        download_path = os.path.join(os.getcwd(), sanitized_title + ".mp4")

        # Create a BytesIO object
        buffer = BytesIO()
        # Download link for manual download
        yd.stream_to_buffer(buffer)
        video_buffer = buffer.getvalue()
       
        video_base64 = base64.b64encode(video_buffer).decode()
        download_link = f'<a href="data:video/mp4;base64,{video_base64}" download="{download_path}">Click here to download</a>'
        
        st.markdown("To download the video manually, right-click the link below and choose 'Save link as':", unsafe_allow_html=True)
        st.markdown(download_link, unsafe_allow_html=True)

        # Progress bar
        progress_bar = st.progress(0)
        for i in range(100):
            # Update the progress bar with each iteration.
            progress_bar.progress(i + 1)
    
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("Téléchargeur de vidéos YouTube")

    # Input for the YouTube video URL
    link = st.text_input("Veuillez entrer l’URL de la vidéo YouTube:")

    if st.button("Download"):
        if link:
            download_video(link)
        else:
            st.warning("Veuillez entrer l’URL de la vidéo YouTube valdie.")

    # Copyright notice
    st.markdown("<p style='text-align: center; color: #888888;'>© Kamil Mohamed Kamil.Tous droits réservés.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
