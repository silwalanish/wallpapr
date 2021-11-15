import os
from gi.repository import Gio
from wallpapr.config import Config

GTK_BACKGROUND_SCHEMA = "org.gnome.desktop.background"
GTK_BACKGROUND_SCHEMA_KEY_PICTURE_URI = "picture-uri"


def get_current_background_path() -> str:
    gsettings = Gio.Settings.new(GTK_BACKGROUND_SCHEMA)
    return Gio.File.new_for_uri(
        gsettings.get_string(GTK_BACKGROUND_SCHEMA_KEY_PICTURE_URI)
    ).get_path()


def set_background_picture(path: str) -> None:
    print("Setting wallpaper...")
    gsettings = Gio.Settings.new(GTK_BACKGROUND_SCHEMA)
    wallpaper_uri = Gio.File.new_for_path(path).get_uri()
    gsettings.set_string(GTK_BACKGROUND_SCHEMA_KEY_PICTURE_URI, wallpaper_uri)


def clean_old_wallpaper(config: Config) -> None:
    print("Cleaning old wallpaper...")
    path = config.current_wallpaper_path
    if path and os.path.exists(path):
        os.remove(path)
