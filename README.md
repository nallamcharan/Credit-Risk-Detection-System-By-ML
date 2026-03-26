# 🔐Problem Statement : 
Some of the customers  get loans from finance companies  and they do not pay back .So that ,business will get  into financial loses.companies can be safe if they colud predict whether the customer will pack loan amount or not.

# 🎯 Objective  :
Build a End to End  credit risk detection system web app  for production ready by using PIPELINE..

It should detect whether the customer will pay back or not before accepting loan

Deploy it into online by using flask for credit risk checking through web interface 

# Demo Result
<img width="1036" height="941" alt="Screenshot 2026-03-26 203708" src="https://github.com/user-attachments/assets/fec179a7-8360-42e7-9ce4-4df41955f5e9" />
<img width="1208" height="697" alt="Screenshot 2026-03-26 203817" src="https://github.com/user-attachments/assets/a1f1e2d3-7e4d-4205-a611-7d6caa4736d5" />


# Data Set Overview:

A realestic dataset that contains transactions related to real time bank transactions with 30000 records 

Following are the columns of the data set

(['Age', 'Gender', 'EmploymentYears', 'HomeOwnership', 'MaritalStatus',
       'AnnualIncome', 'LoanAmount', 'LoanTermMonths', 'CreditScore',
       'NumCreditCards', 'DebtToIncomeRatio', 'PreviousDefaults', 'Default'],dtype='object')
Credit Default prediction 0.5

# 🪜 Approach :

I followed   random forest classifier model to develop this detection system .

# Step-1: importing required libraries and Data collection 

  Pandas ,  Numpy , matplotlib ,  seaborn,  sklearn , imblearn , flask

# Step-2 : Data understanding

  info(), head() , tail(), describe () , .columns

# Step-3 : Data Prepocessing 

   checkinmg null values df.isnull().sum() 

   Handling missing values

   Type conversions
   
# Step-4 : Exploratory Data Analysis 

   Here i performed univariate and bivariate and trivariate analysis through using matplotlib , seabron 
   
  countplot() , heatmap() , barplot() , pairplot()

# Step-4 : Feature Engineering

  label encoding (), one hot coding () or categorical data encoding 

  feature scaling for good model performance

  feature selection 

  chronological splitting (train,split,test)
  
  defing data types for pipeline 
   
# Step -5 : Model Selection 

  RandomForestClassifier(class_weight = 'balanced', n_estimators=100,max_depth = 10, random_state = 42)

# Step-6 : Pipeline building for automating the predictions

  ColumnTransformer () # for auto encoding and featiure scaling 

  SMOTE() # for handing imbalanced data 
  
  sklearn.pipeline.Pipeline ()

# step -6.1 Hyper Parameter Tuning : 

   girdsearchcv() for good hyper parameters and improve model peroformance
  
# Step-7 : Model Training

  model_pipeline.fit()  #training model by using pipeline

# Step-8 : Prediction Of Test Data 

  model_pipeline.predict() # prediction of test data by using predict()

# Step-9 : Model Evaluation 

  accuracy_score(), Classifiacation_report () , roc_auc () ,confusion_matrix() 

  cross validation score 

  Feature Importances 

  Shap Values 

   
# Step-10 : Model Saving 

  Used joblib/pickle to save developed model 
  
# Step-10 : Model Deployment 

  Used Flask API to connect home page and result page.

  Developed two websites by using HTML called Home and Result pages and designed them using CSS.
  
  Conneted two websited by using flask api 
  

# ➡️ Ultimately the model generated 

  ("# 80% Accuracy ") which means 80% of cusotmers are going pay back money but 20 % are credit defaults (not pay back)

  Roc_auc ( 80 %) 
  
# Approaches I Followed To Increase model performace And Imporve Recall : 

  1-class weights 

 2- SMOTING() (Handling imbalance data through using imblearn.over_sapmling.SMOTE())



 # 📈 Impact of this system on business 

  Credit defaulters can be catch easily.so that,they can reject loans of credit defaulters

  Business financial losses can decrease 

  Business growth would increase 

 

   
  

 




      


