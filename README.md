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

{
  "historical": {
      "2024-04-01": 10,
      "2024-04-02": 11,
      "2024-04-03": 14,
      "2024-04-04": 8,
      "2024-04-05": 15,
      "2024-04-06": 6,
      "2024-04-07": 11,
      "2024-04-08": 8,
      "2024-04-09": 3,
      "2024-04-10": 11,
      "2024-04-11": 9,
      "2024-04-12": 6,
      "2024-04-13": 19,
      "2024-04-14": 21,
      "2024-04-15": 6,
      "2024-04-16": 2,
      "2024-04-17": 9,
      "2024-04-18": 7,
      "2024-04-19": 8,
      "2024-04-20": 4,
      "2024-04-21": 20,
      "2024-04-22": 13,
      "2024-04-23": 1,
      "2024-04-24": 10,
      "2024-04-25": 8,
      "2024-04-26": 15,
      "2024-04-27": 14,
      "2024-04-28": 9,
      "2024-04-29": 12,
      "2024-04-30": 3
  },
  "start_date": "2024-05-10",
  "horizon": 7
}

cURL Command

curl -X POST "http://127.0.0.1:8000/forecasting" \
     -H "Content-Type: application/json" \
     -d '{
          "historical": {
              "2024-04-01": 10,
              "2024-04-02": 11,
              "2024-04-03": 14,
              "2024-04-04": 8,
              "2024-04-05": 15,
              "2024-04-06": 6,
              "2024-04-07": 11,
              "2024-04-08": 8,
              "2024-04-09": 3,
              "2024-04-10": 11,
              "2024-04-11": 9,
              "2024-04-12": 6,
              "2024-04-13": 19,
              "2024-04-14": 21,
              "2024-04-15": 6,
              "2024-04-16": 2,
              "2024-04-17": 9,
              "2024-04-18": 7,
              "2024-04-19": 8,
              "2024-04-20": 4,
              "2024-04-21": 20,
              "2024-04-22": 13,
              "2024-04-23": 1,
              "2024-04-24": 10,
              "2024-04-25": 8,
              "2024-04-26": 15,
              "2024-04-27": 14,
              "2024-04-28": 9,
              "2024-04-29": 12,
              "2024-04-30": 3
          },
          "start_date": "2024-05-10",
          "horizon": 7
     }'


Example Response

{"forecast":{"2024-05-10":9.666666666666666,"2024-05-11":12.333333333333334,"2024-05-12":16.666666666666668,"2024-05-13":10.333333333333334,"2024-05-14":2.0,"2024-05-15":9.5,"2024-05-16":7.5}}


 Troubleshooting

If you get an error on docker build, ensure you have Docker installed and running.

If curl returns an error, try accessing http://localhost:8000/docs to check API functionality.


