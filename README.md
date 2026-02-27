# Problem Statement :: Some customers  get loans from finance companies  and they do not pay back .so that ,business will get  into financial loses.

# Object ::

Build a credit risk detection system using random forest classifier and i should detect whether the customer will pay back or not before accepting loan

Deploy it into online by using flask

# Data Set Overview:

A realestic dataset that contains transactions related to real time bank transactions with 30000 records 

Following are the columns of the data set

(['Age', 'Gender', 'EmploymentYears', 'HomeOwnership', 'MaritalStatus',
       'AnnualIncome', 'LoanAmount', 'LoanTermMonths', 'CreditScore',
       'NumCreditCards', 'DebtToIncomeRatio', 'PreviousDefaults', 'Default'],dtype='object')
Credit Default prediction 0.5

# Approach ::

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
  
# Step-7 : Model Trianing

  model_pipeline.fit()  #training model by using pipeline

# Step-8 : Prediction Of Test Data 

  model_pipeline.predict() # prediction of test data by using predict()

# Step-9 : Model Evaluation 

  accuracy_score(), Classifiacation_report () , roc_auc () ,confusion_matrix() 

  cross validation score 

# ➡️ Ultimately the model generated 

  ("# 80% Accuracy ") which means 80% of cusotmers are going pay back money but 20 % are credit defaults (not pay back)

  Roc_auc ( 80 %) 
  
Approaches I Followed To Increase model performace And Imporve Recall : 

  1-class weights 

  2- SMOTING() (Handling imbalance data through using imblearn.over_sapmling.SMOTE())



 # 📈 Impact of this system on business 

  Credit defaulters can be catch easily.so that,they can reject loans of credit defaulters

  Business financial losses can decrease 

  Business growth would increase 

 

   
  

 




      


