import streamlit as st
import pandas as pd
from faker import Faker
from hashlib import sha256

# Sample data for a single course with 10 chapters
course_data = {
    "title": "Python Programming Masterclass",
    "description": "Welcome to the Python Programming Masterclass! This comprehensive course will take you from a beginner to an advanced Python programmer.",
    "video_url": "https://www.youtube.com/embed/your_video_id_python_course",
    "chapters": [
        {
            "title": "Introduction to Python",
            "video_url": "https://www.youtube.com/embed/your_intro_video",
            "content": """In this introductory chapter, you'll get an overview of the Python programming language. We'll cover the basics of Python syntax and set up your development environment. By the end of this chapter, you'll be ready to write your first Python script.

                **Topics Covered:**
                - Python history and philosophy
                - Setting up Python environment
                - Basic syntax and printing
                - Your first Python script
            """,
            "resources": [
                {"title": "Python Official Documentation", "link": "https://docs.python.org/3/"},
                {"title": "Codecademy Python Course", "link": "https://www.codecademy.com/learn/learn-python-3"},
            ],
        },
        # ... Repeat the structure for the remaining chapters
    ],
}

# Quiz data for the Python Programming Masterclass course
quiz_data_python_course = {
    "Introduction to Python": [
        {"question": "What is Python?", "options": ["A", "B", "C", "D"], "answer": "A"},
        {"question": "Which command is used to print in Python?", "options": ["A", "B", "C", "D"], "answer": "B"},
    ],
    # Add more quiz questions for each chapter
    # ...
    "Final Project": [
        {"question": "What is the final project about?", "options": ["A", "B", "C", "D"], "answer": "D"},
        {"question": "How to submit the final project?", "options": ["A", "B", "C", "D"], "answer": "B"},
    ],
}

# Function to display course details
def display_course(course):
    st.title(course["title"])
    st.subheader("Course Overview")
    st.write(course["description"])
    st.subheader("Course Video")
    st.video(course["video_url"])
    st.write("---")

# Function to display individual chapter details
def display_chapter(chapter, progress, user):
    st.title(chapter["title"])
    st.subheader("Chapter Video")
    st.video(chapter["video_url"])
    st.subheader("Chapter Content")
    st.markdown(chapter["content"], unsafe_allow_html=True)

    # Additional Resources
    if "resources" in chapter and chapter["resources"]:
        st.subheader("Additional Resources")
        for resource in chapter["resources"]:
            st.write(f"- [{resource['title']}]({resource['link']})")

    st.write("---")

    # User Progress
    if progress is not None:
        st.subheader("Your Progress")
        st.progress(progress)

    # Discussion Forum
    st.subheader("Discussion Forum")
    show_comments(chapter["title"], user)

# Function to display quiz for a course
def display_quiz(course_title, quiz_data, user_answers):
    st.title(f"Quiz - {course_title}")
    questions = quiz_data.get(course_title, [])
    total_questions = len(questions)
    correct_answers = 0

    for i, question_data in enumerate(questions):
        st.subheader(f"Question {i + 1}")
        user_answer = st.radio(f"Options_{i}", question_data["options"])
        st.write(f"Your answer: {user_answer}")
        st.write(f"Correct answer: {question_data['answer']}")
        st.write("---")

        # Update user answers
        if user_answer == question_data["answer"]:
            correct_answers += 1

    # Display quiz results
    st.subheader("Quiz Results")
    st.write(f"You answered {correct_answers} out of {total_questions} questions correctly.")
    st.write("---")

    # Dynamic Quiz Scoring System
    score = (correct_answers / total_questions) * 100
    st.subheader("Your Score")
    st.write(f"Your score for this quiz: {score:.2f}%")
    st.write("---")

    # User Feedback
    if score == 100:
        st.success("Congratulations! You scored 100%. You've mastered this chapter.")
    elif score >= 70:
        st.info("Good job! You've passed the quiz. Keep up the good work.")
    else:
        st.error("Oops! You might want to review the chapter and try the quiz again.")

    # Leaderboard
    st.subheader("Leaderboard")
    leaderboard = {
        "John Doe": 95,
        "Jane Smith": 88,
        "Bob Johnson": 72,
        # Add more users and scores
    }

    st.table(leaderboard)
    st.write("---")

    # Save user quiz answers
    user_answers[course_title] = correct_answers
    return user_answers

# Function to simulate user progress
def get_user_progress():
    # In a real app, this would come from a user account system and database
    return {
        "Introduction to Python": 0.3,
        # ... Progress for other chapters
        "Final Project": 0.0,
    }

# Function to display discussion forum
def show_comments(chapter_title, user):
    comments = st.expander("Comments", expanded=True)
    new_comment = comments.text_input("Add your comment", key=f"{chapter_title}_{user}")
    if new_comment:
        comments.markdown(f"{user}: {new_comment}")

# Function to simulate user registration and login
def login_simulation():
    fake = Faker()
    username = fake.user_name()
    password = fake.password()

    st.sidebar.subheader("User Login")
    st.sidebar.text_input("Username", value=username, key="username", disabled=True)
    st.sidebar.text_input("Password", value=password, key="password", disabled=True)

    return username

# Streamlit app
def main():
    st.set_page_config(
        page_title="Python Masterclass Viewer",
        page_icon=":snake:",
        layout="wide",
    )

    # Simulate user registration and login
    user = login_simulation()

    # Get user data (simulated for demonstration purposes)
    user_progress = get_user_progress()
    user_quiz_answers = {}

    # Display course details for the Python Programming Masterclass
    display_course(course_data)

    # Sidebar for interactive options
    st.sidebar.title("Interactive Options")
    selected_option = st.sidebar.radio("Select an option", ["Home", "Take Quiz"])

    # Handle selected options
    if selected_option == "Home":
        st.title("Course Chapters")
        for chapter in course_data["chapters"]:
            display_chapter(chapter, user_progress.get(chapter["title"]), user)

    elif selected_option == "Take Quiz":
        selected_chapter = st.sidebar.selectbox("Select a chapter for the quiz", course_data["chapters"])
        user_quiz_answers = display_quiz(selected_chapter, quiz_data_python_course, user_quiz_answers)

if __name__ == "__main__":
    main()
