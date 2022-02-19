import streamlit as st
from PIL import Image
import os
import base64

#reads image data
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

#
@st.cache(allow_output_mutation=True)
def get_img_with_href(local_img_path, target_url, width, height):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}">
            <img src="data:image/{img_format};base64,{bin_str}" width="{width}" height="{height}"/>
        </a>
        '''
    return html_code

##########################################
# Title
##########################################
col1, col2 = st.columns([3,1])
with col1:
    st.markdown("<br/><span style='font-weight:bold;font-size:30pt;'>Muhammad Hammad Hassan</span>",unsafe_allow_html=True)
    st.markdown("#### <span style='color:gray;font-style:italic;'>Python & Java Developer</span>",unsafe_allow_html=True)
with col2:
    profile = Image.open('./img/st_round_profile.png')
    st.image(profile)
st.write("---")

##########################################
# About me + dev card
##########################################
col1, col2 = st.columns([3,1])
with col1:
    st.markdown("## About Me")
    about_me = open("text.txt", encoding="utf-8")
    st.markdown(about_me.read())
with col2:
    st.markdown("<span style='text-align:center; font-size:18pt; color:gray;'><b>Personal Info</b></span>",
               unsafe_allow_html=True)
    st.markdown(
        '<a href="https://app.daily.dev/blankscreenEXE"><img src="https://api.daily.dev/devcards/736b8e5f6ab640779df15513b8c0e2f6.png?r=u7s" width="200" alt="Muhammad Hammad Hassan\'s Dev Card"/></a>',
        unsafe_allow_html=True)
    st.caption("My Dev Card from [Daily.dev](https://daily.dev/)")
    st.write("---")

##########################################
# Title
##########################################
col1, col2, col3, col4 = st.columns([10, 1,1,1])
with col1:
    st.markdown("## Education")
    education = open("text.txt", encoding="utf-8")
    st.markdown(education.read())
with col2:
    linkedin_icon = st.markdown(get_img_with_href("./img/linkedin_icon.png", "https://www.linkedin.com/in/muhammad-hammad-hassan-cs101/", "30pt", "30pt"),unsafe_allow_html=True)
with col3:
    linkedin_icon = st.markdown(get_img_with_href("./img/linkedin_icon.png", "https://www.linkedin.com/in/muhammad-hammad-hassan-cs101/", "30pt", "30pt"),unsafe_allow_html=True)
with col4:
    linkedin_icon = st.markdown(get_img_with_href("./img/linkedin_icon.png", "https://www.linkedin.com/in/muhammad-hammad-hassan-cs101/", "30pt", "30pt"),unsafe_allow_html=True)

with col2:
    linkedin_icon = st.markdown(get_img_with_href("./img/linkedin_icon.png", "https://www.linkedin.com/in/muhammad-hammad-hassan-cs101/", "30pt", "30pt"),unsafe_allow_html=True)
with col3:
    linkedin_icon = st.markdown(get_img_with_href("./img/linkedin_icon.png", "https://www.linkedin.com/in/muhammad-hammad-hassan-cs101/", "30pt", "30pt"),unsafe_allow_html=True)
with col4:
    linkedin_icon = st.markdown(get_img_with_href("./img/linkedin_icon.png", "https://www.linkedin.com/in/muhammad-hammad-hassan-cs101/", "30pt", "30pt"),unsafe_allow_html=True)

with col2:
    linkedin_icon = st.markdown(get_img_with_href("./img/linkedin_icon.png", "https://www.linkedin.com/in/muhammad-hammad-hassan-cs101/", "30pt", "30pt"),unsafe_allow_html=True)
with col3:
    linkedin_icon = st.markdown(get_img_with_href("./img/linkedin_icon.png", "https://www.linkedin.com/in/muhammad-hammad-hassan-cs101/", "30pt", "30pt"),unsafe_allow_html=True)
with col4:
    linkedin_icon = st.markdown(get_img_with_href("./img/linkedin_icon.png", "https://www.linkedin.com/in/muhammad-hammad-hassan-cs101/", "30pt", "30pt"),unsafe_allow_html=True)


# personal_info_table = open("personal_info_table.html",encoding="utf-8")
# st.markdown(personal_info_table.read(), unsafe_allow_html=True)
