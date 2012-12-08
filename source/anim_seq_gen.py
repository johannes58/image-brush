"""
a tool to generate a sequence of n different paintings from the same source image.
"""


import os
from ImagePainter import ImagePainter
from paint_image import INPUT_IMAGE_DIR, OUTPUT_IMAGE_DIR




def generate_animation_frame_sequence_from_still(input_filename, output_filepattern, n_frames):
    """
    generate_animation_frame_sequence_from_still(input_filename, output_filepattern, n_frames)
    """

    input_filepath = os.path.join(INPUT_IMAGE_DIR, input_filename)

    output_animation_dir = os.path.join(OUTPUT_IMAGE_DIR, output_filepattern.split('%s')[0])
    if os.path.exists(output_animation_dir) == False:
        os.mkdir(output_animation_dir)
    
    output_filenames = [output_filepattern % frame for frame in range(n_frames)]
    

    for o_fn in output_filenames:

        output_filepath = os.path.join(output_animation_dir, o_fn)
        ip = ImagePainter(input_filepath)
        ip.monet(output_filepath, plot_results=False)



def process_raw_frame_sequence(raw_frame_sequence_dir, output_filepattern)



if __name__ == '__main__':
    
    n = 30
    input_filename = 'abovetheclouds.png'
    output_filepattern = input_filename.split('.')[0] + '%s.png'
    generate_animation_frame_sequence_from_still(input_filename, output_filepattern, n)
