import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import Image


class ImagePainter:
    """
    Use PNG files.
    """
    
    def __init__(self, image_file_path):
        self.image_file_path = image_file_path
        self.original_image = mpimg.imread(image_file_path)
        self.image = self.original_image
        self.imshape = (self.image.shape[0], self.image.shape[1])  # pixel dimensions
        self.imchannels = self.image.shape[2]  # 1 if grayscale, 3 if RGB, 4 if RGBA
        self.coords_x, self.coords_y = np.meshgrid(range(self.imshape[0]), range(self.imshape[1]))

    def generate_distorted_mesh(self, sigma=.5):
        mesh_noise_x = np.random.normal(scale=sigma, size=self.imshape)
        mesh_noise_y = np.random.normal(scale=sigma, size=self.imshape)
        self.distorted_mesh = np.array([self.coords_x.transpose() + mesh_noise_x, self.coords_y.transpose() + mesh_noise_y])
    
    def distort_image(self):
        distorted_image = np.ones((self.imshape[0], self.imshape[1], self.imchannels))
        for channel in range(self.imchannels):
            ndimage.map_coordinates(self.image[:, :, channel], self.distorted_mesh, order=1, prefilter=False, output=distorted_image[:, :, channel])
        self.image = distorted_image
        
    def plot_image(self):
        self.fig = plt.figure()
        self.fig.show()
        self.implot = plt.imshow(self.image)
        self.implot.axes.set_xticks([])
        self.implot.axes.set_yticks([])
        plt.draw()
        
    def feedback(self):
        plt.clf()
        self.distort_image()
        self.implot = plt.imshow(self.image)
        self.implot.axes.set_xticks([])
        self.implot.axes.set_yticks([])
        plt.draw()

    def run_feedback_loop(self, max_iters=15):
        if max_iters == None:
            #ctrl+c to exit
            while True:
                self.feedback()
                print 'iter'
        else:
            iter = 1
            while iter <= max_iters:
                self.feedback()
                iter += 1

    def shrink_image(self):
        total_pixels =  np.prod(self.imshape)
        if total_pixels < 100000:
            return None
        else:
            self.scale_factor = np.sqrt(total_pixels / 100000.)
            img = Image.open(self.image_file_path)
            rsize = img.resize((img.size[0] / self.scale_factor, img.size[1] / self.scale_factor))
            #PIL returns 8 bit ints. Convert to floats scaled from 0 to 1:
            self.image = (1/255.) * np.asarray(rsize, dtype='float32')
            self.imshape = (self.image.shape[0], self.image.shape[1])
            self.imchannels = self.image.shape[2]
            self.coords_x, self.coords_y = np.meshgrid(range(self.imshape[0]), range(self.imshape[1]))

    def monet(self, out_filepath, plot_results=True):
        self.shrink_image()
        if plot_results == True:
            self.plot_image()
        self.generate_distorted_mesh(sigma=.5)
        self.run_feedback_loop()
        plt.savefig(out_filepath)






