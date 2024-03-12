import streamlit as st
from pytube import YouTube
import os

def sanitize_filename(filename):
    # Replace invalid characters with underscores
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
        download_path = os.path.join(os.getcwd(), sanitized_title)
        st.write("Downloading...")
        yd.download(download_path)
        st.write("Download complete! Video saved at:", download_path)
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("Téléchargement video YouTube ")

    # Input for the YouTube video URLS
    link = st.text_input(" Veuillez mettre le lien URL de la video Youtube: ")

    if st.button("Download"):
        if link:
            download_video(link)
        else:
            st.warning("Veuillez mettre un lien youtube valide.")

    # Copyright notice
    st.markdown("<p style='text-align: center; color: #888888;'>© Kamil Mohamed Kamil. Tous droits réservés.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
