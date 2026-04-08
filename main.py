import streamlit as st

st.set_page_config(layout="wide")

st.title('Streamlit App')

home_page = st.Page(
    page='views/home.py',
    title='Home',
    icon=':material/home:',
)

profile_page = st.Page(
    page='views/profile.py',
    title='Profile',
    icon=':material/person:',
    default=True
)

contact_page = st.Page(
    page='views/contact.py',
    title='Contact Us',
    icon=':material/contact_page:',
)

nb = st.navigation(
    {
        'info':[home_page, profile_page],
        'Useful Link':[contact_page]
    }
)

st.logo('4712293.png', size='large')
st.sidebar.text("Powered by Divyansh")
nb.run()