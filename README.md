📈 Time Series Forecasting API

🚀 Overview

This project is a proof-of-concept web service for time series forecasting using a simple moving average of past 4 weeks' values on the same weekday. It is built with FastAPI and can be containerized using Docker. The forecasted values themselves are used to recursively generate future forecasts within the requested horizon.

Data Assumptions:

Daily, Contiguous Data: Historical data is expected to have no missing dates.
At Least 4 Weeks of History: This ensures there is enough data (4 same-weekday values) to compute meaningful forecasts.

Valid Inputs: This proof of concept assumes the request payload is valid (no checks for erroneous dates, negative horizons, etc.)


Forecasting Logic


1.Same-Weekday Average: For each forecast date, the model looks back 1, 2, 3, and 4 weeks (same weekday) to retrieve those values.

2.Recursive Forecasting: Each newly predicted value is added to the “historical” dataset so that future forecast dates can use it.

3.Default Handling: If there are fewer than 4 past values available (e.g., at the beginning), it defaults to 0.

Example:

If you’re forecasting 2024-05-01, it looks at 2024-04-24, 2024-04-17, 2024-04-10, and 2024-04-03.

The forecast is the average of those values. Once you forecast 2024-05-01, its predicted value will be used for forecasting 2024-05-08.


🛠 Setup Instructions

 Run with Docker

Build the Docker Image

docker build -t forecasting-api .

Run the Container

docker run -p 8000:8000 forecasting-api


🔥 API Usage

Endpoint

POST /forecasting

Accepts JSON payload containing:

historical: A dictionary of past date-value pairs.

start_date: The first date for the forecast.

horizon: Number of days to forecast (inclusive)

Example Request


curl -X POST "http://localhost:8000/forecasting" -H "Content-Type: application/json" -d @Data.json

Example Response
{"forecast":{"2024-05-01":11.0,"2024-05-02":8.0,"2024-05-03":11.0,"2024-05-04":10.75,"2024-05-05":15.25,"2024-05-06":9.75,"2024-05-07":2.25,"2024-05-08":10.25,"2024-05-09":8.0,"2024-05-10":10.0,"2024-05-11":11.9375,"2024-05-12":16.3125,"2024-05-13":10.1875,"2024-05-14":2.0625,"2024-05-15":10.0625,"2024-05-16":7.75,"2024-05-17":11.0,"2024-05-18":10.171875,"2024-05-19":15.140625,"2024-05-20":11.234375,"2024-05-21":2.078125,"2024-05-22":10.328125,"2024-05-23":7.9375,"2024-05-24":11.75,"2024-05-25":11.71484375,"2024-05-26":13.92578125,"2024-05-27":10.79296875,"2024-05-28":2.34765625,"2024-05-29":10.41015625,"2024-05-30":7.921875}}



 Troubleshooting

If you get an error on docker build, ensure you have Docker installed and running.

If curl returns an error, try accessing http://localhost:8000/docs to check API functionality.


