import streamlit as st
import time

# --- Title and Intro ---
st.title('🎓 Student Dashboard')
st.header('Welcome to Student Performance Tracker')
st.subheader('📊 Monitor, Analyze & Interact')

st.text('This app shows how different Streamlit widgets can be used with real data.')

# --- Markdown, Code, LaTeX ---
st.markdown('## Features\n- Interactive inputs\n- Data visualization\n- Real-time updates')
st.code('student_score = (marks_obtained / total_marks) * 100', language='python')
st.latex(r'Percentage = \frac{Marks\ Obtained}{Total\ Marks} \times 100')

# --- Buttons and Checkboxes ---
if st.button('Show Student Status'):
    st.write('✅ Student has passed all subjects!')

if st.checkbox('Show Attendance Record'):
    st.write('📅 Attendance: 92%')

# --- Radio Buttons ---
grade = st.radio('Choose Grade Level:', ['Freshman', 'Sophomore', 'Junior', 'Senior'])
st.write(f'📘 Current Grade: {grade}')

# --- Selectbox ---
subject = st.selectbox('Select Subject:', ['Mathematics', 'Science', 'History'])
st.write(f'📖 Selected subject: {subject}')

# --- Multiselect ---
activities = st.multiselect('Select Extracurricular Activities:', 
                            ['Sports', 'Music', 'Debate Club', 'Coding Club'])
st.write(f'🏆 Activities chosen: {activities}')

# --- Slider ---
marks = st.slider('Marks Obtained (out of 100):', 0, 100, 75)
st.write(f'📈 Marks: {marks}/100')

# --- Text Input ---
student_name = st.text_input('Enter Student Name:', 'John Doe')
st.write(f'👤 Student: {student_name}')

# --- Number Input ---
roll_no = st.number_input('Enter Roll Number:', 1, 100, 23)
st.write(f'🆔 Roll Number: {roll_no}')

# --- Date & Time Inputs ---
dob = st.date_input('Select Date of Birth')
st.write(f'🎂 DOB: {dob}')

study_time = st.time_input('Preferred Study Time')
st.write(f'⏰ Study Time: {study_time}')

# --- File Uploader ---
file = st.file_uploader('Upload Student Report Card')
if file:
    st.write(f'📂 Uploaded File: {file.name}')

# --- Camera Input ---
img = st.camera_input('Take Student Photo')
if img:
    st.image(img, caption="📸 Student Photo")

# --- Color Picker ---
fav_color = st.color_picker('Pick Favorite Color', '#00f900')
st.write(f'🎨 Favorite Color: {fav_color}')

# --- Columns ---
col1, col2 = st.columns(2)
col1.metric(label="GPA", value="3.8", delta="+0.2")
col2.metric(label="Attendance", value="92%", delta="-3%")

# --- Expander ---
with st.expander('📂 See More Details'):
    st.write('Additional academic info, projects, and notes can be stored here.')

# --- Sidebar ---
with st.sidebar:
    st.header("⚙️ Settings")
    st.write('Sidebar filters can be added here.')
    level = st.radio("Difficulty Level", ["Easy", "Medium", "Hard"])
    st.write(f"📌 Selected Level: {level}")

# --- Fun Animations ---
st.balloons()

# --- Spinner & Progress Bar ---
with st.spinner('⏳ Calculating final result...'):
    time.sleep(2)
st.success('✅ Results Ready!')

progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)
st.write('📊 Progress complete')
