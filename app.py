import streamlit as st
import pandas as pd
from datetime import datetime
from docx import Document
from io import BytesIO

# --- Page Config ---
st.set_page_config(page_title="Class Attendance", layout="centered")

# --- Imaginary Student List ---
student_list = [
    {"Name": "POORVA BETWAR", "Roll Number": "1"},
    {"Name": "KHUSHI BHATIA", "Roll Number": "2"},
    {"Name": "BHUMI BOMEWAR", "Roll Number": "3"},
    {"Name": "CHAITANYA PISE", "Roll Number": "4"},
    {"Name": "THORAVI DAF", "Roll Number": "5"},
    {"Name": "RUTUJA DESHMUKH", "Roll Number": "6"},
    {"Name": "MRUGAKSHI FULZELE", "Roll Number": "7"},
    {"Name": "KAMAKSHI HANVAT", "Roll Number": "8"},
    {"Name": "HARSHITA DAYMA", "Roll Number": "9"},
    {"Name": "TANVI HONADE", "Roll Number": "10"},
    {"Name": "SAYALI JIBHAKATE", "Roll Number": "11"},
    {"Name": "SHRUTI KOSURKAR", "Roll Number": "12"},
    {"Name": "PRIYANKA PARATE", "Roll Number": "13"},
    {"Name": "VRUSHALI PARATKAR", "Roll Number": "14"},
    {"Name": "SANSKRUTI RAUT", "Roll Number": "15"},
    {"Name": "NOOPUR SELOKAR", "Roll Number": "16"},
    {"Name": "NAKSHATRA SHARMA", "Roll Number": "17"},
    {"Name": "APURVA TONGE", "Roll Number": "18"},
    {"Name": "RAKHI VERMA", "Roll Number": "19"},
    {"Name": "GAURI YADAV", "Roll Number": "20"},
    {"Name": "SUHANI YADAV", "Roll Number": "21"},
    {"Name": "ADITYA TIWARI", "Roll Number": "22"},
    {"Name": "HARSH AGREY", "Roll Number": "23"},
    {"Name": "ABHISHEK AKHAND", "Roll Number": "24"},
    {"Name": "VARDHAN ANDRASKAR", "Roll Number": "25"},
    {"Name": "TUSHAR BAGHELE", "Roll Number": "26"},
    {"Name": "HARSHAL BAIS", "Roll Number": "27"},
    {"Name": "TANAY BANAIT", "Roll Number": "28"},
    {"Name": "SAGAR BANDAWAR", "Roll Number": "29"},
    {"Name": "ANIRUDDHA BANGRE", "Roll Number": "30"},
    {"Name": "SARTHAK BANKAR", "Roll Number": "31"},
    {"Name": "BHAVESH BARGAT", "Roll Number": "32"},
    {"Name": "ANUJ BARLAWAR", "Roll Number": "33"},
    {"Name": "MANTHAN BELEKAR", "Roll Number": "34"},
    {"Name": "DURGESH BHAGAT", "Roll Number": "35"},
    {"Name": "BHUVAN BHIOGADE", "Roll Number": "36"},
    {"Name": "RUSHIKESH BURDE", "Roll Number": "37"},
    {"Name": "SUJAY DAS", "Roll Number": "38"},
    {"Name": "DIVYA BANGDE", "Roll Number": "39"},
    {"Name": "ABHISHEK FALTANKAR", "Roll Number": "40"},
    {"Name": "SOHAM GAIKWAD", "Roll Number": "41"},
    {"Name": "ANAND HATMODE", "Roll Number": "42"},
    {"Name": "KAPIL HOKARNE", "Roll Number": "43"},
    {"Name": "ADESH INGLE", "Roll Number": "44"},
    {"Name": "ADARSH JAISWAL", "Roll Number": "45"},
    {"Name": "KAPUR PARDHI", "Roll Number": "46"},
    {"Name": "KUSHAL MEHAR", "Roll Number": "47"},
    {"Name": "SHREE LAROKAR", "Roll Number": "48"},
    {"Name": "VEDANT MESHRAM", "Roll Number": "49"},
    {"Name": "OM MALEWAR", "Roll Number": "50"},
    {"Name": "PRANAV VALLUVAR", "Roll Number": "51"},
    {"Name": "MORESHWAR PACHBHAI", "Roll Number": "52"},
    {"Name": "OM PATIL", "Roll Number": "53"},
    {"Name": "KUNAL RAHANGDALE", "Roll Number": "54"},
    {"Name": "ATHANG RAMTEKE", "Roll Number": "55"},
    {"Name": "KRISHNA SAHU", "Roll Number": "56"},
    {"Name": "SAURABH SHARMA", "Roll Number": "57"},
    {"Name": "AYAN SHEIKH", "Roll Number": "58"},
    {"Name": "HIMANSHU SHUKLA", "Roll Number": "59"},
    {"Name": "ARYA SINGANJUDE", "Roll Number": "60"},
    {"Name": "VINEET SINGH", "Roll Number": "61"},
    {"Name": "ADITYA TEMBHARE", "Roll Number": "62"},
    {"Name": "ATUL THAKRE", "Roll Number": "63"},
    {"Name": "YUVRAJ THAKRE", "Roll Number": "64"},
    {"Name": "CHANDRAKANT THAKUR", "Roll Number": "65"},
    {"Name": "ANSHUL UMBARKAR", "Roll Number": "66"},
    {"Name": "UTKARSH SONSARE", "Roll Number": "67"},
    {"Name": "VAIBHAV ENAME", "Roll Number": "68"},
    {"Name": "VAISHALI STUDDEDU", "Roll Number": "69"},
    {"Name": "VIRAJ WANKHADE", "Roll Number": "70"}
]


