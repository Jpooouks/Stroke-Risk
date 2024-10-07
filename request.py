import requests

url = "http://127.0.0.1:1234/predict"

input_data = {
    "data": {
    'gender': ['Female'],  
    'age': [48.0],
    'hypertension': [0],
    'heart_disease': [0],
    'ever_married': ['Yes'],
    'work_type': ['Private'],
    'Residence_type': ['Urban'],
    'avg_glucose_level': [69.21],
    'bmi': [33.1],
    'smoking_status': ['never smoked']
    }
}

response = requests.post(url, json=input_data)

print("Status code:", response.status_code)
print("Response:", response.json())