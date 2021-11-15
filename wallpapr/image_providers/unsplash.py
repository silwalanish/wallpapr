import os
import requests
from typing import Tuple, Union
from wallpapr.utils.download import download_image

from wallpapr.utils.unsplash import get_query_params
from wallpapr.image_providers.base_provider import BaseImageProvider

BASE_API_URL = "https://api.unsplash.com"
RANDOM_IMAGE_API_ENDPOINT = "/photos/random"

UNSPLASH_ACCESS_KEY = os.environ["UNSPLASH_ACCESS_KEY"]
UNSPLASH_SECRET_KEY = os.environ["UNSPLASH_SECRET_KEY"]


class UnsplashImageProvider(BaseImageProvider):
    def get_headers(self):
        return {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}

    def get_random_image(self) -> Tuple[str, str, str]:
        print("Getting random wallpaper to download...")
        try:
            api_url = BASE_API_URL + RANDOM_IMAGE_API_ENDPOINT

            params = get_query_params(self.config)
            print("API Params: ", params)

            req = requests.get(api_url, headers=self.get_headers(), params=params)

            if req.status_code == 200:
                result = req.json()
                return (
                    result["id"],
                    result["urls"]["regular"],
                    result["links"]["download_location"],
                )
            else:
                return (None, None, None)
        except Exception as e:
            print("Error occurred while fetching random image.", e)
            return (None, None, None)

    def trigger_download_endpoint(self, download_endpoint: str):
        requests.get(download_endpoint, headers=self.get_headers())

    def download_random_image(
        self, width: int, height: int, download_path: str
    ) -> Union[str, None]:
        print("Downloading image...")

        params = {
            "w": width,
            "h": height,
        }

        image_id, image_url, download_endpoint = self.get_random_image()

        if image_id and image_url:
            new_wallpaper_path = os.path.join(download_path, f"{image_id}.jpg")

            download_image(image_url, new_wallpaper_path, params)
            self.trigger_download_endpoint(download_endpoint)

            return new_wallpaper_path

        return None
