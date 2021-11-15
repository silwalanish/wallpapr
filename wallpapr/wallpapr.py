import os
import argparse

from wallpapr.config import Config
from wallpapr.utils.download import ensure_download_dir
from wallpapr.image_providers import IMAGE_PROVIDERS, resolve_image_provider
from wallpapr.utils.bg import (
    get_current_background_path,
    set_background_picture,
    clean_old_wallpaper,
)


def parse_cli_arguments():
    parser = argparse.ArgumentParser(
        description="Downloads a random picture and updates the wallpaper."
    )

    parser.add_argument(
        "-c",
        "--get-current-path",
        help="Get the current background path.",
        action="store_true",
    )

    parser.add_argument(
        "-s",
        "--only-set-current",
        help="Set the current background without downloading.",
        action="store_true",
    )

    parser.add_argument(
        "-p",
        "--image-provider",
        choices=set(IMAGE_PROVIDERS.keys()),
        help=f"Set the image provider to use.",
    )

    return parser.parse_args()


def main():
    args = parse_cli_arguments()

    Config.ensure_config_dir()
    config = Config.read()

    if args.get_current_path:
        print(f"Current Background Path: {get_current_background_path()}")
        return

    if args.only_set_current:
        set_background_picture(config.current_wallpaper_path)
        return

    if args.image_provider:
        config.image_provider = args.image_provider

    download_path = ensure_download_dir(config)
    image_provider = resolve_image_provider(config)

    new_wallpaper_path = image_provider.download_random_image(
        config.width, config.height, download_path
    )

    if new_wallpaper_path:
        set_background_picture(new_wallpaper_path)

        clean_old_wallpaper(config)

        config.current_wallpaper_path = new_wallpaper_path
        config.save()
