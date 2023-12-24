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
        },
        {
            "title": "Variables and Data Types",
            "video_url": "https://www.youtube.com/embed/your_variables_video",
            "content": "This chapter delves into variables and data types in Python. Learn how to declare variables, work with strings, numbers, and boolean values. Understanding variables and data types is fundamental to writing effective Python code.",
        },
        {
            "title": "Control Flow and Loops",
            "video_url": "https://www.youtube.com/embed/your_control_flow_video",
            "content": "Explore control flow statements such as if, elif, and else in Python. Additionally, learn how to use loops like for and while to control the flow of your Python programs. Mastering control flow is crucial for creating dynamic and efficient programs.",
        },
        {
            "title": "Functions and Modules",
            "video_url": "https://www.youtube.com/embed/your_functions_video",
            "content": "Dive into the world of functions and modules in Python. Understand how to define functions, pass arguments, and organize your code into reusable modules. Well-structured functions and modules are essential for writing maintainable and scalable Python applications.",
        },
        {
            "title": "File Handling",
            "video_url": "https://www.youtube.com/embed/your_file_handling_video",
            "content": "Learn how to read from and write to files in Python. Understand file modes, and explore techniques for efficient file handling in your programs. File handling is a crucial skill for working with external data and storing information persistently.",
        },
        {
            "title": "Exception Handling",
            "video_url": "https://www.youtube.com/embed/your_exception_handling_video",
            "content": "Explore exception handling in Python. Learn how to handle errors gracefully using try, except, and finally blocks. Understand common exceptions and implement strategies for effective error management in your Python code.",
        },
        {
            "title": "Object-Oriented Programming",
            "video_url": "https://www.youtube.com/embed/your_oop_video",
            "content": "Get introduced to the principles of object-oriented programming (OOP) in Python. Understand classes, objects, inheritance, and encapsulation. OOP is a paradigm that enhances code organization and promotes code reuse and maintainability.",
        },
        {
            "title": "Advanced Topics I",
            "video_url": "https://www.youtube.com/embed/your_advanced_topics_video",
            "content": "Dive into advanced Python topics, including decorators, generators, and context managers. Explore powerful features that make Python a versatile language. Understanding advanced topics will elevate your Python programming skills to the next level.",
        },
        {
            "title": "Advanced Topics II",
            "video_url": "https://www.youtube.com/embed/your_advanced_topics_ii_video",
            "content": "Continue exploring advanced Python concepts such as metaclasses, threading, and multiprocessing. Gain a deeper understanding of Python's capabilities and apply them to solve complex problems. Advanced Topics II will expand your Python knowledge even further.",
        },
        {
            "title": "Final Project",
            "video_url": "https://www.youtube.com/embed/your_final_project_video",
            "content": "Cap off the course by working on a final project. Apply your knowledge to solve a real-world problem and showcase your Python programming skills. The final project is an opportunity to integrate everything you've learned in this masterclass into a comprehensive and meaningful application.",
        },
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
    st.subheader(course["title"])
    st.write(course["description"])
    st.video(course["video_url"])

# Function to display chapter details
def display_chapter(chapter):
    st.subheader(chapter["title"])
    st.video(chapter["video_url"])
    st.write(chapter["content"])

# Function to display quiz for a course
def display_quiz(course_title):
    st.sidebar.title(f"Quiz - {course_title}")
    questions = quiz_data_python_course.get(course_title, [])
    for i, question_data in enumerate(questions):
        st.sidebar.subheader(f"Question {i + 1}")
        user_answer = st.sidebar.radio(f"Options_{i}", question_data["options"])
        st.sidebar.write(f"Your answer: {user_answer}")
        st.sidebar.write(f"Correct answer: {question_data['answer']}")
        st.sidebar.write("---")

# Streamlit app
def main():
    st.set_page_config(
        page_title="Python Masterclass Viewer",
        page_icon=":snake:",
        layout="wide",
    )

    # Display course details for the Python Programming Masterclass
    display_course(course_data)

    # Display individual chapters
    st.title("Course Chapters")
    for chapter in course_data["chapters"]:
        display_chapter(chapter)
        st.write("---")

    # Display quiz for the selected course
    display_quiz("Introduction to Python")

if __name__ == "__main__":
    main()
