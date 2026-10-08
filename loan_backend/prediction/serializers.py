from rest_framework import serializers


class LoanInputSerializer(serializers.Serializer):
    Gender = serializers.ChoiceField(["Male", "Female"])
    Married = serializers.ChoiceField(["Yes", "No"])
    Dependents = serializers.ChoiceField(["0", "1", "2", "3"])
    Education = serializers.ChoiceField(["Graduate", "Not Graduate"])
    Self_Employed = serializers.ChoiceField(["Yes", "No"])
    ApplicantIncome = serializers.FloatField(min_value=0)
    CoapplicantIncome = serializers.FloatField(min_value=0, default=0)
    LoanAmount = serializers.FloatField(min_value=1)
    Loan_Amount_Term = serializers.FloatField(min_value=1)
    Credit_History = serializers.ChoiceField([0, 1])
    Property_Area = serializers.ChoiceField(["Urban", "Semiurban", "Rural"])