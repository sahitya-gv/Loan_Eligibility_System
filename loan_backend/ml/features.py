def add_features(df):
    df = df.copy()
    df["TotalIncome"] = df["ApplicantIncome"] + df["CoapplicantIncome"]
    df["EMI"] = df["LoanAmount"] / df["Loan_Amount_Term"]
    df["Income_to_Loan"] = df["TotalIncome"] / (df["LoanAmount"] + 1)
    return df