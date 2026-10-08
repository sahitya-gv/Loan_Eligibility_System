import time

t0 = time.time()
from ml.predictor import predict_loan
print("Model load time: %.2f seconds" % (time.time() - t0))

sample = {
    "Gender": "Male", "Married": "Yes", "Dependents": "0",
    "Education": "Graduate", "Self_Employed": "No",
    "ApplicantIncome": 6000, "CoapplicantIncome": 2000,
    "LoanAmount": 120, "Loan_Amount_Term": 360,
    "Credit_History": 1, "Property_Area": "Urban",
}

predict_loan(sample)   # first call warms things up, not counted

n = 100
t0 = time.time()
for _ in range(n):
    predict_loan(sample)
total = time.time() - t0

print("%d predictions took %.2f seconds" % (n, total))
print("Average per prediction: %.1f ms" % (total / n * 1000))