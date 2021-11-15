from wallpapr.config import Config
from wallpapr.image_providers.base_provider import BaseImageProvider
from wallpapr.image_providers.unsplash import UnsplashImageProvider


IMAGE_PROVIDERS = {"unsplash": UnsplashImageProvider}


def resolve_image_provider(config: Config) -> BaseImageProvider:
    if config.image_provider in IMAGE_PROVIDERS.keys():
        return IMAGE_PROVIDERS[config.image_provider](config.image_provider_config)

    raise ValueError(
        f"Unknown image provider: {config.image_provider}. Supported values: {IMAGE_PROVIDERS.keys()}"
    )
