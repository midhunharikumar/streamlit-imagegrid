import streamlit as st

from streamlit_imagegrid import streamlit_imagegrid

st.set_page_config(layout='wide')

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`


# Create a second instance of our component whose `name` arg will vary
# based on a text_input widget.
#
# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.
urls = [{"src":'https://t3.ftcdn.net/jpg/08/27/75/34/240_F_827753427_Sr2wCt8kJIWzJBWSsigkpsL7vO2CJCN5.jpg',"tag":"A woman"},
        'https://t3.ftcdn.net/jpg/08/62/65/26/240_F_862652654_DpYBIzsWxhBZmjyd3ogyc2nCRFFIjKNW.jpg',
        'https://t3.ftcdn.net/jpg/08/77/80/16/240_F_877801667_6NmA5PNf4sqkzNN8rR56J33yEXPEKL3u.jpg',
        'https://t3.ftcdn.net/jpg/08/20/10/90/240_F_820109020_OIUI5MRWMh3aORvO3bkzEpYIQXwkbyyq.jpg',
        'https://v.ftcdn.net/01/44/56/29/700_F_144562936_5XthDbYbGehoWbTcUb8Q8pN8F6EImebi_ST.mp4']


name_input = st.text_input("Enter a name", value="Streamlit")
zoom  = st.slider("Zoom", 1, 10, 3)
col1, col2 = st.columns(2)
urls = urls
num_clicks = streamlit_imagegrid(name_input,urls=urls, zoom=zoom,key="foo")


