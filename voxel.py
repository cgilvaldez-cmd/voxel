# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 21:00:50 2025

@author: Carlos Gil
"""

import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
            
# Load a NIfTI file
file= 'sub-01_task-rest_bold.nii'
nifti_img = nib.load(file)
datos= nifti_img.get_fdata()

print(datos.shape)
i0= 20
j0=30
k0= 20

vol= datos[:,:,:, 30]

sagital= vol[i0, :, :]
coronal= vol[:, j0, :]
axial= vol[:, :, k0]

img= np.zeros((99, 99)) 
img[0:64, 0:64] = axial
img[0:64, 64:] = coronal
img[64:, :64] = np.rot90(sagital)

# Crear figura
fig, ax = plt.subplots()
im = ax.imshow(img, cmap='gray')
plt.title("Vista: (axial, coronal, sagital)")

# Crear texto para mostrar coordenadas
texto = ax.text(0.02, 0.98, '', color='yellow',
                transform=ax.transAxes, va='top', fontsize=10,
                bbox=dict(facecolor='black', alpha=0.5))

# Función que se ejecuta al mover el mouse
def mostrar_coordenadas(event):
    if event.inaxes == ax:
        x, y = int(event.xdata), int(event.ydata)
        texto.set_text(f"x={x}, y={y}")
    else:
        texto.set_text('')

# Conectar el evento al movimiento del ratón
fig.canvas.mpl_connect('motion_notify_event', mostrar_coordenadas)

   
plt.imshow(img)
plt.axis('on')
plt.show()
