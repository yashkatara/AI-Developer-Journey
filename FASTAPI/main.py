from  fastapi import FastAPI, HTTPException,Path, Query
from fastapi.responses import JSONResponse
import json
from typing import Annotated, Literal, Optional
from pydantic import BaseModel, Field, computed_field;

app = FastAPI()

class Patient(BaseModel):
    id : Annotated[str, Field(..., description="Unique identifier for the patient", example="P001")]
    name: Annotated[str, Field(..., description="Name of the patient", example="John Doe")]
    city: Annotated[str, Field(..., description="City of the patient", example="New York")]
    age: Annotated[int, Field(..., description="Age of the patient", example=30)]
    gender: Annotated[Literal['Male', 'Female', 'Other'], Field(..., description="Gender of the patient", example="Male")]
    height: Annotated[float, Field(...,gt=0, description="Height of the patient in cm", example=175.5)]
    weight: Annotated[float, Field(...,gt=0, description="Weight of the patient in kg", example=70.0)]
    @computed_field
    @property
    def bmi(self) -> float:
       bmi = round(self.weight / ((self.height / 100) ** 2), 2)
       return bmi
     
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity" 
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default = None)]
    city: Annotated[Optional[str], Field(default = None)]
    age: Annotated[Optional[int], Field(default = None)]
    gender: Annotated[Optional[Literal['Male', 'Female', 'Other']], Field(default = None)]
    height: Annotated[Optional[float], Field(default = None, gt=0)]
    weight: Annotated[Optional[float], Field(default = None, gt=0),]
def load_data():
    # Load your data here
    with open('patients.json', 'r') as f:
      data = json.load(f)
    return data
def save_data(data):
    # Save your data here
    with open('patients.json', 'w') as f:
        json.dump(data, f, indent=4)
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
  
@app.get('/patient/{patient_id}/records')
async def view_patient_records(patient_id: str = Path(...,description = 'ID of the patient in DB', example='P001')):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id].get('records', [])
    return {"message": "Patient not found"}  
@app.get('/sort')
async def sort_patients(sort_by: str = Query(..., description="Sort patients by height,width or bmi"), order:str = Query(..., description="Order of sorting: asc or desc")):
    valid_feilds = ['height', 'weight', 'bmi']
    if sort_by not in valid_feilds:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid fields are: {', '.join(valid_feilds)}")
      
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Valid orders are: asc or desc")  
    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=(order == sort_order))
    return sorted_data  
  
  
@app.post('/create')
async def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    
    data[patient.id] = patient.model_dump(exclude=['id'])
    # data[patient.id] = patient.dict()
    
    save_data(data)
    
    return JSONResponse(status_code=201, content={"message": "Patient created successfully", "patient": patient.model_dump()})
    
    # return {"message": "Patient created successfully", "patient": patient.dict()}
    
@app.put('/edit/{patient_id}')
async def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    existing_patient_info = data[patient_id]
    updated_patient_info= patient_update.model_dump(exclude_unset=True)
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value
    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)
    existing_patient_info=patient_pydantic_obj.model_dump(exclude="id")
    data[patient_id] = existing_patient_info  
    # data[patient_id] = patient_update.model_dump(exclude=['id'])
    save_data(data)
    
    return JSONResponse(status_code=200, content={"message": "Patient updated successfully", "patient": patient_update.model_dump()})
@app.delete('/delete/{patient_id}')
async def delete_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    del data[patient_id]
    save_data(data)
    
    return {"message": "Patient deleted successfully"}    