import streamlit as st
from datetime import date, datetime
from zoneinfo import ZoneInfo
import gspread
import base64
import re
# Phone number validation
def validate_phone(phone):
    digits = re.sub(r"\D", "", phone)
    return len(digits) == 10


# Email validation
def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.fullmatch(pattern, email.strip()) is not None
st.set_page_config(
    page_title="B.C.M. College Kottayam (Autonomous) Registration Portal",
    page_icon="🎓",
    layout="wide"
)

# ---------- CLEAR FORM AFTER SUCCESSFUL REGISTRATION ----------

if st.session_state.pop("_clear_registration_form", False):

    reset_values = {
        "full_name": "",
        "dob": None,
        "gender": "Select Gender",
        "email": "",
        "contact": "",
        "guardian_contact": "",
        "address": "",
        "program_level": "Select Program",
        "preference1": "Select Course",
        "preference2": "Select Course",
        "preference3": "Select Course",
        "sslc_board": "Select Board",
        "sslc_stream": "",
        "sslc_percentage": "Select Percentage",
        "plus_two_board": "Select Board",
        "plus_two_stream": "Select Stream",
        "plus_two_percentage": "Select Percentage"
    }

    for key, value in reset_values.items():
        st.session_state[key] = value

registration_success = st.session_state.pop(
    "_registration_success", False
)

# ---------- GOOGLE SHEETS CONNECTION ----------

credentials = dict(st.secrets["gcp_service_account"])
credentials["private_key"] = credentials["private_key"].replace("\\n", "\n")

gc = gspread.service_account_from_dict(credentials)

spreadsheet = gc.open("BCM Student Registrations")
worksheet = spreadsheet.sheet1

# ---------- PAGE DESIGN ----------

