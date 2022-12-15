from PIL import Image
import random
import os


def random_name(symbols=8):
    pas = 'processed_'
    for x in range(symbols):
        pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return pas

def watermark_photo(input_image_path,
                    output_image_folder,
                    watermark_image_path,
                    position=None):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)

    width, height = base_image.size
    wm_width, wm_height = watermark.size
        


    if position == 1:
        pixel_position = (width-wm_width,0)
    elif position == 2:
        pixel_position = (0,0)
    elif position == 3:
        pixel_position = (0,height-wm_height)
    else:
        pixel_position=(width-wm_width,height-wm_height)

    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, pixel_position, mask=watermark)
    # transparent.show()
    
    output_image_path = output_image_folder + random_name()+".png"

    transparent.save(output_image_path)

    print(" ----------")
    print("res:" + output_image_path)
    print(" ----------")

    return output_image_path

    
    # print("YN")
    # if input()=="Y":
    #     dir = output_image_folder
    #     for f in os.listdir(dir):
    #         os.remove(os.path.join(dir, f))
    # else: pass



input_image_path='data/pics/photos/photo_1.jpg'
output_image_folder='data/pics/photos/'
watermark_image_path='data/pics/Group_34550.png'



# watermark_photo(
#     input_image_path,
#     output_image_folder,
#     watermark_image_path
    
#     )