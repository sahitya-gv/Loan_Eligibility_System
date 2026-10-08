from ml.predictor import predict_loan

strong = {
    "Gender": "Male", "Married": "Yes", "Dependents": 0,
    "Education": "Graduate", "Self_Employed": "No",
    "ApplicantIncome": 6000, "CoapplicantIncome": 2000,
    "LoanAmount": 120, "Loan_Amount_Term": 360,
    "Credit_History": 1, "Property_Area": "Urban",
}

weak = {
    "Gender": "Female", "Married": "No", "Dependents": 2,
    "Education": "Not Graduate", "Self_Employed": "Yes",
    "ApplicantIncome": 1500, "CoapplicantIncome": 0,
    "LoanAmount": 200, "Loan_Amount_Term": 120,
    "Credit_History": 0, "Property_Area": "Rural",
}

print("STRONG:", predict_loan(strong))
print("WEAK:  ", predict_loan(weak))