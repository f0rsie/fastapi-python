class ServiceUnavailableError(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UrlFileNotFound(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
