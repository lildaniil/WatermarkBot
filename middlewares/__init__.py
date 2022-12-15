from aiogram import Dispatcher

from loader import dp

from .media_group import AlbumMiddleware
# from .throttling import ThrottlingMiddleware


if __name__ == "middlewares":
#     dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(AlbumMiddleware())
