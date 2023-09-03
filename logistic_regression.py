import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

#sample dataset
credit_scores = np.random.randint(300, 850, size=1000)
loan_approved = np.random.binomial(1, p=1 / (1 + np.exp(-0.02 * (credit_scores - 700))), size=1000)

data = pd.DataFrame({
    'credit_score': credit_scores,
    'loan_approved': loan_approved
})

#print(data.head(20))

model = LogisticRegression()
model.fit(data[['credit_score']], data['loan_approved'])

try:
    new_customer_credit_score = input("Enter your credit score: ")
    new_customer_data = pd.DataFrame({'credit_score': [new_customer_credit_score]})
    predicted_class = model.predict(new_customer_data[['credit_score']])[0]

    # print the predicted class
    if predicted_class == 0:
        print(f'A loan is not approved for a customer with a credit score of {new_customer_credit_score}.')
    else:
        print(f'A loan is approved for a customer with a credit score of {new_customer_credit_score}.')
        
except Exception as e:
    print('ERROR: ' + str(e))
