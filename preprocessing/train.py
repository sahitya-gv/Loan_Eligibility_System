import sys
sys.path.append("../loan_backend")

import pandas as pd
import joblib
from ml.features import add_features

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score, confusion_matrix)

# ---------- 1. Load and clean ----------
df = pd.read_csv("../dataset/Loan_Data.csv")
df["Loan_Status"] = df["Loan_Status"].replace("N/", "N").map({"Y": 1, "N": 0})
df["Dependents"] = df["Dependents"].replace("3+", "3")
df = df.drop(columns=["Loan_ID"]).drop_duplicates() ##
df = add_features(df)

print("Rows:", df.shape[0]) ##
print(df["Loan_Status"].value_counts())

# ---------- 2. Split ----------
X = df.drop(columns=["Loan_Status"])
y = df["Loan_Status"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# ---------- 3. Preprocessing (saved inside the model) ----------
num_cols = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount",
            "Loan_Amount_Term", "Credit_History",
            "TotalIncome", "EMI", "Income_to_Loan"]
cat_cols = ["Gender", "Married", "Dependents", "Education",
            "Self_Employed", "Property_Area"]

preprocess = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")),
                      ("sc", StandardScaler())]), num_cols),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                      ("oh", OneHotEncoder(handle_unknown="ignore"))]), cat_cols),
])

# ---------- 4. Train and tune 3 models ----------
candidates = {
    "Logistic Regression": (LogisticRegression(max_iter=1000),
                            {"model__C": [0.01, 0.1, 1, 10, 100]}),
    "Decision Tree": (DecisionTreeClassifier(random_state=42),
                      {"model__max_depth": [3, 5, 7],
                       "model__min_samples_leaf": [1, 5, 10]}),
    "Random Forest": (RandomForestClassifier(random_state=42),
                      {"model__n_estimators": [100, 200],
                       "model__max_depth": [4, 6, None]}),
}

results, fitted = [], {}
for name, (clf, grid) in candidates.items():
    pipe = Pipeline([("prep", preprocess), ("model", clf)])
    gs = GridSearchCV(pipe, grid, cv=5, scoring="roc_auc").fit(X_train, y_train)
    best = gs.best_estimator_
    pred = best.predict(X_test)
    proba = best.predict_proba(X_test)[:, 1]
    fitted[name] = best
    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, pred),
        "Precision": precision_score(y_test, pred),
        "Recall": recall_score(y_test, pred),
        "F1": f1_score(y_test, pred),
        "ROC_AUC": roc_auc_score(y_test, proba),
    })
    print("\n", name, "best settings:", gs.best_params_)
    print("Confusion matrix:\n", confusion_matrix(y_test, pred))

# ---------- 5. Compare and save the best ----------
results_df = pd.DataFrame(results).sort_values("ROC_AUC", ascending=False)
print("\n--- Model Comparison ---")
print(results_df.round(3).to_string(index=False))

best_name = results_df.iloc[0]["Model"]
joblib.dump(fitted[best_name], "../loan_backend/ml/loan_model.pkl")
print("\nSaved best model:", best_name)
