import os
import json
from typing import Any, Dict

HOME_PATH = os.path.expanduser("~")
CONFIG_PATH = os.path.join(HOME_PATH, ".config/wallpaper")
WALLPAPER_CONFIG_PATH = os.path.join(CONFIG_PATH, "wallpaper.json")

DEFAULT_IMAGE_PROVIDER_CONFIG = {
    "orientation": "landscape",
    "collections": [
        {
            "id": "606028",
            "url": "https://unsplash.com/collections/606028/technology",
        },
        {
            "id": "11649432",
            "url": "https://unsplash.com/collections/11649432/landscape",
        },
        {
            "id": "827743",
            "url": "https://unsplash.com/collections/827743/landscape",
        },
        {
            "id": "2476111",
            "url": "https://unsplash.com/collections/2476111/retro-tech",
        },
    ],
}


class Config:
    width: int
    height: int
    current_wallpaper_path: str
    download_path: str
    image_provider: str
    image_provider_config: Dict[str, Any]

    def __init__(self, **params) -> None:
        self.width = params.get("width", 1360)
        self.height = params.get("height", 768)
        self.current_wallpaper_path = params.get("current_wallpaper_path", "")
        self.download_path = params.get(
            "download_path", os.path.join(HOME_PATH, "Pictures")
        )
        self.image_provider = params.get("image_provider", "unsplash")
        self.image_provider_config = params.get(
            "image_provider_config",
            DEFAULT_IMAGE_PROVIDER_CONFIG,
        )

    def toJSON(self):
        return {
            "width": self.width,
            "height": self.height,
            "current_wallpaper_path": self.current_wallpaper_path,
            "download_path": self.download_path,
            "image_provider": self.image_provider,
            "image_provider_config": self.image_provider_config,
        }

    @classmethod
    def ensure_config_dir(cls):
        print("Making sure config directory exists...")
        os.makedirs(CONFIG_PATH, exist_ok=True)

    @classmethod
    def read(cls):
        print("Reading config...")

        try:
            with open(WALLPAPER_CONFIG_PATH, "r") as f:
                return Config(**json.load(f))
        except:
            pass
        return Config()

    def save(self):
        print("Saving config...")
        with open(WALLPAPER_CONFIG_PATH, "w") as f:
            json.dump(self.toJSON(), f, indent=2)
