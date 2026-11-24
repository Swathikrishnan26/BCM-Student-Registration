import streamlit as st
from datetime import date
import gspread
import streamlit as st
from datetime import date
import gspread
import base64
from pathlib import Path
st.set_page_config(
    page_title="B.C.M. College Kottayam (Autonomous) Registration Portal",
    page_icon="🎓",
    layout="wide"
)
# ---------- GOOGLE SHEETS CONNECTION ----------

credentials = dict(st.secrets["gcp_service_account"])

credentials["private_key"] = credentials["private_key"].replace("\\n", "\n")

gc = gspread.service_account_from_dict(credentials)

spreadsheet = gc.open("BCM Student Registrations")

worksheet = spreadsheet.sheet1
st.markdown("""
<style>

/* ---------- MAIN PAGE ---------- */
.stApp {
        background-color: #F7F4FC !important;
}
.block-container {
 max-width: 1150px; 
 padding-top: 2rem; 
 padding-bottom: 3rem; 
 }
 /* Reduce space around registration instruction */
div[data-testid="stMarkdown"] p {
    margin-bottom: 2px !important;
}

/* Reduce space before Personal Information */
h2 {
    margin-top: 5px !important;
    margin-bottom: 10px !important;
}

/* ---------- HEADINGS ---------- */

h1, h2, h3 {
        color: #493B67 !important;
}

h2 {
    font-size: 25px !important;
    margin-top: 20px;
    margin-bottom: 18px;
}

h3 {
    font-size: 19px !important;
}

/* ---------- SECTION BORDERS ---------- */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #ffffff;
    border: 1px solid #d5dfec;
    border-radius: 14px;
    padding: 22px;
    box-shadow: 0 3px 12px rgba(23, 54, 93, 0.06);
}

/* ---------- INPUT BOXES ---------- */

div[data-testid="stTextInput"] input,
div[data-testid="stDateInput"] input,
div[data-testid="stTextArea"] textarea {
    background-color: #ffffff;
    border: 1px solid #bdcbdc;
    border-radius: 8px;
    color: #24364b;
    min-height: 42px;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background-color: #ffffff;
    border: 1px solid #bdcbdc;
    border-radius: 8px;
    min-height: 42px;
}

/* ---------- LABELS ---------- */

div[data-testid="stWidgetLabel"] p {
    color: #294563;
    font-weight: 600;
    font-size: 14px;
}

/* ---------- BUTTONS ---------- */

.stButton > button {
    background-color: #174b78;
    color: white;
    border: none;
    border-radius: 9px;
    height: 48px;
    font-weight: 700;
    font-size: 16px;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background-color: #0e3457;
    color: white;
    border: none;
}

/* ---------- DIVIDERS ---------- */

hr {
    border-color: #d5dfec;
    margin-top: 22px;
    margin-bottom: 22px;
}

/* ---------- INFORMATION MESSAGES ---------- */

div[data-testid="stAlert"] {
    border-radius: 9px;
}

/* ---------- RESPONSIVE SPACING ---------- */

div[data-testid="stHorizontalBlock"] {
    gap: 20px;
}

/* ---------light lavender THEME OVERRIDE ---------- */

/* Main page background */
.stApp,
[data-testid="stAppViewContainer"] {
        background-color: #EFF7F6 !important;
}
}

/* Main headings */
h1, h2, h3 {
            color: #36556D !important;
}

/* Form containers */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFFFF !important;
    border-color: #DDD9E5 !important;
    box-shadow: 0 3px 12px rgba(57, 51, 79, 0.06) !important;
}

/* Buttons */
.stButton > button {
    background-color: #39334F !important;
    color: #FFFFFF !important;
}

.stButton > button:hover {
    background-color: #514968 !important;
    color: #FFFFFF !important;
}

/* Input borders */
div[data-testid="stTextInput"] input,
div[data-testid="stDateInput"] input,
div[data-testid="stTextArea"] textarea {
    border-color: #C9C3D5 !important;
}

/* Dividers */
hr {
    border-color: #DDD9E5 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------- NEW COLLEGE HEADER ----------

st.markdown("""
<style>
.college-header {
    background: linear-gradient(120deg, #F1EAF8, #E4D8F0);
    border: 1px solid #D5C5E5;
    border-radius: 8px;
    padding: 22px 25px;
    display: flex;
    align-items: center;
    gap: 25px;
    min-height: 125px;
    width: 100%;
    box-sizing: border-box;
}

.college-logo {
    width: 120px;
    height: auto;
    object-fit: contain;
    flex-shrink: 0;
}

.header-text {
    color: #39334F;
}

.header-text h2 {
    color: #39334F !important;
    font-size: 27px;
    margin: 0;
    letter-spacing: 1px;
}

.header-text p {
    color: #514968;
    font-size: 13px;
    margin: 8px 0 0 0;
}

@media (max-width: 600px) {
    .college-header {
        padding: 15px;
        gap: 12px;
    }

    .college-logo {
        width: 140px;
    }

    .header-text h2 {
        font-size: 19px;
    }
}
</style>
""", unsafe_allow_html=True)




import base64

with open("bcm_logo.png", "rb") as logo_file:
    logo_base64 = base64.b64encode(logo_file.read()).decode()

st.markdown(f"""
<div class="college-header">
    <img src="data:image/png;base64,{logo_base64}"
         class="college-logo">
    <div class="header-text">
        <h2>ONLINE REGISTRATION FORM</h2>
        <p>B. C. M. College, Kottayam (Autonomous)</p>
    </div>
</div>
""", unsafe_allow_html=True)
# ---------- REGISTRATION INSTRUCTION ----------

st.markdown("""
<p style="
    color: #64748b;
    font-size: 14px;
    margin: 8px 0 0 0;
    padding: 0;
    line-height: 1.3;
">
    Please fill out the form to register your application.
</p>
""", unsafe_allow_html=True)

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
    "TNDGE",
    "Kerala Board of School Education",
    "Other"
]


# ---------- CLASS 12 BOARD OPTIONS ----------

PLUS_TWO_BOARDS = [
    "CBSE",
    "CISCE",
    "NIOS",
    "DHSE KERALA",
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
      "Date of Birth",
       value=None,
       min_value=date(1980, 1, 1),
       max_value=date(2026, 12, 31),
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

        st.markdown("### Class 10 Details")

        col1, col2 = st.columns(2)

        with col1:
            sslc_board = st.selectbox(
                "Board of Examination *",
                ["Select Board"] + SSLC_BOARDS
            )

        with col2:
            sslc_stream = st.text_input(
    "Current Stream of Study *",
    placeholder="Enter your current stream of study"
            )

        sslc_percentage = st.selectbox(
            "Percentage Obtained in 10 th *",
            ["Select Percentage"] + PERCENTAGE_RANGES
        )


elif program_level == "PG":

    with st.container(border=True):

        st.markdown("### Class 12  Details")

        col1, col2 = st.columns(2)

        with col1:
            plus_two_board = st.selectbox(
                "Board of Examination *",
                ["Select Board"] + PLUS_TWO_BOARDS
            )

        with col2:
            plus_two_stream = st.text_input(
    "Current Stream of Study *",
    placeholder="Enter your current stream of study"
           )

        plus_two_percentage = st.selectbox(
            "Percentage Obtained in 12 th*",
            ["Select Percentage"] + PERCENTAGE_RANGES
        )

# ---------- APPLICATION SUBMISSION ----------


with st.container(border=True):

    st.markdown("Please review your details before registering.")

    if st.button("REGISTER", type="primary", use_container_width=True):

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

            if program_level == "UG":
                board = sslc_board
                stream = sslc_stream
                percentage = sslc_percentage

            else:
                board = plus_two_board
                stream = plus_two_stream
                percentage = plus_two_percentage

            student_data = [
                full_name,
                dob.strftime("%d/%m/%Y"),
                gender,
                email,
                contact,
                guardian_contact,
                address,
                program_level,
                preference1,
                preference2 if preference2 != "Select Course" else "",
                preference3 if preference3 != "Select Course" else "",
                board,
                stream,
                percentage
            ]

            try:
                worksheet.append_row(
                    student_data,
                    value_input_option="USER_ENTERED"
                )

                st.success("Registration submitted successfully!")
                st.info("Your details have been saved to the college registration records.")

            except Exception as e:
                st.error("Unable to save your registration. Please try again.")
                st.write(e)
