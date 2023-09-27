from flask import Flask, render_template, url_for, request
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return render_template("Front.html")


@app.route("/Heart")
def Heart():
    return render_template("Heart.html")


@app.route("/about")
def about():
    return render_template("about.html")


def getParameters():
    # parameters = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    global parameters
    if request.method == "POST":
        gender = request.form['gender']
        age = request.form['age']  # sort
        marital = request.form['marital']
        ethnicity = request.form['ethnicity']
        bmi = request.form['bmi']
        smoke = request.form['smoke']
        sports = request.form['sports']
        health = request.form['health']
        walk = request.form['walk']
        physical_health = request.form['physical_health']
        stroke = request.form['stroke']
        attack = request.form['attack']
        kidney = request.form['kidney']
        other_cancer = request.form['other_cancer']
        lungs = request.form['lungs']
        skin_cancer = request.form['skin_cancer']
        depression = request.form['depression']
        asthma = request.form['asthma']
        mental_health = request.form['mental_health']

        gender1 = 0
        age1 = 0
        marital1 = 0
        ethnicity1 = 0
        bmi1 = 0
        smoke1 = 0
        sports1 = 0
        health1 = 0
        walk1 = 0
        physical_health1 = 0
        stroke1 = 0
        attack1 = 0
        kidney1 = 0
        other_cancer1 = 0
        lungs1 = 0
        skin_cancer1 = 0
        depression1 = 0
        asthma1 = 0
        mental_health1 = 0

        if gender == 'Male-1':
            gender1 = 1
        elif gender == 'Female-2':
            gender1 = 2

        if age == '18 <= AGE <= 24 --- 1':
            age1 = 1
        elif age == '25 <= AGE <= 34 --- 2':
            age1 = 2
        elif age == '35 <= AGE <= 44 --- 3':
            age1 = 3
        elif age == '45 <= AGE <= 54 --- 4':
            age1 = 4
        elif age == '55 <= AGE <= 64 --- 5':
            age1 = 5
        elif age == '64 <= AGE  --- 5':
            age1 = 6

        if marital == 'Married-1':
            marital1 = 1
        elif marital == 'Divorced-2':
            marital1 = 2
        elif marital == 'Widowed-3':
            marital1 = 3
        elif marital == 'Separated-4':
            marital1 = 4
        elif marital == 'Never Married-5':
            marital1 = 5
        elif marital == 'A member of an unmarried couple-6':
            marital1 = 6

        if ethnicity == 'white-1':
            ethnicity1 = 1
        elif ethnicity == 'Black-2':
            ethnicity1 = 2
        elif ethnicity == 'Asian-3':
            ethnicity1 = 3
        elif ethnicity == 'American Indian-4':
            ethnicity1 = 4
        elif ethnicity == 'Hispanic--5':
            ethnicity1 = 5
        elif ethnicity == 'others--6':
            ethnicity1 = 6

        if bmi == '1-UnderWeight BMI':
            bmi1 = 1.0
        elif bmi == '2-Normal Weight':
            bmi1 = 2.0
        elif bmi == '3-OverWeight':
            bmi1 = 3.0
        elif bmi == '4-OverWeight':
            bmi1 = 4.0

        if smoke == '1-Smoke Every Day':
            smoke1 = 1
        elif smoke == '2-Smoke Some day':
            smoke1 = 2
        elif smoke == '3-Former Smoker':
            smoke1 = 3
        elif smoke == '4-Never Smoked':
            smoke1 = 4

        if sports == 'Yes-1':
            sports1 = 1
        elif sports == 'No-2':
            sports1 = 2

        if health == 'Excellent-1':
            health1 = 1
        elif health == 'Very Good-2':
            health1 = 2
        elif health == 'Good-3':
            health1 = 3
        elif health == 'Fair-4':
            health1 = 4
        elif health == 'Poor-5':
            health1 = 5
        if walk == 'Yes-1':
            walk1 = 1
        elif walk == 'No-2':
            walk1 = 2

        # <!-- _PHYS14D -->

        if stroke == 'Yes-1':
            stroke1 = 1
        elif stroke == 'No-2':
            stroke1 = 2

        if attack == 'Yes-1':
            attack1 = 1
        elif attack == 'No-2':
            attack1 = 2
        if kidney == 'Yes-1':
            kidney1 = 1

        elif kidney == 'No-2':
            kidney1 = 2

        if other_cancer == 'Yes-1':
            other_cancer1 = 1
        elif other_cancer == 'No-2':
            other_cancer1 = 2

        if lungs == 'Yes-1':
            lungs1 = 1
        elif lungs == 'No-2':
            lungs1 = 2

        if skin_cancer == 'Yes-1':
            skin_cancer1 = 1
        elif skin_cancer == 'No-2':
            skin_cancer1 = 2

        if depression == 'Yes-1':
            depression1 = 1
        elif depression == 'No-2':
            depression1 = 2

        if asthma == 'Yes-1':
            asthma1 = 1
        elif asthma == 'No-2':
            asthma1 = 2

        if mental_health == 'Yes-1':
            mental_health1 = 1
        elif mental_health == 'No-2':
            mental_health1 = 2

        parameters = [age1, health1, attack1, physical_health1, walk1, marital1, ethnicity1,
                      sports1, smoke1, lungs1, gender1, stroke1, bmi1, kidney1, skin_cancer1,
                      other_cancer1, depression1, asthma1, mental_health1]
    print(parameters)
    return parameters


@app.route("/submit", methods=['POST'])
def predict():
    model = open("model.pkl", "rb")
    clr = joblib.load(model)
    if request.method == 'POST':
        parameter = getParameters()
        inputfeature = np.asarray(parameter).reshape(1, -1)
        my_prediction = clr.predict(inputfeature)
    return render_template('resultdisplay.html', prediction=int(my_prediction[0]))


if __name__ == '__main__':
    app.run(debug=True)
