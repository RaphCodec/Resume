import streamlit as st


def main():
    # Set page title and configuration
    st.set_page_config(page_title="Resume Dashboard", layout="wide", page_icon=":bar_chart:", initial_sidebar_state="expanded")

    # Header section
    st.title("Raphael Clifton - Resume Dashboard")

    # st.write("📧 email@example.com | 📱 (123) 456-7890 | 📍 New York City, New York")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Experience", value="3 years", border=True)
        st.metric(label="Current Role", value="Data Engineer")
    with col2:
        st.metric(label="Current Role", value="Data Engineer", border=True)
    with col3:
        st.metric(label="Portfolio", value="placeholder", border=True)

    # Professional Summary
    st.header("About Me")
    st.write(
        "Experienced Data Engineer with expertise in Python, web development, and cloud technologies."
    )


if __name__ == "__main__":
    main()
