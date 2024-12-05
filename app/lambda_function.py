import os
import json
from app.config import get_config

def lambda_handler(event, context):
    config = get_config()
    environment = os.environ.get("ENV", "unknown")
    label = os.getenv('LABEL', 'No label defined')
    print(f"Running in environment: ===> {environment}")
    
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Hello from {environment} enviroment! LABEL: {label}",
            "db_host": config['db_host'],
            "api_url": config['api_url'],
            "input": event
        })
    }
    
    return response
