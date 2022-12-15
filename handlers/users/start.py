from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import MediaGroupFilter
from aiogram.types.input_media import InputMediaPhoto

from typing import List
import logging

from add_watermark import watermark_photo
from loader import dp



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    


@dp.message_handler(text='/a')
async def show_almul(message: types.Message):

    media_group = types.MediaGroup()

    file_id_1='AgACAgIAAxkBAAIB62OZ8EohkOqGuAd6lWAfGLipfaoLAALbxjEbO_bQSAWJjiZSW7eIAQADAgADcwADLAQ'
    file_id_2='AgACAgIAAxkBAAIB62OZ8EohkOqGuAd6lWAfGLipfaoLAALbxjEbO_bQSAWJjiZSW7eIAQADAgADeAADLAQ'
    caption = "FFFFFFFF"
    
    media_group.attach_photo(types.InputMediaPhoto(media=file_id_2, caption=caption))
    media_group.attach_photo(types.InputMediaPhoto(media=file_id_1))


    await dp.bot.send_media_group(chat_id=312897103,media=media_group)



# @dp.message_handler(MediaGroupFilter(is_media_group=True), content_types=types.ContentType.ANY)
# async def handle_albums(messages: List[types.Message]):
    
#     #Represents a photo to be sent.
#     # medias = InputMediaPhoto()
#     #Helper for sending media group
#     media_group = types.MediaGroup()
#     print(media_group)
#     print("---------------")
#     print(messages)
#     print("---------------")

#     await types.ChatActions.upload_photo()

#     # print(messages)
#     # print(type(messages))

#     # TODO
#     # 1. Get photos and caption
#     # 2. Edit all photos
#     # 3. Create InputMediaPhoto with caption    
#     # 4. Use sendMediaGroup() where media = InputMediaPhoto 

#     # user_id = messages.from_user.id

#     # 1. Get photos and caption
#     photos_file_id = []
#     caption = messages.caption

#     print("-------INFO-------")
#     print(f"pics {len(messages.photo)}\n ids: \n")

#     for photo in messages.photo:
#         print(photo.file_id)
#         print('\n')


#     print(caption)
#     print()

#     first_element=True
    
#     for photo in messages.photo:
#         if first_element:
#             print(f'add first file_id \n {photo.file_id} \n')
#             media_group.attach_photo(types.InputMediaPhoto(media=photo.file_id, caption=caption))
#             first_element=False
#         else:    
#             print(f'add file_id {photo.file_id} \n')
#             media_group.attach_photo(types.InputMediaPhoto(media=photo.file_id))
        

#     print(media_group)

#     await messages.answer_media_group(media=media_group)








@dp.message_handler(MediaGroupFilter(is_media_group=True), content_types=types.ContentType.ANY)
async def handle_albums(msg: types.Message, messages: List[types.Message]):
    media_group = types.MediaGroup()

    print(f'message: \n{msg} \n\nalbum:{messages}\n')
    first_element=True

    for message in messages:
        if first_element:
            file_id = message.photo[-1].file_id
            try:
                media_group.attach_photo(photo=file_id,caption=message.caption)
            except: ValueError             
            first_element=False
        else:
            file_id = message.photo[-1].file_id
            try:
                media_group.attach_photo(photo=file_id)
            except: ValueError

    print(f'\n\nmedia_group: ({type(media_group)}) \n ---------- \n{media_group}\n\n')
    # await msg.answer_media_group(msg.from_user.id, media=media_group)
    await dp.bot.send_media_group(msg.from_user.id, media=media_group)


@dp.message_handler(content_types=['photo'])
async def menu_setting_ser_photo(message : types.Message):
    
    print(message.photo[0].file_id)
    file_id = message.photo[0].file_id
    text = message.caption
    print(text)
    print("-----------------")

    caption = message.caption if message.caption != None else None
    
    await message.photo[-1].download('data/pics/photos/'+str(file_id)+".jpg")

    await message.answer("Editing your pictures...")

    input_image_path='data/pics/photos/'+str(file_id)+".jpg"
    output_image_folder='data/pics/photos/'
    watermark_image_path='data/pics/Group_34550.png'


    res = watermark_photo(
        input_image_path,
        output_image_folder,
        watermark_image_path
    )

    photo = open(res, 'rb')

  
    await dp.bot.send_photo(
        message.from_user.id,
        photo=photo,
        caption=caption)



    