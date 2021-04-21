import PIL
from PIL import Image
import argparse

import traceback
#TODO support commandline arguments

"""parser = argparse.ArgumentParser(description="A script to convert and output images to ascii")
parser.add_argument("-i","--image_path",help="The path to the image file, any supported by PIL will work")
args = parser.parse_args()"""


ASCII_CHARS = ["@","#","S","%","|",".",":","\'","!","?",";"]


def resize_image(image, new_width = 100):
    width,height = image.size
    ratio = height/width / 1.65
    new_height = int(new_width * ratio)
    resize_image = image.resize((new_width,new_height))
    return(resize_image)


def grayify(image):
    greayscale_image = image.convert("L")
    return greayscale_image


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)


def main(input_image):
    #print(args.image_path)
    """if(input_image == None):
        path = input("Enter Image name:\n") 
        try:
            image = PIL.Image.open(path)
        except Exception:
            traceback.print_exc()
            print(path," Incorrect Format, please enter an actual image file")
            return
    else:
        image = input_image
    """
    image = input_image
    new_width=100
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[i:(i+new_width)] for i in range(0,pixel_count,new_width)])

    print(ascii_image)
    #with open("ascii_image.txt","w") as f:
    #    f.write(ascii_image)


