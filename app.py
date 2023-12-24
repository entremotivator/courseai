import streamlit as st

# Sample data for a single course with 10 chapters
course_data = {
    "title": "Python Programming Masterclass",
    "description": "Welcome to the Python Programming Masterclass! This comprehensive course will take you from a beginner to an advanced Python programmer.",
    "video_url": "https://www.youtube.com/embed/your_video_id_python_course",
    "chapters": [
        {
            "title": "Introduction to Python",
            "video_url": "https://www.youtube.com/embed/your_intro_video",
            "content": "In this introductory chapter, you'll get an overview of the Python programming language. We'll cover the basics of Python syntax and set up your development environment. By the end of this chapter, you'll be ready to write your first Python script.",
            "resources": [
                {"title": "Python Official Documentation", "link": "https://docs.python.org/3/"},
                {"title": "Codecademy Python Course", "link": "https://www.codecademy.com/learn/learn-python-3"},
            ],
        },
        {
            "title": "Variables and Data Types",
            "video_url": "https://www.youtube.com/embed/your_variables_video",
            "content": "This chapter delves into variables and data types in Python. Learn how to declare variables, work with strings, numbers, and boolean values. Understanding variables and data types is fundamental to writing effective Python code.",
            "resources": [
                {"title": "W3Schools Python Variables", "link": "https://www.w3schools.com/python/python_variables.asp"},
                {"title": "Real Python - Python Data Types", "link": "https://realpython.com/python-data-types/"},
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
    "Variables and Data Types": [
        {"question": "What is a variable?", "options": ["A", "B", "C", "D"], "answer": "A"},
        {"question": "How to define a string variable?", "options": ["A", "B", "C", "D"], "answer": "C"},
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
def display_chapter(chapter):
    st.title(chapter["title"])
    st.subheader("Chapter Video")
    st.video(chapter["video_url"])
    st.subheader("Chapter Content")
    st.write(chapter["content"])

    # Additional Resources
    if "resources" in chapter and chapter["resources"]:
        st.subheader("Additional Resources")
        for resource in chapter["resources"]:
            st.write(f"- [{resource['title']}]({resource['link']})")

    st.write("---")

# Function to display quiz for a course
def display_quiz(course_title, quiz_data):
    st.title(f"Quiz - {course_title}")
    questions = quiz_data.get(course_title, [])
    for i, question_data in enumerate(questions):
        st.subheader(f"Question {i + 1}")
        user_answer = st.radio(f"Options_{i}", question_data["options"])
        st.write(f"Your answer: {user_answer}")
        st.write(f"Correct answer: {question_data['answer']}")
        st.write("---")

# Function to edit course information
def edit_course_info(course):
    st.subheader("Edit Course Information")
    new_title = st.text_input("New Title", course["title"])
    new_description = st.text_area("New Description", course["description"])
    new_video_url = st.text_input("New Video URL", course["video_url"])

    if st.button("Update Course Info"):
        course["title"] = new_title
        course["description"] = new_description
        course["video_url"] = new_video_url
        st.success("Course information updated successfully!")

# Function to add a new chapter
def add_new_chapter(course):
    st.subheader("Add New Chapter")
    new_chapter_title = st.text_input("Chapter Title")
    new_chapter_video_url = st.text_input("Chapter Video URL")
    new_chapter_content = st.text_area("Chapter Content")

    if st.button("Add Chapter"):
        new_chapter = {
            "title": new_chapter_title,
            "video_url": new_chapter_video_url,
            "content": new_chapter_content,
            "resources": [],  # Add resources as needed
        }
        course["chapters"].append(new_chapter)
        st.success("New chapter added successfully!")

# Streamlit app
def main():
    st.set_page_config(
        page_title="Python Masterclass Viewer",
        page_icon=":snake:",
        layout="wide",
    )

    # Display course details for the Python Programming Masterclass
    display_course(course_data)

    # Sidebar for interactive options
    st.sidebar.title("Interactive Options")
    selected_option = st.sidebar.radio("Select an option", ["Home", "Edit Course Info", "Add New Chapter"])

    # Handle selected options
    if selected_option == "Home":
        st.title("Course Chapters")
        for chapter in course_data["chapters"]:
            display_chapter(chapter)

        # Display quiz for the selected course
        display_quiz("Introduction to Python", quiz_data_python_course)

    elif selected_option == "Edit Course Info":
        edit_course_info(course_data)

    elif selected_option == "Add New Chapter":
        add_new_chapter(course_data)

if __name__ == "__main__":
    main()
