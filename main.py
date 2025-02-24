from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
import statistics

app = FastAPI()

class ForecastRequest(BaseModel):
    historical: dict[str, float]
    start_date: str
    horizon: int

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

def generate_forecast(historical, start_date, horizon):
    historical_data = {parse_date(k): v for k, v in historical.items()}
    forecast = {}
    
    current_date = parse_date(start_date)
    
    for _ in range(horizon):
        weekday = current_date.weekday()
        past_values = []
        
        for i in range(1, 5):
            past_date = current_date - timedelta(weeks=i)
            if past_date in historical_data:
                past_values.append(historical_data[past_date])
        
        if past_values:
            predicted_value = statistics.mean(past_values)
        else:
            predicted_value = 0  # Default in case of missing data
        
        forecast[current_date.strftime("%Y-%m-%d")] = predicted_value
        historical_data[current_date] = predicted_value  # Use forecasted value for future predictions
        current_date += timedelta(days=1)
    
    return forecast

@app.post("/forecasting")
def forecasting(request: ForecastRequest):
    forecast = generate_forecast(request.historical, request.start_date, request.horizon)
    return {"forecast": forecast}
