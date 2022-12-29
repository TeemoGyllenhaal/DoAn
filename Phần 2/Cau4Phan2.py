import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
def do_thi_yen_ngua(x, y):
    z = (x/3)**2 - (y/2)**2
    return z

def do_thi_mat_hyperbolic_1(x,y):
    z1 = 2 * (np.sqrt((x/3)**2+(y/5)**2-1) )
    return z1
def do_thi_mat_hyperbolic_2(x,y):
    z2 = -2 * (np.sqrt((x/3)**2+(y/5)**2-1) )
    return z2

def do_thi_mat_cau_1(x,y):
    z1 = np.sqrt(4-(x+2)**2-(y-1)**2)+4
    return z1
def do_thi_mat_cau_2(x,y):
    z1 = -np.sqrt(4-(x+2)**2-(y-1)**2)+4
    return z1

def du_lieu(a,b):
    x = np.linspace(start=a, stop=b,num=3000)
    return x


def ve_do_thi_1(x,y):
    x, y = np.meshgrid(x, y)
    z = do_thi_yen_ngua(x,y)
    fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
    rosen_surf = ax.plot_surface(x, y,z,cmap=cm.viridis,linewidth=0, antialiased=False)
    fig.colorbar(rosen_surf, shrink=0.5,aspect=5)
    plt.show()
    
def ve_do_thi_2(x,y):
    x, y = np.meshgrid(x, y)
    z1 = do_thi_mat_hyperbolic_1(x,y)
    z2 = do_thi_mat_hyperbolic_2(x,y)
    fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
    rosen_surf_1 = ax.plot_surface(x, y,z1, cmap=cm.viridis,linewidth=0, antialiased=False)
    fig.colorbar(rosen_surf_1, shrink=0.5,aspect=5)
    rosen_surf_2 = ax.plot_surface(x, y,z2, cmap=cm.viridis,linewidth=0, antialiased=False)
    fig.colorbar(rosen_surf_2, shrink=0.5,aspect=5)
    plt.show()
    
def ve_do_thi_3(x,y):
    x, y = np.meshgrid(x, y)
    z1 = do_thi_mat_cau_1(x,y)
    z2 = do_thi_mat_cau_2(x,y)
    fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
    rosen_surf_1 = ax.plot_surface(x, y,z1, cmap=cm.viridis,linewidth=0, antialiased=False)
    fig.colorbar(rosen_surf_1, shrink=0.5,aspect=5)
    rosen_surf_2 = ax.plot_surface(x, y,z2, cmap=cm.viridis,linewidth=0, antialiased=False)
    fig.colorbar(rosen_surf_2, shrink=0.5,aspect=5)
    plt.show()
    
    
def main():
    x = du_lieu(-6,6)
    y = du_lieu(-6,6)
    ve_do_thi_1(x,y)
    
    x1 = du_lieu(-10,10)
    y1 = du_lieu(-10,10)
    ve_do_thi_2(x1,y1)
    
    x2 = du_lieu(-4,0)
    y2 = du_lieu(-1,3)
    ve_do_thi_3(x2,y2)
    
    
    
if __name__ == "__main__":
    main()