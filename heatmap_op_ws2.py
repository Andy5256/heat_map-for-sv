#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as mtransforms
import matplotlib.colors as colors
points = np.arange(-5,5,0.1)
xs,ys = np.meshgrid(points,points)
# z1 = np.loadtxt("shiftvec_333_100_op_hdch.dat")
# z = np.loadtxt("shiftvec_111_100_op_4315.dat") # sc for GeS
z = np.loadtxt("shiftvec_ws2_222_op.dat") # sc for WS2
# z = np.transpose(z1)+z2
# nkp = 100
fig = plt.figure()
ax = fig.add_subplot(111)
# ax.imshow(z,cmap=plt.cm.seismic,interpolation='bicubic',vmin=-100,vmax=100)
def do_plot(ax, Z, transform):
    im = ax.imshow(Z,cmap=plt.cm.summer,interpolation='none',
    norm=colors.SymLogNorm(linthresh=0.1,linscale=1,vmin=-9,vmax=0.9))
    trans_data = transform + ax.transData
    im.set_transform(trans_data)
    ax.set_xlim(-5, 150)
    ax.set_ylim(-5, 150)
    # fig.colorbar(im, ax, extend='both')
# image skew
do_plot(ax, z, mtransforms.Affine2D().skew_deg(15, 15))

plt.show()
# plt.savefig("sv_ws2_222_op.png")
# plt.close()