from sklearn.base import BaseEstimator, TransformerMixin

class MoreThanTwoFeature(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        age_condition = X['age'] > 40
        heart_disease_condition = X['heart_disease'] == 1
        hypertension_condition = X['hypertension'] == 1
        glucose_condition = X['avg_glucose_level'] > 126
        smoked_condition = X['smoking_status'] == 'formerly smoked'

        X['more_than_two'] = (
            age_condition.astype(int) 
            + heart_disease_condition.astype(int) 
            + hypertension_condition.astype(int) 
            + glucose_condition.astype(int) 
            + smoked_condition.astype(int)
        ) > 2 

        X['more_than_two'] = X['more_than_two'].astype(int)
        
        return X