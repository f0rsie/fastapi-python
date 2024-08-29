class DbUnavailableError(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class DbAddError(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
