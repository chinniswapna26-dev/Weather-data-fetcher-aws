# Weather Data Fetcher

A serverless application that fetches current weather data daily and stores it in a database for later analysis.

## AWS Services Used
- AWS Lambda
- Amazon DynamoDB
- Amazon EventBridge Scheduler
- AWS IAM

## External API
- OpenWeather API

## How It Works
1. EventBridge Scheduler triggers the Lambda function daily.
2. The Lambda function fetches current weather data from the OpenWeather API.
3. The function stores the weather information in the WeatherData DynamoDB table.
4. Stored data includes city, temperature, humidity, weather condition, and timestamp.

## Configuration
- City: Bangalore
- DynamoDB Table: WeatherData
- Environment Variable: OPENWEATHER_API_KEY

## Security
The OpenWeather API key is stored as an AWS Lambda environment variable and is not included in the source code.
