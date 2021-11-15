from typing import Any, Dict, Union


class BaseImageProvider:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    def download_random_image(
        self, width: int, height: int, download_path: str
    ) -> Union[str, None]:
        raise NotImplementedError("download_image is not implemented yet.")
