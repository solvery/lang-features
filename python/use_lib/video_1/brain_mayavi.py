"""
Animation of a head slicing.

Based on a BSD-like licenced code by Gael Varoquaux
http://docs.enthought.com/mayavi/mayavi/auto/example_mri.html

Result:
http://i.imgur.com/EJZELfi.gif
"""

from urllib import urlretrieve # to download the data
import tarfile # to uncompress the data
import numpy as np # to load the data
from mayavi import mlab # to plot the data
import moviepy.editor as mpy # to animate the data

# DOWNLOAD THE DATA AND LOAD IT IN THE RAM

name = "MRbrain.tar.gz"
urlretrieve("http://graphics.stanford.edu/data/voldata/"+name, name)

with tarfile.open(name) as f:
    data = np.array([np.fromstring(f.extractfile('MRbrain.%d'%i).read(),
                     dtype='>u2') for i in range(1, 110)])
data.shape = (109, 256, 256)
data = data.T

# MAKE THE FIGURE

fig = mlab.figure(bgcolor=(0, 0, 0), size=(250, 250))
src = mlab.pipeline.scalar_field(data)
src.spacing = [1, 1, 1.5]
src.update_image_data = True

blur = mlab.pipeline.user_defined(src, filter='ImageGaussianSmooth')
voi = mlab.pipeline.extract_grid(blur)
voi.set(x_min=125, x_max=193, y_min=92, y_max=125, z_min=34, z_max=75)

mlab.pipeline.iso_surface(voi, contours=[1610, 2480], colormap='Spectral')

thr = mlab.pipeline.threshold(src, low=1120)
plane = mlab.pipeline.scalar_cut_plane(thr, vmin=1400, vmax=2600,
                    plane_orientation='y_axes', colormap='black-white')
plane.implicit_plane.widget.enabled = False

voi = mlab.pipeline.extract_grid(src)
outer = mlab.pipeline.iso_surface(voi, contours=[1776,],color=(.8,.7,.6))

mlab.view(-125, 54, 326, (145.5, 138, 66.5))
mlab.roll(-175)

# ANIMATE WITH MOVIEPY

def make_frame(t):
    fig.scene.disable_render = True
    new_y = 50+12.5*t
    plane.implicit_plane.origin = (136, new_y+0.5, 82)
    voi.set(y_min=new_y)
    fig.scene.disable_render = False
    return mlab.screenshot(antialiased=True)

clip = mpy.VideoClip(make_frame, duration=6)
clip.write_gif('brain.gif', fps=10)