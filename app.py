import streamlit as st
import hashlib
import random

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

# Simulated database for user accounts
user_database = {
    "john_doe": {"password": hashlib.sha256("password123".encode()).hexdigest(), "enrolled_courses": []},
    "jane_smith": {"password": hashlib.sha256("securepass".encode()).hexdigest(), "enrolled_courses": []},
    # Add more users and hashed passwords
}

# Function to generate a random username
def generate_random_username():
    adjectives = ["Happy", "Smart", "Creative", "Adventurous", "Friendly"]
    nouns = ["Coder", "Explorer", "Dreamer", "Enthusiast", "Champion"]
    return f"{random.choice(adjectives)}_{random.choice(nouns)}"

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
    st.sidebar.subheader("User Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if username in user_database and hashed_password == user_database[username]["password"]:
            st.sidebar.success(f"Welcome, {username}!")
            return username
        else:
            st.sidebar.error("Invalid username or password. Please try again.")

    st.sidebar.subheader("Don't have an account?")
    if st.sidebar.button("Register"):
        new_user = generate_random_username()
        new_password = "securepassword"  # Simulated registration with a default password
        hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
        user_database[new_user] = {"password": hashed_new_password, "enrolled_courses": []}
        st.sidebar.success(f"Account created for {new_user}. You can now log in.")
    
    return None

# Function to simulate secure login
def secure_login_simulation():
    st.sidebar.subheader("Secure User Login")
    secure_user = st.sidebar.text_input("Username")
    secure_password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if secure_user in user_database and user_database[secure_user]["password"] == hashlib.sha256(secure_password.encode()).hexdigest():
            st.sidebar.success(f"Secure login successful. Welcome, {secure_user}!")
            return secure_user
        else:
            st.sidebar.error("Invalid username or password. Please try again.")
    
    return None

# Function to simulate user enrollment in a course
def enroll_user():
    st.sidebar.subheader("Enroll in a Course")
    available_courses = [course["title"] for course in course_data["chapters"]]
    selected_course = st.sidebar.selectbox("Select a course", available_courses)

    if st.sidebar.button("Enroll"):
        # In a real app, this would update the user's data in the database
        st.sidebar.success(f"You are now enrolled in the course: {selected_course}.")
        user_database[user]["enrolled_courses"].append(selected_course)

# Function to add a new course
def add_new_course():
    st.sidebar.subheader("Add New Course")
    new_course_title = st.sidebar.text_input("Course Title")
    new_course_description = st.sidebar.text_area("Course Description")
    new_course_video_url = st.sidebar.text_input("Course Video URL")
    new_course_chapters = st.sidebar.slider("Number of Chapters", 1, 20, 5)

    new_course_data = {
        "title": new_course_title,
        "description": new_course_description,
        "video_url": new_course_video_url,
        "chapters": [],
    }

    for i in range(new_course_chapters):
        chapter_title = f"Chapter {i + 1} - {new_course_title}"
        chapter_video_url = f"https://www.youtube.com/embed/chapter_{i + 1}_video"
        chapter_content = f"This is the content for Chapter {i + 1} of the course {new_course_title}."
        new_course_data["chapters"].append({
            "title": chapter_title,
            "video_url": chapter_video_url,
            "content": chapter_content,
            "resources": [],
        })

    # Display the new course data (for demonstration purposes)
    st.sidebar.subheader("New Course Preview")
    st.sidebar.write(new_course_data)

    if st.sidebar.button("Add Course"):
        # In a real app, this would update the courses data
        st.sidebar.success(f"New course added: {new_course_title}")

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
    selected_option = st.sidebar.radio("Select an option", ["Home", "Take Quiz", "Secure Login", "Enroll", "Add Course"])

    # Handle selected options
    if selected_option == "Home":
        st.title("Course Chapters")
        for chapter in course_data["chapters"]:
            display_chapter(chapter, user_progress.get(chapter["title"]), user)

    elif selected_option == "Take Quiz":
        selected_chapter = st.sidebar.selectbox("Select a chapter for the quiz", course_data["chapters"])
        user_answers = user_quiz_answers.get(selected_chapter, {})
        user_quiz_answers = display_quiz(selected_chapter, quiz_data_python_course, user_answers)

    elif selected_option == "Secure Login":
        secure_user = secure_login_simulation()
        st.success(f"Secure login successful. Welcome, {secure_user}!")

    elif selected_option == "Enroll":
        enroll_user()

    elif selected_option == "Add Course":
        add_new_course()

if __name__ == "__main__":
    main()
