import html
import requests, streamlit as st
from config import KEYWORD, DEFAULT_IMAGE, NEWS_API_KEY as API_KEY
from streamlit.runtime.media_file_storage import MediaFileStorageError

def _get_news(): 
    return requests.get(f'https://newsapi.org/v2/everything?q={KEYWORD}&apiKey={API_KEY}&language=en&searchIn=title').json()['articles']

def news_page():
    for random_news in list(_get_news()):
        st.write(f"""<h2>{html.unescape(random_news['title'])}</h2><br>""", unsafe_allow_html=True)
        try:
            if random_news["urlToImage"]:
                st.image(f'{random_news["urlToImage"]}')
        except MediaFileStorageError:
            st.image(DEFAULT_IMAGE)
        st.write(f"""
            <h5>{random_news['description']}</h5>
            Link : <a href="{random_news['url']}">{random_news['url'][:80]}...</a><br>
            Author : {random_news['author']}, &nbsp; <i>{random_news['publishedAt'][:10]}</i>
            <hr>
            """, unsafe_allow_html=True)
        