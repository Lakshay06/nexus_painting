import streamlit as st
import base64

# Helper to add full-screen background image
def add_hero_bg(image_path):
    with open(image_path, "rb") as img_file:
        img_data = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .hero {{
            background-image: url("data:image/png;base64,{img_data}");
            height: 100vh;
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: #202A44;
            padding-left: 5%;
        }}
        .hero h1 {{
            font-size: 4em;
            margin-bottom: 0.2em;
        }}
        .hero p {{
            font-size: 1.5em;
            line-height: 1.5em;
        }}
        .hero .btn {{
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #d72638;
            color: white;
            border: none;
            border-radius: 20px;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
            width: fit-content;
        }}
        </style>
        <div class="hero">
            <h1>NEXUS PAINTING</h1>
            <p>Exterior.<br>Interior.<br>Professional.</p>
            <a href="#contact" class="btn">Get in Touch</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Set page config
st.set_page_config(layout="wide")
add_hero_bg("images/bg_header.jpeg")


# Services Section
st.markdown("## Our Services")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("images/interior.png", use_column_width=True)
    st.markdown("<h4 style='text-align: center; color: #d72638;'>Interior</h4>", unsafe_allow_html=True)
with col2:
    st.image("images/exterior.png", use_column_width=True)
    st.markdown("<h4 style='text-align: center; color: #d72638;'>Exterior</h4>", unsafe_allow_html=True)
with col3:
    st.image("images/commercial.png", use_column_width=True)
    st.markdown("<h4 style='text-align: center; color: #d72638;'>Commercial</h4>", unsafe_allow_html=True)





# Testimonial Section
st.markdown("## What Our Clients Say")
with st.container():
    test_cols = st.columns(3)
    reviews = [
        ("Sarah L.", 5, "Nexus Painting did a fantastic job on our home. Professional, quick, and very neat!"),
        ("James M.", 5, "The team was reliable and easy to communicate with. Highly recommend!"),
        ("Priya D.", 4, "Great color consultation and interior work. Would definitely hire again.")
    ]
    for col, (name, stars, review) in zip(test_cols, reviews):
        with col:
            st.markdown(f"**{name}**")
            st.markdown("⭐" * stars)
            st.markdown(f"*\"{review}\"*")

# Text Before Color Consultation Image
st.markdown(
    "<h2 style='text-align: center; margin-top: 60px;'>Need Help Choosing the Perfect Color?</h2>",
    unsafe_allow_html=True
)

# Color Consultation Image
st.image("images/color_consultation.png", use_column_width=True)

# Project Gallery
st.markdown("## Project Gallery")
project_cols = st.columns(3)
project_imgs = ["images/project1.png", "images/project2.png", "images/project3.png"]
for col, img in zip(project_cols, project_imgs):
    col.image(img, use_column_width=True)

# Contact Form
st.markdown("## Contact Us")
with st.form("contact_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name")
        email = st.text_input("Email")
    with col2:
        phone = st.text_input("Phone Number")
        service = st.selectbox("Service Type", ["Interior", "Exterior", "Commercial", "Color Consultation"])
    message = st.text_area("Message")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success("Thank you! We'll be in touch shortly.")

# Footer
st.markdown("""
    <footer style='background-color: #202A44; padding: 40px; margin-top: 50px; text-align: center; color: white;'>
        <h3 style='color: white;'>NEXUS PAINTING</h3>
        <p>Email: contact@nexuspainting.com | Phone: (123) 456-7890</p>
        <p>123 Paint Street, Kelowna, BC</p>
    </footer>
""", unsafe_allow_html=True)
