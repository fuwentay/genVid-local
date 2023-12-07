import json
from base64 import b64decode
from pathlib import Path
import json
import openai
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Generates file saved as json
def get_image(prompt):
    DATA_DIR = Path("/tmp/responses")

    DATA_DIR.mkdir(exist_ok=True)

    openai.api_key = os.environ.get('openai_api_key')

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="b64_json",
    )

    # file_name = DATA_DIR / f"{prompt[:5]}-{response['created']}.json"
    file_name = DATA_DIR / f"{prompt[:10]}.json"

    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(response, file)
    
    time.sleep(12)

# get_image("conspiracy theory crop circles humans")

# Decode all json to png
def decode_json():
    DATA_DIR = Path("/tmp/responses")
    IMAGE_DIR = Path("/tmp/images")

    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    for json_file in Path(DATA_DIR).glob("*.json"):
        with open(json_file, mode="r", encoding="utf-8") as file:
            response = json.load(file)

        for index, image_dict in enumerate(response["data"]):
            image_data = b64decode(image_dict["b64_json"])
            image_file = IMAGE_DIR / f"{json_file.stem}.png"
            with open(image_file, mode="wb") as png:
                png.write(image_data)

# decode_json()