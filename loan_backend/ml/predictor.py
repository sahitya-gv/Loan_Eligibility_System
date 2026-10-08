import joblib
import pandas as pd
from pathlib import Path
from .features import add_features

MODEL = joblib.load(Path(__file__).parent / "loan_model.pkl")


def build_recommendation(data, approved, risk):
    tips = []
    total_income = data["ApplicantIncome"] + data.get("CoapplicantIncome", 0)
    monthly_emi = data["LoanAmount"] * 1000 / data["Loan_Amount_Term"]

    if data["Credit_History"] == 0:
        tips.append("Improve your credit history before reapplying.")
    if monthly_emi > 0.4 * total_income:
        tips.append("Consider a smaller loan amount or a longer repayment term.")
    if data.get("CoapplicantIncome", 0) == 0 and total_income < 4000:
        tips.append("Adding a co-applicant with income may improve eligibility.")
    if approved and not tips:
        tips.append("Your profile looks strong. You are likely eligible.")
    if not approved and not tips:
        tips.append("Review your details and try again later.")
    return tips


def predict_loan(data: dict) -> dict:
    data = dict(data)
    data["Dependents"] = str(data["Dependents"])      # model expects text: "0","1","2","3"
    df = add_features(pd.DataFrame([data]))

    prob = float(MODEL.predict_proba(df)[0][1])       # chance of approval
    approved = prob >= 0.5
    confidence = round((prob if approved else 1 - prob) * 100, 2)

    if prob >= 0.75:
        risk = "Low"
    elif prob >= 0.5:
        risk = "Medium"
    else:
        risk = "High"

    return {
        "status": "Approved" if approved else "Rejected",
        "confidence": confidence,
        "risk_level": risk,
        "recommendation": build_recommendation(data, approved, risk),
    }