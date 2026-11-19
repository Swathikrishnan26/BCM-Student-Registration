import streamlit as st
from datetime import date

st.set_page_config(
    page_title="B.C.M. College Kottayam (Autonomous) Registration Portal",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #f0f6ff;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}

h1, h2, h3 {
    color: #12366b;
}

div[data-testid="stForm"] {
    background-color: white;
    border: 2px solid #1e5aa8;
    border-radius: 15px;
    padding: 25px;
}

div[data-testid="stForm"] label {
    color: #12366b;
    font-weight: 600;
}

div[data-testid="stFormSubmitButton"] button {
    background-color: #174b91;
    color: white;
    border-radius: 8px;
    height: 45px;
    font-weight: bold;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background-color: #0e3265;
    border: 1px solid #0e3265;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] {
    border-radius: 6px;
}

hr {
    border-color: #b6d0f5;
}
</style>
""", unsafe_allow_html=True)

# ---------- COLLEGE HEADER WITH LOGO ----------

col_logo, col_title = st.columns([1,4],gap="small",vertical_alignment="center")

with col_logo:
    st.image("bcm_logo.png", width=150)

with col_title:
    st.markdown("""
    <div style="text-align:center; padding:10px 0px;">
        <h1 style="color:#a51c83; margin-bottom:0;">
            B.C.M. COLLEGE, KOTTAYAM
        </h1>
        <h3 style="color:#087da5; margin-top:5px;">
            (AUTONOMOUS)
        </h3>
        <h2 style="color:#174b91;">
            STUDENT REGISTRATION PORTAL
        </h2>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.subheader("Student Registration")

st.caption("Please enter your details carefully.")

# ---------- UG COURSES ----------

UG_COURSES = [
    "B.A. (Hons) English Language & Literature",
    "B.A. (Hons) Economics",
    "B.A. (Hons) Sociology",
    "B.A. (Hons) History",
    "B.Sc. (Hons) Mathematics",
    "B.Sc. (Hons) Computer Science (SF)",
    "B.Sc. (Hons) Home Science",
    "B.Sc. (Hons) Food Science & Quality Control (SF)",
    "B.Sc. (Hons) Zoology",
    "B.Sc. (Hons) Physics",
    "B.Sc. (Hons) Chemistry",
    "B.Sc. (Hons) Botany",
    "B.Com. (Hons) (SF)",
    "B.Com. (Hons)"
]


# ---------- PG COURSES ----------

PG_COURSES = [
    "M.A. English",
    "M.Sc. Mathematics",
    "M.Sc. Statistics",
    "M.Sc. Home Science (Child Development) (SF)",
    "M.Com. (SF)",
    "Master of Social Work (SF)"
]


# ---------- CLASS 10 BOARD OPTIONS ----------

SSLC_BOARDS = [
    "CBSE",
    "CISCE",
    "NIOS",
    "MSBSHSE",
    "TNDGE",
    "KSEEB",
    "Kerala Board of School Education",
    "Other"
]


# ---------- CLASS 12 BOARD OPTIONS ----------

PLUS_TWO_BOARDS = [
    "CBSE",
    "CISCE",
    "NIOS",
    "DHSE",
    "Government of Kerala",
    "MSBSHSE",
    "Board of Higher Secondary",
    "Tamil Nadu",
    "Other"
]


# ---------- PERCENTAGE OPTIONS ----------

PERCENTAGE_RANGES = [
    "30-40%",
    "40-50%",
    "50-60%",
    "60-70%",
    "70-80%",
    "80-90%",
    "90-100%"
]

# ---------- PERSONAL INFORMATION ----------

st.markdown("## 1. Personal Information")

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:
        full_name = st.text_input("Full Name *")

    with col2:
        dob = st.date_input(
            "Date of Birth *",
            value=None,
            min_value=date(1980, 1, 1),
            max_value=date.today(),
            format="DD/MM/YYYY"
        )

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox(
            "Gender *",
            ["Select Gender", "FEMALE", "MALE", "OTHER GENDER"]
        )

    with col2:
        email = st.text_input("Email Address *")

    col1, col2 = st.columns(2)

    with col1:
        contact = st.text_input("Contact / WhatsApp Number *")

    with col2:
        guardian_contact = st.text_input(
            "Guardian's Contact Number *"
        )

    address = st.text_area("Address *")

# ---------- COURSE DETAILS ----------

st.markdown("## 2. Course Details")

with st.container(border=True):

    program_level = st.selectbox(
        "Program Level *",
        ["Select Program", "UG", "PG"]
    )

    st.markdown("### Course Applied For")

    if program_level == "UG":
        available_courses = UG_COURSES

    elif program_level == "PG":
        available_courses = PG_COURSES

    else:
        available_courses = []

    if program_level == "Select Program":

        st.info("Please select UG or PG to view available courses.")

    else:

        col1, col2 = st.columns(2)

        with col1:
            preference1 = st.selectbox(
                "Preference 1 *",
                ["Select Course"] + available_courses
            )

        with col2:
            preference2 = st.selectbox(
                "Preference 2",
                ["Select Course"] + available_courses
            )

        preference3 = st.selectbox(
            "Preference 3",
            ["Select Course"] + available_courses
        )

# ---------- ACADEMIC QUALIFICATION ----------

st.markdown("## 3. Academic Qualification")

if program_level == "UG":

    with st.container(border=True):

        st.markdown("### Class 10 (SSLC) Details")

        col1, col2 = st.columns(2)

        with col1:
            sslc_board = st.selectbox(
                "Board of Examination *",
                ["Select Board"] + SSLC_BOARDS
            )

        with col2:
            sslc_year = st.number_input(
                "Year of Passing *",
                min_value=2000,
                max_value=date.today().year,
                step=1
            )

        sslc_percentage = st.selectbox(
            "Percentage Obtained *",
            ["Select Percentage"] + PERCENTAGE_RANGES
        )


elif program_level == "PG":

    with st.container(border=True):

        st.markdown("### Class 12 (+2) Details")

        col1, col2 = st.columns(2)

        with col1:
            plus_two_board = st.selectbox(
                "Board of Examination *",
                ["Select Board"] + PLUS_TWO_BOARDS
            )

        with col2:
            plus_two_year = st.number_input(
                "Year of Passing *",
                min_value=2000,
                max_value=date.today().year,
                step=1
            )

        plus_two_percentage = st.selectbox(
            "Percentage Obtained *",
            ["Select Percentage"] + PERCENTAGE_RANGES
        )

# ---------- APPLICATION SUBMISSION ----------

st.markdown("## 4. Submit Application")

with st.container(border=True):

    st.markdown("Please review your details before submitting.")

    if st.button("SUBMIT APPLICATION", type="primary", use_container_width=True):

        errors = []

        # Personal information validation
        if not full_name.strip():
            errors.append("Please enter your full name.")

        if dob is None:
            errors.append("Please select your date of birth.")

        if gender == "Select Gender":
            errors.append("Please select your gender.")

        if not email.strip() or "@" not in email or "." not in email:
            errors.append("Please enter a valid email address.")

        if not contact.strip():
            errors.append("Please enter your contact number.")

        if not guardian_contact.strip():
            errors.append("Please enter your guardian's contact number.")

        if not address.strip():
            errors.append("Please enter your address.")

        # Course validation
        if program_level == "Select Program":
            errors.append("Please select UG or PG.")

        else:
            if preference1 == "Select Course":
                errors.append("Please select your first course preference.")

            selected_preferences = [
                p for p in [preference1, preference2, preference3]
                if p != "Select Course"
            ]

            if len(selected_preferences) != len(set(selected_preferences)):
                errors.append("Please select different courses for each preference.")

            # Academic qualification validation
            if program_level == "UG":

                if sslc_board == "Select Board":
                    errors.append("Please select your SSLC board.")

                if sslc_percentage == "Select Percentage":
                    errors.append("Please select your SSLC percentage.")

            elif program_level == "PG":

                if plus_two_board == "Select Board":
                    errors.append("Please select your Plus Two board.")

                if plus_two_percentage == "Select Percentage":
                    errors.append("Please select your Plus Two percentage.")

        # Display validation results
        if errors:

            st.error("Please correct the following details:")

            for error in errors:
                st.write("•", error)

        else:

            st.success("All required details have been entered correctly!")

            st.info(
                "Your application details have passed validation. "
                "The Google Sheets, PDF and email submission features "
                "will be connected in the next stages."
            )
