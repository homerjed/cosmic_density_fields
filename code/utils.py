import os
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from mpl_toolkits.axes_grid1 import make_axes_locatable


normalize = lambda x: (x - x.min()) / (x.max() - x.min())


def plot_wireframe(ax):
  # terrifying function to plot the edges of a cube.
  Z = 1.1 * np.array([[-1,+1,-1], [+1,+1,-1], 
                      [+1,-1,-1], [-1,-1,-1], 
                      [-1,+1,+1], [+1,+1,+1], 
                      [+1,-1,+1], [-1,-1,+1]])
  verts = [[Z[0],Z[1],Z[2],Z[3]],
           [Z[4],Z[5],Z[6],Z[7]],
           [Z[0],Z[1],Z[5],Z[4]],
           [Z[2],Z[3],Z[7],Z[6]], 
           [Z[1],Z[2],Z[6],Z[5]],
           [Z[4],Z[7],Z[3],Z[0]]] # return verts
  ax.add_collection3d(
      Poly3DCollection(
          verts, 
          facecolors=(0.,0.,0.,0.),
          linewidths=1., 
          edgecolors='k'
      )
  )

    
def plot_points(ax, points):
    x, y, z = points.T
    p = ax.scatter(x, y, z, c='royalblue', s=1.0, alpha=0.5)
    ax.axis('off')
    ax.dist = 10.0
    
    
def plot_grid(ax, grid):
    line = np.linspace(-1.0, 1.0, grid.shape[0])
    mesh = np.meshgrid(line, line, line)
    mesh = np.vstack(map(np.ravel, mesh)).T
    cube = np.concatenate((mesh, grid.reshape(-1,1)), axis=1)
    
    x, y, z, c = cube.T
    p = ax.scatter(x, y, z, c=c, cmap='gray_r', s=0.05, alpha=0.5) 
    ax.axis('off')
    ax.dist = 10.0

    
def plot_3d(R):
  # show the sphere in three-dimensional space
  fig = plt.figure(figsize=(2.,2.), dpi=400)

  ax1 = fig.add_subplot(111, projection='3d')
  # ax1.set_title('training', y=1.05)
  plot_wireframe(ax1)
  plot_grid(ax1, R)
    

def upscale(x, factor):
    up_x = np.zeros((factor * x.shape[0], factor * x.shape[1]))[::]
    return up_x
