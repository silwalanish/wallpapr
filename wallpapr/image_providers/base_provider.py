from typing import Any, Dict, Tuple


class BaseImageProvider:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    def get_random_image(self) -> Tuple[str, str]:
        raise NotImplementedError("get_random_image is not implemented yet.")
