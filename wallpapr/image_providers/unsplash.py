import os
import requests
from typing import Tuple

from wallpapr.utils.unsplash import get_query_params
from wallpapr.image_providers.base_provider import BaseImageProvider

BASE_API_URL = "https://api.unsplash.com"
RANDOM_IMAGE_API_ENDPOINT = "/photos/random"

UNSPLASH_ACCESS_KEY = os.environ["UNSPLASH_ACCESS_KEY"]
UNSPLASH_SECRET_KEY = os.environ["UNSPLASH_SECRET_KEY"]


class UnsplashImageProvider(BaseImageProvider):
    def get_random_image(self) -> Tuple[str, str]:
        print("Getting random wallpaper to download...")
        try:
            api_url = BASE_API_URL + RANDOM_IMAGE_API_ENDPOINT

            headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}

            params = get_query_params(self.config)
            print("API Params: ", params)

            req = requests.get(api_url, headers=headers, params=params)

            if req.status_code == 200:
                result = req.json()
                return (result["id"], result["urls"]["regular"])
            else:
                return (None, None)
        except Exception as e:
            print("Error occurred while fetching random image.", e)
            return (None, None)
