from typing import Any


def utils_handler(func):
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            raise

    return inner_func


def db_handler(func):
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            raise

    return inner_func


def dao_handler(func):
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            raise

    return inner_func


def controllers_handler(func):
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            raise

    return inner_func


def routers_handler(func):
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            return ex

    return inner_func
