import os
from ImagePainter import ImagePainter


IMAGE_DIR = '/Users/Jonathan/Documents/ProgrammingProjects/image_feedback/images/'
INPUT_IMAGE_DIR = os.path.join(IMAGE_DIR, 'input_images')
OUTPUT_IMAGE_DIR = os.path.join(IMAGE_DIR, 'output_images')

def paint_image(input_filename, output_filename):
    input_filepath = os.path.join(INPUT_IMAGE_DIR, demo_input_filename)
    output_filepath = os.path.join(OUTPUT_IMAGE_DIR, demo_output_filename)
    imcontainer = ImagePainter(demo_input_filepath)
    
    imcontainer.monet(demo_output_filepath)



def demo():
    paint_image('Red_sunset.png', 'Red_sunset_monet.png')




if __name__=="__main__":
    demo()
