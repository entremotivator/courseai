import streamlit as st

# Sample data for courses
courses = [
    {
        "title": "Course 1",
        "description": "Introduction to Streamlit",
        "video_url": "https://www.youtube.com/embed/your_video_id1",
    },
    {
        "title": "Course 2",
        "description": "Data Visualization with Matplotlib",
        "video_url": "https://www.youtube.com/embed/your_video_id2",
    },
    # Add more courses as needed
]

# Function to display course details
def display_course(course):
    st.subheader(course["title"])
    st.write(course["description"])
    st.video(course["video_url"])

# Streamlit app
def main():
    st.title("Course Viewer App")

    # Sidebar for course selection
    selected_course_index = st.sidebar.selectbox(
        "Select a course", range(len(courses))
    )

    # Display selected course details
    display_course(courses[selected_course_index])

    # List all courses
    st.sidebar.title("Course List")
    for i, course in enumerate(courses):
        st.sidebar.write(f"{i+1}. {course['title']}")

if __name__ == "__main__":
    main()
