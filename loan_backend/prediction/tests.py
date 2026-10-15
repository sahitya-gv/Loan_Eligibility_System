

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from ml.predictor import MODEL, predict_loan

STRONG = {
    "Gender": "Male", "Married": "Yes", "Dependents": "0",
    "Education": "Graduate", "Self_Employed": "No",
    "ApplicantIncome": 6000, "CoapplicantIncome": 2000,
    "LoanAmount": 120, "Loan_Amount_Term": 360,
    "Credit_History": 1, "Property_Area": "Urban",
}

WEAK = {
    "Gender": "Female", "Married": "No", "Dependents": "2",
    "Education": "Not Graduate", "Self_Employed": "Yes",
    "ApplicantIncome": 1500, "CoapplicantIncome": 0,
    "LoanAmount": 200, "Loan_Amount_Term": 120,
    "Credit_History": 0, "Property_Area": "Rural",
}


class PredictionTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_model_loads(self):
        self.assertIsNotNone(MODEL)

    def test_valid_request_returns_all_fields(self):
        r = self.client.post("/api/predict/", STRONG, format="json")
        self.assertEqual(r.status_code, 200)
        for key in ["status", "confidence", "risk_level", "recommendation"]:
            self.assertIn(key, r.json())

    def test_missing_field_returns_400(self):
        data = dict(STRONG)
        del data["Gender"]
        r = self.client.post("/api/predict/", data, format="json")
        self.assertEqual(r.status_code, 400)

    def test_invalid_value_returns_400(self):
        data = dict(STRONG, ApplicantIncome=-5)
        r = self.client.post("/api/predict/", data, format="json")
        self.assertEqual(r.status_code, 400)

    def test_strong_and_weak_differ(self):
        self.assertEqual(predict_loan(STRONG)["status"], "Approved")
        self.assertEqual(predict_loan(WEAK)["status"], "Rejected")