import streamlit as st

# Sample data for courses
courses = [
    {
        "title": "Course 1",
        "description": "Introduction to Streamlit",
        "video_url": "https://www.youtube.com/embed/your_video_id1",
        "chapters": ["Getting Started", "Basic Components", "Advanced Features"],
    },
    {
        "title": "Course 2",
        "description": "Data Visualization with Matplotlib",
        "video_url": "https://www.youtube.com/embed/your_video_id2",
        "chapters": ["Introduction", "Plotting Techniques", "Customization"],
    },
    # Add more courses as needed
]

# Quiz data
quiz_data = {
    "Course 1": [
        {"question": "What is Streamlit?", "options": ["A", "B", "C", "D"], "answer": "A"},
        {"question": "Which component allows user input?", "options": ["A", "B", "C", "D"], "answer": "B"},
    ],
    "Course 2": [
        {"question": "What library is used for data visualization?", "options": ["A", "B", "C", "D"], "answer": "C"},
        {"question": "How to customize a plot in Matplotlib?", "options": ["A", "B", "C", "D"], "answer": "D"},
    ],
    # Add more quiz questions as needed
}

# Function to display course details
def display_course(course):
    st.subheader(course["title"])
    st.write(course["description"])
    st.video(course["video_url"])

# Function to display quiz for a course
def display_quiz(course_title):
    st.sidebar.title(f"Quiz - {course_title}")
    questions = quiz_data.get(course_title, [])
    for i, question_data in enumerate(questions):
        st.sidebar.subheader(f"Question {i + 1}")
        st.sidebar.write(question_data["question"])
        user_answer = st.sidebar.radio("Options", question_data["options"])
        st.sidebar.write(f"Your answer: {user_answer}")
        st.sidebar.write(f"Correct answer: {question_data['answer']}")
        st.sidebar.write("---")

# Function to dynamically add a new course
def add_new_course():
    with st.form("new_course_form"):
        st.write("## Add New Course")
        new_course_title = st.text_input("Enter the new course title:")
        new_course_description = st.text_area("Enter the new course description:")
        new_course_video_url = st.text_input("Enter the new course video URL:")
        new_course_chapters = st.text_area("Enter the new course chapters (comma-separated):")
        submitted = st.form_submit_button("Add Course")

    if submitted:
        if new_course_title and new_course_description and new_course_video_url and new_course_chapters:
            new_course = {
                "title": new_course_title,
                "description": new_course_description,
                "video_url": new_course_video_url,
                "chapters": [chap.strip() for chap in new_course_chapters.split(",")],
            }
            courses.append(new_course)
            st.success("New course added successfully!")

# Streamlit app
def main():
    st.set_page_config(
        page_title="Interactive Course Viewer",
        page_icon=":books:",
        layout="wide",
    )

    # Navigation sidebar
    page = st.sidebar.radio("Navigation", ["Home", "Add New Course"])

    if page == "Home":
        st.title("Explore Courses and Take a Quiz")

        # Sidebar for course selection
        selected_course_index = st.sidebar.selectbox(
            "Select a course", range(len(courses))
        )

        # Display selected course details
        selected_course = courses[selected_course_index]
        display_course(selected_course)

        # Display chapters
        st.sidebar.title("Chapters")
        st.sidebar.write(selected_course["chapters"])

        # Display quiz for the selected course
        display_quiz(selected_course["title"])

    elif page == "Add New Course":
        st.title("Add a New Course")
        add_new_course()

if __name__ == "__main__":
    main()
