# -*- coding: utf-8 -*-
"""customer_churn.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1reTJY86Nqtt4Lhh2Y2NDYct79qWRuFrB

1. **`import pandas as pd`**:
   - This imports the **pandas** library, which is essential for data manipulation and analysis in Python. It helps you work with structured data, such as tables, by creating and manipulating **DataFrames** and **Series**.

2. **`from sklearn.model_selection import train_test_split`**:
   - This imports the **`train_test_split`** function from **scikit-learn (sklearn)**. It's used to split your dataset into two parts: training data and testing data. The training data is used to train your machine learning model, while the testing data is used to evaluate the model’s performance.

3. **`from sklearn.preprocessing import StandardScaler, LabelEncoder`**:
   - **`StandardScaler`**: A preprocessing tool that standardizes features by removing the mean and scaling them to unit variance. This is useful when your features have different ranges and you want to normalize them for better model performance.
   - **`LabelEncoder`**: This encodes categorical labels into numerical form (e.g., converting 'male' and 'female' to 0 and 1). It's used when machine learning algorithms require numerical input.

4. **`from sklearn.ensemble import RandomForestClassifier`**:
   - This imports the **RandomForestClassifier**, a machine learning algorithm used for classification tasks. It builds multiple decision trees and merges them to get a more accurate and stable prediction.

5. **`from sklearn.metrics import accuracy_score, classification_report, confusion_matrix`**:
   - **`accuracy_score`**: A function that calculates the accuracy of the model, which is the ratio of correctly predicted instances to the total instances.
   - **`classification_report`**: Provides a detailed report on precision, recall, F1-score, and support for each class in a classification problem.
   - **`confusion_matrix`**: A table used to evaluate the performance of a classification algorithm by comparing predicted and actual values, showing true positives, true negatives, false positives, and false negatives.

6. **`import numpy as np`**:
   - This imports **NumPy**, a library for numerical computing in Python. It's used to handle large multi-dimensional arrays and matrices, as well as perform mathematical operations on them.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

"""1. **`data = pd.read_csv(r'/content/Customer-Churn.csv')`**:
   - This line reads a CSV (Comma Separated Values) file named **Customer-Churn.csv** from the specified path (`/content/Customer-Churn.csv`) into a pandas DataFrame called **data**.
   - The `r` before the file path indicates a **raw string**, ensuring that any special characters (like `\`) in the file path are treated literally and not as escape characters.

2. **`print(data.head())`**:
   - The **`head()`** function displays the first 5 rows of the DataFrame (by default). It’s useful for getting a quick overview of the data structure, column names, and the first few entries.
   - This will output the top 5 rows of your **Customer-Churn** data.

3. **`print(data.isnull().sum())`**:
   - **`isnull()`** checks for missing values (NaNs) in each cell of the DataFrame.
   - **`sum()`** adds up the number of missing values per column.
   - This prints a count of the missing (null) values in each column of the DataFrame, helping you identify which columns have missing data.
"""

data = pd.read_csv(r'/content/Customer-Churn.csv')
print(data.head())
print(data.isnull().sum())

"""1. **`label_encoder = LabelEncoder()`**:
   - This creates an instance of **LabelEncoder**, which is a tool used to convert categorical labels (like text) into numerical values. This is important because many machine learning algorithms work better with numerical data rather than categorical data.

2. **The `for` loop**:
   - The loop iterates through a list of columns from your DataFrame `data` that contain categorical data, such as **'gender'**, **'Partner'**, **'InternetService'**, etc. These columns likely contain text labels that need to be transformed into numerical form.
   
3. **`data[column] = label_encoder.fit_transform(data[column])`**:
   - For each column in the list:
     - **`fit_transform()`** first fits the label encoder to the unique values in that column, then transforms these values into numeric labels (e.g., 'Male' -> 0, 'Female' -> 1).
     - It then assigns the transformed numeric labels back to the same column in the DataFrame.
   - For example, if the **'gender'** column has values 'Male' and 'Female', it will be encoded as `0` for 'Male' and `1` for 'Female' (or vice versa, depending on the order encountered by `fit_transform()`).

### Purpose:
- This step is **encoding categorical features** (those that are text-based) into numerical values to prepare them for machine learning algorithms. By converting them into numbers, the algorithm can process the data effectively.
"""

label_encoder = LabelEncoder()


for column in ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
                'PaperlessBilling', 'PaymentMethod', 'Churn']:
    data[column] = label_encoder.fit_transform(data[column])

"""1. **`X = data.drop(columns=['customerID', 'Churn'])`**:
   - This creates the **feature matrix** `X` by dropping the **'customerID'** and **'Churn'** columns from the DataFrame `data`.
   - The **`customerID`** column is likely a unique identifier for each customer, which doesn’t contribute to the prediction and could lead to overfitting if used.
   - The **`Churn`** column contains the target variable (whether the customer has churned or not), which is what we want to predict, so it’s excluded from `X` and stored in `y`.

2. **`y = data['Churn']`**:
   - This sets `y` as the **target variable** that the model will learn to predict. In this case, `y` contains the values from the **`Churn`** column, which are typically 0 or 1, indicating whether a customer has churned (left the service) or not.

### Purpose:
- **`X`** is the feature set that the machine learning model will use to learn patterns from (input data), and **`y`** is the target (output data) that the model will predict. This is a typical step in preparing data for a supervised machine learning task where you have a set of features and a corresponding target variable.
"""

X = data.drop(columns=['customerID', 'Churn'])
y = data['Churn']

"""1. **`X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)`**:
   - **`train_test_split()`** is a function that splits your data into two parts: one for training the model and one for testing the model.
   
   - **Parameters**:
     - **`X`**: The features or input data (without the target variable).
     - **`y`**: The target or output data (the `Churn` column in this case).
     - **`test_size=0.2`**: This specifies that 20% of the data will be reserved for testing, and the remaining 80% will be used for training. This ensures the model is trained on a large portion of the data and then tested on unseen data.
     - **`random_state=42`**: This is a seed used to ensure the data is split in the same way every time the code is run. Setting this parameter helps make the results reproducible.

2. **Output Variables**:
   - **`X_train`**: The training set of features.
   - **`X_test`**: The testing set of features.
   - **`y_train`**: The training set of target values (churn labels).
   - **`y_test`**: The testing set of target values (churn labels).

### Purpose:
- This step splits the data into training and testing sets so that the model can be trained on the **training data** (80%) and its performance can be evaluated on **unseen testing data** (20%). This helps ensure the model generalizes well to new, unseen data, which is critical in building reliable machine learning models.
"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""### 1. **Identify Columns with Object Data Types**:
   ```python
   object_columns = X_train.select_dtypes(include=['object']).columns
   ```
   - This line finds all columns in `X_train` that have the **data type `object`**, which usually indicates they contain strings or mixed types.
   - These columns could have issues like spaces, non-numeric values, or other formatting problems that need to be resolved before the data can be used in a machine learning model.

### 2. **Print Unique Values in Object Columns**:
   ```python
   for col in object_columns:
       print(f"Unique values in column '{col}': {X_train[col].unique()}")
   ```
   - This loop prints the **unique values** in each of the columns identified as having the `object` data type.
   - This helps you inspect and identify if there are any unexpected values (such as empty spaces or special characters) that could cause issues during model training.

### 3. **Handle Missing or Inconsistent Values in 'TotalCharges' Column**:
   ```python
   X_train['TotalCharges'] = X_train['TotalCharges'].replace(' ', np.nan).fillna(0)
   X_test['TotalCharges'] = X_test['TotalCharges'].replace(' ', np.nan).fillna(0)
   ```
   - Here, you focus on the `'TotalCharges'` column, assuming it's one of the columns with `object` data type.
   - **`replace(' ', np.nan)`**: Replaces any blank spaces (' ') in the column with `NaN` (Not a Number), marking them as missing values.
   - **`fillna(0)`**: Fills any missing values (NaNs) with `0`. This ensures that the column does not have any missing or non-numeric values.

### 4. **Convert Object Columns to Numeric**:
   ```python
   for col in object_columns:
       try:
           X_train[col] = pd.to_numeric(X_train[col])
           X_test[col] = pd.to_numeric(X_test[col])
       except ValueError:
           print(f"Could not convert column '{col}' to numeric.")
   ```
   - This loop attempts to convert each object-type column in both the training (`X_train`) and testing (`X_test`) sets into **numeric** form using `pd.to_numeric()`.
   - If a column contains non-numeric values that can't be converted (e.g., if there are strings or special characters), a **`ValueError`** is caught, and a message is printed to indicate the issue.

### 5. **Scale the Features**:
   ```python
   scaler = StandardScaler()
   X_train = scaler.fit_transform(X_train)
   X_test = scaler.transform(X_test)
   ```
   - **`StandardScaler()`**: Initializes a scaler that standardizes features by removing the mean and scaling them to unit variance. This ensures that the features are normalized, which is important for many machine learning algorithms.
   - **`fit_transform(X_train)`**: Fits the scaler to the training data and then transforms the data by scaling it.
   - **`transform(X_test)`**: Uses the same scaling parameters derived from the training data to transform the test data. This ensures consistency between the training and testing sets.

### Purpose:
- This step ensures that all features are numeric and properly scaled, which is critical for many machine learning algorithms. Handling missing values, converting data types, and scaling features are common preprocessing steps in machine learning pipelines.
"""

object_columns = X_train.select_dtypes(include=['object']).columns

for col in object_columns:
    print(f"Unique values in column '{col}': {X_train[col].unique()}")
X_train['TotalCharges'] = X_train['TotalCharges'].replace(' ', np.nan).fillna(0)
X_test['TotalCharges'] = X_test['TotalCharges'].replace(' ', np.nan).fillna(0)

for col in object_columns:
    try:
        X_train[col] = pd.to_numeric(X_train[col])
        X_test[col] = pd.to_numeric(X_test[col])
    except ValueError:
        print(f"Could not convert column '{col}' to numeric.")

# Now you can try scaling again
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

"""1. **`rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)`**:
   - This line initializes a **RandomForestClassifier**, which is a machine learning algorithm used for classification tasks.
   - **`n_estimators=100`**: Specifies the number of **decision trees** (100 in this case) to build in the random forest. The random forest classifier aggregates the predictions of these trees to make the final classification decision. More trees typically lead to a more robust and accurate model.
   - **`random_state=42`**: This sets a seed for the random number generator, ensuring that the results are reproducible. Using the same random state will produce the same random splits and model training each time the code is run.

2. **`rf_classifier.fit(X_train, y_train)`**:
   - This trains (or **fits**) the random forest classifier on the **training data**.
   - **`X_train`**: The training features (input data).
   - **`y_train`**: The corresponding target values (churn labels, in this case).
   - During this process, the algorithm builds multiple decision trees based on different subsets of the training data and features. Each tree makes a prediction, and the final model will aggregate these predictions (usually by majority vote) to classify new data points.

### Purpose:
- The **RandomForestClassifier** is being trained to learn patterns in the training data. By using multiple decision trees, the model can reduce overfitting and generalize well to unseen data. After training, the model will be ready to make predictions on new or test data.
"""

rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

rf_classifier.fit(X_train, y_train)

"""1. **`y_pred = rf_classifier.predict(X_test)`**:
   - This line uses the trained **RandomForestClassifier** model to make predictions on the **test data**.
   - **`X_test`**: The feature set from the test dataset, which the model has not seen before.
   - **`predict()`**: This method generates predictions based on the patterns learned during training. It applies the trained model to the test features and outputs the predicted class labels for each instance.

### Purpose:
- **`y_pred`** will contain the predicted labels for the test set, which you can compare to the actual labels (`y_test`) to evaluate the performance of your model. This allows you to assess how well the model generalizes to new, unseen data.
"""

y_pred = rf_classifier.predict(X_test)

"""1. **Calculate and Print Accuracy**:
   ```python
   accuracy = accuracy_score(y_test, y_pred)
   print(f'Accuracy: {accuracy:.2f}')
   ```
   - **`accuracy_score(y_test, y_pred)`**: Computes the accuracy of the model’s predictions by comparing the predicted values (`y_pred`) with the actual values (`y_test`). Accuracy is the proportion of correctly predicted instances out of the total instances.
   - **`print(f'Accuracy: {accuracy:.2f}')`**: Prints the accuracy value rounded to two decimal places. This gives a straightforward measure of how often the classifier is correct.

2. **Print Classification Report**:
   ```python
   print('Classification Report:')
   print(classification_report(y_test, y_pred))
   ```
   - **`classification_report(y_test, y_pred)`**: Generates a detailed report of classification metrics, including:
     - **Precision**: The ratio of true positive predictions to the total predicted positives. It measures how many of the predicted positives are actually positive.
     - **Recall**: The ratio of true positive predictions to the total actual positives. It measures how many of the actual positives were correctly predicted.
     - **F1-Score**: The harmonic mean of precision and recall. It provides a single metric that balances both precision and recall.
     - **Support**: The number of true instances for each label.
   - This report provides a comprehensive view of the classifier's performance across different classes.

3. **Print Confusion Matrix**:
   ```python
   print('Confusion Matrix:')
   print(confusion_matrix(y_test, y_pred))
   ```
   - **`confusion_matrix(y_test, y_pred)`**: Computes the confusion matrix, which shows the counts of true positive, true negative, false positive, and false negative predictions.
     - **True Positives (TP)**: Correctly predicted positive instances.
     - **True Negatives (TN)**: Correctly predicted negative instances.
     - **False Positives (FP)**: Instances incorrectly predicted as positive.
     - **False Negatives (FN)**: Instances incorrectly predicted as negative.
   - This matrix helps visualize how the model's predictions compare to the actual values and identify areas where the model might be making errors.

### Purpose:
- These metrics are used to evaluate and interpret the performance of the classification model. Accuracy gives an overall performance measure, while the classification report and confusion matrix provide more detailed insights into how well the model performs across different classes.
"""

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Classification report
print('Classification Report:')
print(classification_report(y_test, y_pred))

print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

"""1. **Prepare a Single Instance for Prediction**:
   ```python
   single_instance = X_test[0].reshape(1, -1)
   ```
   - **`X_test[0]`**: This selects the first instance (row) from the test dataset `X_test`.
   - **`reshape(1, -1)`**: Reshapes this single instance into a 2D array with one row and as many columns as needed. This is necessary because the `predict()` method expects a 2D array, even if you’re predicting for just one sample.

2. **Predict the Class for the Single Instance**:
   ```python
   single_prediction = rf_classifier.predict(single_instance)
   print(f'Predicted class for the single instance: {single_prediction[0]}')
   ```
   - **`rf_classifier.predict(single_instance)`**: Uses the trained model to predict the class label for the single instance. The result is an array with the predicted class label.
   - **`single_prediction[0]`**: Extracts the predicted class label from the array and prints it.

3. **Get the Probability for Each Class**:
   ```python
   single_proba = rf_classifier.predict_proba(single_instance)
   print(f'Probability for each class: {single_proba}')
   ```
   - **`rf_classifier.predict_proba(single_instance)`**: Calculates the probability of each class for the single instance. The result is an array where each element is a list of probabilities corresponding to each class.
   - **`print(f'Probability for each class: {single_proba}')`**: Prints the probability values for each class. This shows how confident the model is about the prediction.

### Purpose:
- **`predict()`** provides the final class label for the instance, which tells you the model’s prediction for that sample.
- **`predict_proba()`** gives the probability distribution across all possible classes, allowing you to understand how confident the model is in its prediction. This can be useful for assessing the certainty of the predictions and making decisions based on probability thresholds.
"""

single_instance = X_test[0].reshape(1, -1)
single_prediction = rf_classifier.predict(single_instance)
print(f'Predicted class for the single instance: {single_prediction[0]}')
single_proba = rf_classifier.predict_proba(single_instance)
print(f'Probability for each class: {single_proba}')