st.markdown("""
<style>

/* Main page background */
.stApp,
[data-testid="stAppViewContainer"] {
    background-color: #EFF5F8 !important;
    color-scheme: light !important;
}

/* Main content width */
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Headings */
h1, h2, h3 {
    color: #234766 !important;
}

h2 {
    font-size: 25px !important;
    margin-top: 20px;
    margin-bottom: 18px;
}

h3 {
    font-size: 19px !important;
}

/* Form containers */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFFFF !important;
    border: 1px solid #D4E0E9 !important;
    border-radius: 14px;
    padding: 22px;
    box-shadow: 0 3px 12px rgba(23, 50, 77, 0.06);
}

/* Input boxes */
div[data-testid="stTextInput"] input,
div[data-testid="stDateInput"] input,
div[data-testid="stTextArea"] textarea {
    background-color: #FFFFFF !important;
    color: #24364b !important;
    border: 1px solid #B8C8D8 !important;
    border-radius: 8px;
    min-height: 42px;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #24364b !important;
    border: 1px solid #B8C8D8 !important;
    border-radius: 8px;
    min-height: 42px;
}

/* Labels */
div[data-testid="stWidgetLabel"] p {
    color: #294563 !important;
    font-weight: 600;
    font-size: 14px;
}

/* Buttons */
.stButton > button {
    background-color: #17324D !important;
    color: #FFFFFF !important;
    border: none;
    border-radius: 9px;
    height: 48px;
    font-weight: 700;
    font-size: 16px;
}

.stButton > button:hover {
    background-color: #285477 !important;
    color: #FFFFFF !important;
}

/* Dividers */
hr {
    border-color: #D4E0E9 !important;
    margin-top: 22px;
    margin-bottom: 22px;
}

/* Information messages */
div[data-testid="stAlert"] {
    border-radius: 9px;
}

/* Spacing */
div[data-testid="stHorizontalBlock"] {
    gap: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------- COLLEGE HEADER ----------

st.markdown("""
<style>

/* College header */
.college-header {
    background: linear-gradient(120deg, #EAF2F8, #DCE8F2);
    border: 1px solid #C5D4E2;
    border-radius: 12px;
    padding: 25px 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 30px;
    min-height: 155px;
    width: 100%;
    box-sizing: border-box;
}

/* BCM logo */
.college-logo {
    width: 210px;
    max-height: 125px;
    height: auto;
    object-fit: contain;
    flex-shrink: 0;
}

/* Header title */
.header-text {
    color: #17324D;
    flex: 1;
}

.header-text h2 {
    color: #17324D !important;
    font-size: 29px !important;
    font-weight: 750;
    margin: 0;
    letter-spacing: 1.2px;
    line-height: 1.4;
}

/* Mobile screen */
@media (max-width: 600px) {

    .college-header {
        padding: 18px 12px;
        gap: 14px;
        min-height: 125px;
    }

    .college-logo {
        width: 125px;
        max-height: 100px;
    }

    .header-text h2 {
        font-size: 19px !important;
        letter-spacing: 0.5px;
    }
}

</style>
""", unsafe_allow_html=True)

# Load BCM logo
with open("bcm_logo.png", "rb") as logo_file:
    logo_base64 = base64.b64encode(logo_file.read()).decode()

# Display college header
st.markdown(f"""
<div class="college-header">
    <img src="data:image/png;base64,{logo_base64}"
         class="college-logo"
         alt="BCM College Logo">

    <div class="header-text">
        <h2>ONLINE REGISTRATION PORTAL</h2>
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

if registration_success:
    st.success("Registration submitted successfully!")
    st.info("Your details have been saved to the college registration records. The form is ready for the next student.")

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
        full_name = st.text_input(
            "Full Name *",
            key="full_name"
        )

    with col2:
        dob = st.date_input(
            "Date of Birth",
            value=None,
            min_value=date(1980, 1, 1),
            max_value=date(2026, 12, 31),
            format="DD/MM/YYYY",
            key="dob"
        )

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox(
            "Gender *",
            ["Select Gender", "FEMALE", "MALE", "OTHER"],
            key="gender"
        )

    with col2:
        email = st.text_input(
            "Email Address *",
            key="email"
        )

    col1, col2 = st.columns(2)

    with col1:
        contact_number = st.text_input(
            "Contact / WhatsApp Number *",
            key="contact"
        )

    with col2:
        guardian_contact = st.text_input(
            "Guardian's Contact Number *",
            key="guardian_contact"
        )

    address = st.text_area(
        "Address *",
        key="address"
    )


# ---------- COURSE DETAILS ----------

st.markdown("## 2. Course Details")

with st.container(border=True):

    program_level = st.selectbox(
        "Program Level *",
        ["Select Program", "UG", "PG"],
        key="program_level"
    )

    st.markdown("### Course Applied For")

    if program_level == "UG":

        major1 = st.selectbox(
            "Major 1 *",
            ["Select Course"] + UG_COURSES,
            key="major1"
        )

        major2 = st.selectbox(
            "Major 2",
            ["Select Course"] + UG_COURSES,
            key="major2"
        )

        # Store UG majors in the existing sheet columns
        preference1 = major1
        preference2 = major2
        preference3 = "Select Course"

    elif program_level == "PG":

        col1, col2 = st.columns(2)

        with col1:
            preference1 = st.selectbox(
                "Preference 1 *",
                ["Select Course"] + PG_COURSES,
                key="preference1"
            )

        with col2:
            preference2 = st.selectbox(
                "Preference 2",
                ["Select Course"] + PG_COURSES,
                key="preference2"
            )

        preference3 = st.selectbox(
            "Preference 3",
            ["Select Course"] + PG_COURSES,
            key="preference3"
        )

    else:
        st.info("Please select UG or PG to view available courses.")


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
            sslc_stream = st.selectbox(
                "Current Stream of Study *",
                [
                    "Select Stream",
                    "Science",
                    "Commerce",
                    "Humanities",
                    "Vocational (VHSE)",
                    "Technical",
                    "Other"
                ]
            )

        sslc_percentage = st.selectbox(
            "Percentage Obtained in 10 th *",
            ["Select Percentage"] + PERCENTAGE_RANGES
        )
elif program_level == "PG":

    with st.container(border=True):

        st.markdown("### Class 12 Details")

        col1, col2 = st.columns(2)

        with col1:
            plus_two_board = st.selectbox(
                "Board of Examination *",
                ["Select Board"] + PLUS_TWO_BOARDS,
                key="plus_two_board"
            )

        with col2:
             plus_two_stream = st.text_input(
                "Current Stream of Study *",
                placeholder="Enter your stream of study"
            )
        plus_two_percentage = st.selectbox(
            "Percentage Obtained in 12 th*",
            ["Select Percentage"] + PERCENTAGE_RANGES,
            key="plus_two_percentage"
        )
# ---------- RESIDENTIAL TRAINING PROGRAMME ----------

st.markdown("## 4. Residential Training Programme")

with st.container(border=True):

    st.markdown(
        "**Would you like to opt for a Residential Training Programme at BCM?**"
    )

    residential_training = st.multiselect(
        "Select your preferred training programmes",
        [
            "BCM Civil Service Academy",
            "SSC, PSC, RRB, Bank Exams",
            "ACCA",
            "CA (India)",
            "BCM Defence Academy (Uniform Services)",
            "Soft Skills for Professionals",
            "NET/JRF"
        ],
        placeholder="Choose one or more programmes"
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

        if not validate_email(email):
            errors.append("Please enter a valid email address.")

        if not validate_phone(contact_number):
            errors.append("Contact number must contain at least 10 digits.")

        if not validate_phone(guardian_contact):
            errors.append("Guardian contact number must contain at least 10 digits.")

        if not address.strip():
            errors.append("Please enter your address.")

        # Course validation

        if program_level == "Select Program":
            errors.append("Please select UG or PG.")

        elif program_level == "UG":

            if major1 == "Select Course":
                errors.append("Please select Major 1.")

            if major2 != "Select Course" and major1 == major2:
                errors.append("Major 1 and Major 2 must be different.")

        elif program_level == "PG":

            if preference1 == "Select Course":
                errors.append("Please select Preference 1.")

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

            if sslc_stream == "Select Stream":
                errors.append("Please select your current stream of study.")

            if sslc_percentage == "Select Percentage":
                errors.append("Please select your SSLC percentage.")

        elif program_level == "PG":

            if plus_two_board == "Select Board":
                errors.append("Please select your Plus Two board.")

            if not plus_two_stream.strip():
                errors.append("Please enter your current stream of study.")

            if plus_two_percentage == "Select Percentage":
                errors.append("Please select your Plus Two percentage.")

        # Display errors

        if errors:

            st.error("Please correct the following details:")

            for error in errors:
                st.write("•", error)

        else:

            # Academic details

            if program_level == "UG":
                board = sslc_board
                stream = sslc_stream
                percentage = sslc_percentage

            else:
                board = plus_two_board
                stream = plus_two_stream
                percentage = plus_two_percentage

            # Submission date and time in IST

            now_ist = datetime.now(ZoneInfo("Asia/Kolkata"))

            submission_date = now_ist.strftime("%d/%m/%Y")
            submission_time = now_ist.strftime("%I:%M %p")

            # Save student details

            student_data = [
                full_name,
                dob.strftime("%d/%m/%Y"),
                gender,
                email,
                contact_number,
                guardian_contact,
                address,
                program_level,
                preference1,
                preference2 if preference2 != "Select Course" else "",
                preference3 if preference3 != "Select Course" else "",
                board,
                stream,
                percentage,
                submission_date,
                submission_time,
                ", ".join(residential_training)
            ]

            try:

                worksheet.append_row(
                    student_data,
                    value_input_option="USER_ENTERED"
                )

                st.session_state["_registration_success"] = True
                st.session_state["_clear_registration_form"] = True

                st.rerun()

            except Exception as e:

                st.error("Unable to save your registration. Please try again.")
                st.write(e)

        

            


                
# ---------- FOOTER ----------

st.markdown("""
<style>
.footer {
    background-color: #17324D;
    color: white;
    text-align: center;
    padding: 12px;
    border-radius: 6px;
    margin-top: 25px;
    font-size: 13px;
}
</style>

<div class="footer">
    <b>For Enquiries:</b> +91 XXXXXXXXXX | +91 XXXXXXXXXX
    <br>
    B. C. M. College, Kottayam (Autonomous)
</div>
""", unsafe_allow_html=True)

