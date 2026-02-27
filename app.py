from flask import Flask , render_template,request,url_for
import joblib
import pandas as pd 

app = Flask(__name__)
model = joblib.load('developedmodel.pk1')

@app.route("/")
def run():
    return render_template("home.html")

#prediction 
@app.route("/",methods  = ["POST","GET"])
def prediction():
    age  = float(request.form['age'])
    gender  = request.form['gender']
    employment_years  = float(request.form['emp_years'])
    annual_salary = float(request.form['a_s'])
    credit_score  = float(request.form['c_s'])
    loan_amount  = float(request.form['l_a'])
    loan_term_months = int(request.form['loan_term_months'])

    new_data  = {"Age":age,
                 "Gender":gender,
                 "AnnualIncome":annual_salary,
                 "CreditScore":credit_score,
                 "EmploymentYears":employment_years,
                 "LoanAmount":loan_amount,
                 'LoanTermMonths':loan_term_months
    }
    new_data = pd.DataFrame([new_data])
    
    pred_result  = model.predict(new_data)
    print(pred_result)
    probability = model.predict_proba(new_data)[0][1] * 100
    print(probability)

    return render_template('result.html',result  = pred_result,probability=round(probability),
                           Age  =age ,Gender=gender,Annual_Income=annual_salary,
                           Employment_years=employment_years,
                           Credit_Score= credit_score,Loan_Amount=loan_amount,
                           Loan_Term_Months=loan_term_months
                           )

if __name__ == "__main __":
    app.run(debug = True)


if __name__ == "__main__":
    app.run(debug=True)