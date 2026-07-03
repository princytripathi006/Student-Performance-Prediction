import streamlit as st
import pandas as pd
import joblib

# ------------------------------
# Load Model
# ------------------------------

model = joblib.load("student_performance_model.pkl")

# ------------------------------
# Page Settings
# ------------------------------

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

# ------------------------------
# Custom CSS
# ------------------------------

st.markdown("""
<style>

.main{
    background-color:#f5f5f5;
}

h1,h2,h3{
    color:#0f172a;
}

.stButton>button{
    width:100%;
    height:55px;
    font-size:20px;
    border-radius:12px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------
# Sidebar
# ------------------------------

st.sidebar.title("🎓 Student Performance Prediction")

st.sidebar.markdown("---")

st.sidebar.subheader("Project Details")

st.sidebar.write("**Developer:** Princy Tripathi")

st.sidebar.write("**College:**")

st.sidebar.write("United College of Engineering & Research")

st.sidebar.write("**Model Used:**")

st.sidebar.write("Random Forest Regressor")

st.sidebar.write("**Dataset:**")

st.sidebar.write("Student Performance Dataset")

st.sidebar.markdown("---")

st.sidebar.success(
"""
This application predicts a student's final examination performance using Machine Learning.
"""
)

# ------------------------------
# Main Heading
# ------------------------------

st.title("🎓 Student Performance Prediction System")

st.write(
"""
Fill all the details below to predict the student's final examination grade.
"""
)

st.markdown("---")

left,right = st.columns(2)

# ==========================
# LEFT COLUMN
# ==========================

with left:

    school = st.selectbox(
        "School",
        ["GP","MS"]
    )

    school = 0 if school=="GP" else 1

    gender = st.selectbox(
        "Gender",
        ["Female","Male"]
    )

    gender = 0 if gender=="Female" else 1

    age = st.slider(
        "Age",
        15,
        22,
        17
    )

    address = st.selectbox(
        "Address",
        ["Urban","Rural"]
    )

    address = 1 if address=="Urban" else 0

    family_size = st.selectbox(
        "Family Size",
        ["Greater than 3",
         "Less than or Equal to 3"]
    )

    family_size = 0 if family_size=="Greater than 3" else 1

    pstatus = st.selectbox(
        "Parents Living Together",
        ["Yes","No"]
    )

    pstatus = 1 if pstatus=="Yes" else 0

    medu = st.slider(
        "Mother's Education",
        0,
        4,
        2
    )

    fedu = st.slider(
        "Father's Education",
        0,
        4,
        2
    )

    studytime = st.slider(
        "Study Time",
        1,
        4,
        2
    )

    failures = st.slider(
        "Past Failures",
        0,
        4,
        0
    )

# ==========================
# RIGHT COLUMN
# ==========================

with right:

    schoolsup = st.selectbox(
        "School Support",
        ["No","Yes"]
    )

    schoolsup = 0 if schoolsup=="No" else 1

    famsup = st.selectbox(
        "Family Support",
        ["No","Yes"]
    )

    famsup = 0 if famsup=="No" else 1

    paid = st.selectbox(
        "Extra Paid Classes",
        ["No","Yes"]
    )

    paid = 0 if paid=="No" else 1

    higher = st.selectbox(
        "Higher Education",
        ["No","Yes"]
    )

    higher = 0 if higher=="No" else 1

    internet = st.selectbox(
        "Internet Access",
        ["No","Yes"]
    )

    internet = 0 if internet=="No" else 1

    absences = st.number_input(
        "Absences",
        0,
        100,
        5
    )

    health = st.slider(
        "Health",
        1,
        5,
        3
    )

    goout = st.slider(
        "Going Out Frequency",
        1,
        5,
        3
    )

    g1 = st.slider(
        "First Period Grade (G1)",
        0,
        20,
        10
    )

    g2 = st.slider(
        "Second Period Grade (G2)",
        0,
        20,
        10
    )

st.markdown("---")
# ==========================================
# Prediction Button
# ==========================================

if st.button("🚀 Predict Final Grade"):

    input_df = pd.DataFrame({

        "school":[school],
        "sex":[gender],
        "age":[age],
        "address":[address],
        "famsize":[family_size],
        "Pstatus":[pstatus],
        "Medu":[medu],
        "Fedu":[fedu],
        "studytime":[studytime],
        "failures":[failures],
        "schoolsup":[schoolsup],
        "famsup":[famsup],
        "paid":[paid],
        "higher":[higher],
        "internet":[internet],
        "absences":[absences],
        "health":[health],
        "goout":[goout],
        "G1":[g1],
        "G2":[g2]

    })

    prediction = model.predict(input_df)[0]

    prediction = max(0, min(20, prediction))

    st.markdown("---")

    st.subheader("📊 Prediction Result")

    st.metric(
        label="Predicted Final Grade",
        value=f"{prediction:.2f} / 20"
    )

    st.progress(prediction / 20)

    if prediction >= 16:

        st.success("🌟 Excellent Performance")
        st.balloons()

        st.info("""
### Suggestions

✅ Continue your current study routine.

✅ Maintain regular attendance.

✅ Keep revising weekly.

✅ Practice previous year papers.
""")

    elif prediction >= 12:

        st.success("👍 Good Performance")

        st.info("""
### Suggestions

✅ Increase study time.

✅ Focus on weak subjects.

✅ Avoid unnecessary absences.
""")

    elif prediction >= 8:

        st.warning("📘 Average Performance")

        st.info("""
### Suggestions

✅ Make a daily study timetable.

✅ Revise every week.

✅ Solve more practice questions.

✅ Improve attendance.
""")

    else:

        st.error("📚 Needs Improvement")

        st.info("""
### Suggestions

✅ Spend more time studying.

✅ Reduce distractions.

✅ Ask teachers for guidance.

✅ Practice regularly.
""")

# ==========================================
# Footer
# ==========================================

st.markdown("---")

st.subheader("📖 About This Project")

st.write("""
This project predicts the final grade (G3) of a student using a
Random Forest Regression model trained on academic and personal
attributes.

### Technologies Used
- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit

### Machine Learning Model
Random Forest Regressor

### Dataset
Student Performance Dataset

### Developed By
Princy Tripathi
B.Tech Computer Science & Engineering
United College of Engineering & Research
""")