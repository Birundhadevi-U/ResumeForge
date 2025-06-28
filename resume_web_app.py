import streamlit as st
from PIL import Image
from resume_generator import generate_resume
from datetime import datetime
import csv

st.set_page_config(page_title="ResumeForge – AI Resume Builder", layout="centered")

st.title("📝 ResumeForge")
st.markdown("Build your professional resume using AI-powered tools ✨")

# Sidebar Photo
st.sidebar.title("👤 Upload Profile Photo")
photo = st.sidebar.file_uploader("Upload your photo", type=["jpg", "png", "jpeg"])
if photo:
    st.sidebar.image(Image.open(photo), width=150)

# User Inputs
st.subheader("📇 Contact Information")
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
linkedin = st.text_input("LinkedIn URL")
github = st.text_input("GitHub URL")

st.subheader("👤 Profile Summary")
summary = st.text_area("Write a brief personal summary")

st.subheader("🎓 Education")
education = st.text_area("Add your education details")

st.subheader("💼 Work Experience")
experience = st.text_area("Describe your work experience")

st.subheader("🛠 Skills")
skills = st.text_input("List your skills (comma-separated)")

st.subheader("📜 Certifications")
certifications = st.text_area("List your certifications")

st.subheader("🌟 Projects")
projects = st.text_area("List your major projects")

st.subheader("🏆 Achievements")
achievements = st.text_area("Mention any awards or achievements")

st.subheader("💬 Languages Known")
languages = st.text_input("Languages you know (comma-separated)")

# Resume Download Section
st.markdown("---")
st.subheader("📥 Download Resume")

if st.button("Generate & Download Resume"):
    resume = generate_resume(
        name, email, phone, linkedin, github,
        education, experience, skills,
        "",  # career_objective (optional for now)
        photo, summary, certifications, projects,
        achievements, languages
    )
    st.download_button(
        label="Download Resume (Word)",
        data=resume,
        file_name="ResumeForge_Resume.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    # Log analytics
    with open("analytics.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), name, email, phone])

# Feedback Section
st.markdown("---")
st.subheader("💬 Feedback")
feedback = st.text_area("Tell us how we can improve ResumeForge")

if st.button("Submit Feedback"):
    with open("feedback.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), name, email, feedback])
    st.success("✅ Thank you for your feedback!")