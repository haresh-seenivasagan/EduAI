import streamlit as st
from IPython.display import Image
from pytube import YouTube
from youtube_search import YoutubeSearch
st.title('Video Recommendation Engine')
# Get user input for the search term
search_term = st.text_input("Enter the search term:")

# Search for the most viewed videos on YouTube
results = YoutubeSearch(search_term, max_results=10).to_dict()

# Iterate through the results and display the title, URL, and thumbnail of each video
for result in results:
    # Get the video ID
    video_id = result['id']

    # Get the video title
    video_title = result['title']

    # Construct the video URL
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    # Get the video thumbnail URL
    thumbnail_url = f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg"

    # Display the video title, URL, and thumbnail image
    st.write(f"Title: {video_title}")
    st.write(f"URL: {video_url}")
    st.image(thumbnail_url)