# --- Session State ---
if "present_list" not in st.session_state:
    st.session_state.present_list = []

if "absent_list" not in st.session_state:
    st.session_state.absent_list = []

st.title("📋 Class Attendance System")

st.subheader("👩‍🏫 Mark Attendance")

# --- Attendance Form ---
with st.form("attendance_form"):
    marked_attendance = {}
    for student in student_list:
        key = f"{student['Roll Number']}_status"
        status = st.checkbox(
            f"{student['Roll Number']} - {student['Name']}",
            key=key,
            value=True
        )
        marked_attendance[student["Roll Number"]] = "Present" if status else "Absent"

    submitted = st.form_submit_button("✅ Submit Attendance")

    if submitted:
        today = datetime.now().strftime("%Y-%m-%d")
        st.session_state.present_list.clear()
        st.session_state.absent_list.clear()

        for student in student_list:
            record = {
                "Date": today,
                "Name": student["Name"],
                "Roll Number": student["Roll Number"]
            }
            if marked_attendance[student["Roll Number"]] == "Present":
                st.session_state.present_list.append(record)
            else:
                st.session_state.absent_list.append(record)

        st.success("🎉 Attendance submitted successfully!")

# --- Display Tables ---
def show_table(title, data_list, color):
    if data_list:
        st.subheader(f"{title}")
        df = pd.DataFrame(data_list)
        st.dataframe(df, use_container_width=True)
        return df
    return None

df_present = show_table("✅ Present Students", st.session_state.present_list, "green")
df_absent = show_table("❌ Absent Students", st.session_state.absent_list, "red")

# --- Create Word file ---
def create_word_file(present_df, absent_df):
    doc = Document()
    doc.add_heading("Class Attendance Report", 0)
    doc.add_paragraph(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    doc.add_paragraph("")

    if not present_df.empty:
        doc.add_heading("✅ Present Students", level=1)
        table = doc.add_table(rows=1, cols=len(present_df.columns))
        hdr_cells = table.rows[0].cells
        for i, col in enumerate(present_df.columns):
            hdr_cells[i].text = col
        for _, row in present_df.iterrows():
            row_cells = table.add_row().cells
            for i, val in enumerate(row):
                row_cells[i].text = str(val)
        doc.add_paragraph("")

    if not absent_df.empty:
        doc.add_heading("❌ Absent Students", level=1)
        table = doc.add_table(rows=1, cols=len(absent_df.columns))
        hdr_cells = table.rows[0].cells
        for i, col in enumerate(absent_df.columns):
            hdr_cells[i].text = col
        for _, row in absent_df.iterrows():
            row_cells = table.add_row().cells
            for i, val in enumerate(row):
                row_cells[i].text = str(val)

    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

# --- Download Word Button ---
if submitted:
    word_file = create_word_file(df_present if df_present is not None else pd.DataFrame(),
                                  df_absent if df_absent is not None else pd.DataFrame())

    st.download_button(
        label="📥 Download Attendance as Word File (.docx)",
        data=word_file,
        file_name="attendance_report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
