from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import MediaGroupFilter
from aiogram.types.input_media import InputMediaPhoto

from typing import List
from loader import dp


@dp.message_handler(MediaGroupFilter(is_media_group=True), content_types=types.ContentType.ANY)
async def handle_albums(messages: List[types.Message]):
   
    media_group = types.MediaGroup()
    caption = messages.caption
    first_element=True
    
    for photo in messages.photo:
        if first_element:
            media_group.attach_photo(types.InputMediaPhoto(media=photo.file_id, caption=caption))
            first_element=False
        else:    
            media_group.attach_photo(types.InputMediaPhoto(media=photo.file_id))

    await messages.answer_media_group(media=media_group)