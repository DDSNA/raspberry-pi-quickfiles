from datetime import datetime

import requests
import pandas as pd
import numpy as np

import logging

logging.basicConfig(level=logging.DEBUG)

def download_dataset(type: str):
    import requests
    import pandas as pd
    import numpy as np
    url = "http://eve.danserban.ro/call-fuzz"
    if type == "csv":
        response = requests.get(url)
        logging.debug(response.status_code)
        logging.debug(response.text)
        print(response.status_code)
        df = pd.DataFrame(response.json())
        df.to_csv("dataset.csv", index=False)
        print(df.head())
        
    elif type == "parquet":
        response = requests.get(url)
        logging.debug(response.status_code)
        df = pd.DataFrame(response.json())
        for col in df.columns:
            if df[col].dtype == 'object':  # Check if the column is of object type (strings)
                try:
                    df[col] = pd.to_numeric(df[col], errors='coerce')  # Attempt to convert to numeric, coercing errors
                except ValueError:
                    print(f"Failed to convert {col} to numeric.")
        df.to_parquet("dataset.parquet")
        parse_parquet()

def parse_parquet():
    import pandas as pd
    df = pd.read_parquet("dataset.parquet")
    print(df.head())

download_dataset("csv")

download_dataset("parquet")