from flask import Flask, render_template, request, redirect
import pickle
import pandas as pd

app = Flask(__name__)

filename = "models/model.pkl"
model = pickle.load(open(filename, "rb"))

@app.route("/")
def index():
    return render_template("index.html") 

@app.route('/predict', methods=['GET', 'POST'])
def home():
    df = pd.DataFrame(columns=['Age', 'Diabetes', 'BloodPressureProblems',
            'AnyTransplants','AnyChronicDiseases','Height','Weight','KnownAllergies',
            'HistoryOfCancerInFamily','NumberOfMajorSurgeries'])

    if request.method == "POST":
        age = request.form["age"]
        diabetes = request.form["diabetes"]
        blood = request.form["blood"]
        transplant = request.form["transplant"]
        disease = request.form["disease"]
        height = request.form["height"]
        weight = request.form["weight"]
        allergies = request.form["allergies"]
        cancer = request.form["cancer"]
        ns = request.form["ns"]

        df = df.append({'Age': age,'Diabetes': diabetes, 'BloodPressureProblems': blood,
        'AnyTransplants': transplant,'AnyChronicDiseases': disease,
        'Height': height,'Weight': weight,'KnownAllergies': allergies,
        'HistoryOfCancerInFamily': cancer,'NumberOfMajorSurgeries': ns}, ignore_index=True)
        
    pred = int(model.predict(df))
    return render_template('result.html', pred=pred)

if __name__ == "__main__":
    app.debug=True
    app.run()