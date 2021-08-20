from loader import dp
from .throttling import ThrottlingMiddleware


if __name__ == '__middlewares__':
    dp.middleware.setup(ThrottlingMiddleware())


def setup(dp):
    return None

def shutdown(dp):
    return None