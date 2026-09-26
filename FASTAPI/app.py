from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated
import pandas as pd
import pickle

#import the ml model
with  open ('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

tier1_cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Pune']
tier2_cities = ['Jaipur', 'Lucknow', 'Kanpur', 'Nagpur', 'Indore', 'Thane', 'Bhopal', 'Visakhapatnam', 'Pimpri-Chinchwad', 'Patna', 'Vadodara', 'Ghaziabad', 'Ludhiana', 'Agra', 'Nashik', 'Faridabad', 'Meerut', 'Rajkot', 'Kalyan-Dombivli', 'Vasai-Virar', 'Varanasi', 'Srinagar', 'Dhanbad', 'Jabalpur', 'Amritsar', 'Navi Mumbai', 'Allahabad', 'Ranchi', 'Howrah', 'Coimbatore', 'Jodhpur', 'Gwalior', 'Vijayawada', 'Madurai', 'Raipur', 'Kota', 'Guwahati', 'Chandigarh', 'Solapur', 'Hubli-Dharwad', 'Mysore', 'Tiruchirappalli', 'Bareilly', 'Aligarh', 'Tiruppur', 'Jalandhar', 'Bhubaneswar', 'Salem', 'Warangal', 'Mira-Bhayandar', 'Thiruvananthapuram', 'Bhiwandi', 'Saharanpur']

# pydantic model to validate incoming data
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the person in years")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the person in kg")]
    height: Annotated[float, Field(..., gt=0, description="Height of the person in cm")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Income of the person in LPA")]
    smoker: Annotated[bool, Field(..., description="Whether the person is a smoker or not")]
    city: Annotated[str, Field(..., description="City of the person ")]
    occupation: Annotated[Literal["retired", "freelancer", "student",'government_job','business_owner','unemployed','private_job'], Field(..., description="Occupation of the person")]
    
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return 'High'
        elif self.smoker or self.bmi > 27:
            return 'Medium'
        else:
            return 'Low'

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return 'young'
        elif self.age < 45:
            return 'Young Adult'
        elif self.age < 60:
            return 'middle_aged'
        else:
            return 'Senior'

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier1_cities:
            return 1
        elif self.city in tier2_cities:
            return 2
        else:
            return 3
      
@app.post("/predict")
async def predict_premium(data: UserInput):
    input_df = pd.DataFrame([{
    
    'age': data.age,
    'weight': data.weight,
    'height': data.height,
    'income_lpa': data.income_lpa,
    'smoker': data.smoker,
    'city_tier': data.city_tier,
    'occupation': data.occupation,
    
  }])

    prediction = model.predict(input_df)[0]
    return JSONResponse(status_code=200, content={"predicted_category": prediction})