import os
import requests

from wallpapr.config import Config


def ensure_download_dir(config: Config):
    print("Making sure download directory exists...")
    download_path = config.download_path
    os.makedirs(download_path, exist_ok=True)

    return download_path


def download_image(config: Config, url: str, file_path: str):
    print("Downloading image...")
    try:
        params = {
            "w": config.width,
            "h": config.height,
        }

        image_data = requests.get(url, params=params, stream=True)

        with open(file_path, "wb") as img:
            for chunk in image_data.iter_content(chunk_size=1024):
                img.write(chunk)
        return True
    except Exception as e:
        print("Error occurred while downloading.", e)
        return False
