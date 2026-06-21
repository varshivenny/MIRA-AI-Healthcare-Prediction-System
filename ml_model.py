import joblib


model=joblib.load(
"models/health_model.pkl"
)



def predict(glucose,hb,cholesterol):

    result=model.predict(
    [
        [
        glucose,
        hb,
        cholesterol
        ]
    ]
    )[0]


    if result=="High Risk":

        remark="""
        🚨 High Risk detected.
        Consult doctor and monitor health.
        """

    elif result=="Medium Risk":

        remark="""
        ⚠ Moderate Risk.
        Improve diet and lifestyle.
        """

    elif result=="Low Risk":

        remark="""
        🟡 Slight changes detected.
        Regular checkups recommended.
        """

    else:

        remark="""
        🟢 Health parameters look normal.
        """


    return result+" "+remark