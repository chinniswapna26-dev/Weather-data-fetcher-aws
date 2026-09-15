import json
import os
import boto3
import urllib.request
import uuid
from datetime import datetime, timezone

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("WeatherData")

API_KEY = os.environ["OPENWEATHER_API_KEY"]
CITY = "Bangalore"


def lambda_handler(event, context):
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={API_KEY}&units=metric"
    )

    with urllib.request.urlopen(url) as response:
        weather_data = json.loads(response.read().decode())

    item = {
        "record_id": str(uuid.uuid4()),
        "city": CITY,
        "temperature": str(weather_data["main"]["temp"]),
        "humidity": str(weather_data["main"]["humidity"]),
        "weather": weather_data["weather"][0]["description"],
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }
