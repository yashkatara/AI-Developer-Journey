from  fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    # Load your data here
    with open('patients.json', 'r') as f:
      data = json.load(f)
    return data

@app.get("/")
async def root():
    return {"message": "patient management system"}
  
@app.get('/about')
async def about():
      return {"message": "A fully functiional API to manage your patients and their medical records."}
    
@app.get('/view')
async def view():
    data = load_data()
    return data  ;  
  
@app.get ('/patient/{patient_id}')
async def view_patient(patient_id: str):
    data = load_data()
    
    if patient_id in data:
     return data[patient_id]
    return {"message": "Patient not found"}