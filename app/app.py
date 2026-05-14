import streamlit as st
from openai import OpenAI

# Page Configuration
st.set_page_config(
    page_title="AI Career Guidance Assistant",
    page_icon="🎓",
    layout="wide"
)

# OpenRouter Client
client = OpenAI(
    api_key="YOUR_OPENROUTER_API_KEY",
    base_url="https://openrouter.ai/api/v1"
)

# Title
st.title("🎓 AI Career Guidance Assistant")
st.markdown("### Prompt Engineering Comparison for Career Counseling")

# User Inputs
name = st.text_input("👤 Enter your name")

skills = st.text_area(
    "💻 Enter your skills",
    placeholder="Example: Python, HTML, JavaScript"
)

interest = st.text_input(
    "🚀 Enter your interests",
    placeholder="Example: Artificial Intelligence"
)

goal = st.text_input(
    "🎯 Enter your career goal",
    placeholder="Example: AI Engineer"
)

# Button
if st.button("Generate Career Guidance"):

    # BASIC PROMPT
    basic_prompt = f"""
    Suggest careers for a student with skills in {skills}
    """

    # ADVANCED PROMPT
    advanced_prompt = f"""
    You are an AI-powered expert career counselor.

    Analyze the following student profile carefully and provide professional career guidance.

    Student Details:
    Name: {name}
    Skills: {skills}
    Interests: {interest}
    Career Goal: {goal}

    Provide the response in the following structured format:

    1. Best Career Options
    - Suggest top 3 suitable careers
    - Explain why each career matches the student profile

    2. Skill Gap Analysis
    - Mention missing skills the student should learn

    3. Learning Roadmap
    - Step-by-step roadmap for becoming successful

    4. Recommended Certifications
    - Suggest useful certifications

    5. Industry Trends
    - Explain future demand

    6. Salary Insights
    - Mention beginner salary ranges

    7. Personalized Career Advice
    """

    with st.spinner("Generating AI Responses..."):

        # Basic Prompt Response
        basic_response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": basic_prompt}
            ]
        )

        basic_result = basic_response.choices[0].message.content

        # Advanced Prompt Response
        advanced_response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": advanced_prompt}
            ]
        )

        advanced_result = advanced_response.choices[0].message.content

    # Display Results Side by Side
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚠️ Basic Prompt Output")
        st.write(basic_result)

    with col2:
        st.subheader("✅ Engineered Prompt Output")
        st.write(advanced_result)

st.header("📄 Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume (TXT File)",
    type=["txt"]
)

if uploaded_file is not None:

    resume_text = uploaded_file.read().decode("utf-8")

    st.subheader("📑 Resume Content")
    st.text(resume_text)

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            resume_prompt = f"""
            You are an expert ATS resume analyzer and career counselor.

            Analyze the following resume and provide:

            1. Resume Strength
            2. Missing Skills
            3. ATS Improvement Suggestions
            4. Career Recommendations
            5. Project Improvement Suggestions
            6. Technical Skills Enhancement Tips

            Resume:
            {resume_text}

            Make the response professional and detailed.
            """

            resume_response = client.chat.completions.create(
                model="openai/gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": resume_prompt}
                ]
            )

            resume_result = resume_response.choices[0].message.content

        st.subheader("📌 Resume Analysis Result")
        st.write(resume_result)

st.header("💬 AI Career Chatbot")

user_question = st.text_input(
    "Ask your career-related question"
)

if st.button("Get Answer"):

    chatbot_prompt = f"""
    You are an intelligent AI career counselor.

    Answer the following career-related question professionally and clearly.

    Question:
    {user_question}

    Provide:
    - Clear explanation
    - Career guidance
    - Required skills
    - Learning suggestions
    - Career opportunities
    """

    with st.spinner("Generating Answer..."):

        chatbot_response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": chatbot_prompt}
            ]
        )

        chatbot_result = chatbot_response.choices[0].message.content

    st.subheader("📌 Chatbot Response")
    st.write(chatbot_result)
