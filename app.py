import streamlit as st
import pandas as pd
import plotly.express as px

from database import *
from ml_model import predict
from validation import *


st.set_page_config(
page_title="MIRA AI Healthcare",
layout="wide"
)


create()


st.sidebar.title(
"🏥 MIRA AI"
)


password=st.sidebar.text_input(
"Admin Password",
type="password"
)


if password!="admin123":

    st.warning(
    "Enter admin password"
    )

    st.stop()



menu=st.sidebar.radio(

"Dashboard",

[
"Add Patient",
"View Patients",
"Analytics",
"Update",
"Delete"
]

)



st.title(
"🤖 MIRA Medical Intelligence Robotic Automation"
)


# ADD PATIENT

if menu=="Add Patient":


    name=st.text_input(
    "Patient Full Name"
    )


    dob=st.date_input(
    "Date of Birth"
    )


    email=st.text_input(
    "Email"
    )


    c1,c2,c3=st.columns(3)


    glucose=c1.number_input(
    "Glucose"
    )


    hb=c2.number_input(
    "Haemoglobin"
    )


    chol=c3.number_input(
    "Cholesterol"
    )


    if st.button(
    "Predict using AI"
    ):


        if not email_check(email):

            st.error(
            "Invalid Email"
            )


        elif not dob_check(dob):

            st.error(
            "Invalid DOB"
            )


        else:


            result=predict(
            glucose,
            hb,
            chol
            )


            insert(
            (
            name,
            str(dob),
            email,
            glucose,
            hb,
            chol,
            result
            )
            )


            st.success(result)




elif menu=="View Patients":


    records=show()


    df=pd.DataFrame(

    records,

    columns=[
    "ID",
    "Name",
    "DOB",
    "Email",
    "Glucose",
    "HB",
    "Cholesterol",
    "AI Remarks"
    ]

    )


    search=st.text_input(
    "Search Patient"
    )


    if search:

        df=df[
        df["Name"].str.contains(
        search,
        case=False
        )
        ]


    st.dataframe(df)



    st.download_button(

    "Download Report",

    df.to_csv(),

    "patient_report.csv"

    )





elif menu=="Analytics":


    df=pd.DataFrame(
    show(),
    columns=[
    "ID","Name","DOB",
    "Email",
    "Glucose",
    "HB",
    "Cholesterol",
    "Remarks"
    ]
    )


    st.metric(
    "Total Patients",
    len(df)
    )


    fig=px.histogram(

    df,

    x="Glucose",

    title="Patient Glucose Analysis"

    )


    st.plotly_chart(fig)




elif menu=="Update":


    id=st.number_input(
    "Patient ID"
    )


    remark=st.text_area(
    "New Remark"
    )


    if st.button("Update"):

        update(
        id,
        remark
        )

        st.success(
        "Updated Successfully"
        )




elif menu=="Delete":


    id=st.number_input(
    "Enter Patient ID"
    )


    if st.button(
    "Delete Record"
    ):

        delete(id)

        st.success(
        "Deleted"
        )