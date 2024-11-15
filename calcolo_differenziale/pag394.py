from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np 
import time

def Dtime(start):
    print("--- %s seconds ---" % (time.time() - start))

def plt_parameters():
    plt.rcParams['text.usetex'] = True #using latex
    params = {'font.size': 20, 'text.latex.preamble' : r"""
    \usepackage{amsmath} 
    \usepackage{amssymb}
    \usepackage{mathtools}
              
    \everymath{\displaystyle}
    """}
    #font size
    pyplot.rcParams.update(params)

def axis_limits(ax1, xmin, xmax, ymin, ymax):
    # Set identical scales for both axes
    ax1.set(xlim=(xmin, xmax), ylim=(ymin, ymax))

def set_position(ax1):
    # Set bottom and left spines as x and y axes of coordinate system
    ax1.spines['bottom'].set_position('zero')
    ax1.spines['left'].set_position('zero')

def remove_axes(ax1, *args):
    # Remove top and right spines
    if "n" in args or "N" in args: 
        ax1.spines['top'].set_visible(False)
    if "e" in args or "E" in args: 
        ax1.spines['right'].set_visible(False)
    if "s" in args or "S" in args: 
        ax1.spines['bottom'].set_visible(False)
    if "w" in args or "W" in args: 
        ax1.spines['left'].set_visible(False)

def x_y_axis_labels(ax1, args):
    # Create 'x' and 'y' labels placed at the end of the axes
    if "n" in args or "N" in args: 
        ax1.set_ylabel('$y$', labelpad=-21, y=1.02, rotation=0)
    if "e" in args or "E" in args: 
        ax1.set_xlabel('$x$', labelpad=-24, x=1.03)
    if "s" in args or "S" in args: 
        pass
    if "w" in args or "W" in args: 
        pass
    
def axis_arrows(ax1, c, args):
    # Draw arrows
    arrow_fmt = dict(markersize=4, color=c, clip_on=False)
    if "n" in args or "N" in args: 
        ax1.plot((0), (1), marker='^', transform=ax1.get_xaxis_transform(), **arrow_fmt)
    if "e" in args or "E" in args: 
        ax1.plot((1), (0), marker='>', transform=ax1.get_yaxis_transform(), **arrow_fmt)
    if "s" in args or "S" in args: 
        pass
    if "w" in args or "W" in args: 
        pass

def axis_label(ax1, xtic, xlab, ytic, ylab):
    ax1.set_xticks(xtic)
    ax1.set_xticklabels(xlab)
    ax1.set_yticks(ytic)
    ax1.set_yticklabels(ylab)

def x_label_color(ax1, color):
    ax1.tick_params(axis='x', colors=color)

def y_label_color(ax1, color):
    ax1.tick_params(axis='y', colors=color)

def fun(x):
    return 2 * x**2

def fun2(x):
    return x**2

def plot_curves(ax1): 
    x = np.arange(-2.1, 2.1, .01)
    ax1.plot(x, fun(x), color="teal")
    ax1.plot(x, fun2(x), color="b")

def plot_segments(ax1):
    ax1.plot([0, 1/2], [1, 1], color="r", linewidth=2)
    ax1.plot([1/2, 1/2 + 1/6], [1, 0], color="r", linewidth=2)
    ax1.plot([1/2 + 1/6, 1], [0, 0], color="r", linewidth=2)
    ax1.plot([1/2, 1/2], [0, 1], color="teal", linestyle="--")
    pass

def plot_points(ax1):
    plt.scatter([3], [fun(3)], color="r", marker="o")
    pass

def fill(ax1):
    x = np.arange(-2, 2, .01)
    ax1.fill_between(x=x, y1=fun(x), y2=fun2(x),
                    color="orange", alpha=.4)

def text(ax1, coor, text, c):
    #Add text
    ax1.text(coor[0], coor[1], text, color=c)


def save_file():
    file_name = str(__file__)[0:-1] + "ng"
    plt.savefig(file_name)


if __name__ == "__main__":
    # k = 3
    k = 3
    START = time.time()
    plt_parameters()
    FIG, AX = plt.subplots()
    AX.set(aspect=1)
    axis_limits(AX, -2.1, 2.1, -.1, 4.1)
    set_position(AX)
    remove_axes(AX, "n", "e")
    axis_arrows(AX, "k", ["n", "e"])
    axis_label(AX, xtic=[], xlab=[], ytic=[], ylab=[])
    plot_curves(AX)
    fill(AX)
    
    text(AX, coor=[.3, 3], text=r"$y=2x^2$", c="teal")
    text(AX, coor=[1, .8], text=r"$y=x^2$", c="b")
    text(AX, coor=[-.5, 2], text=r"$f(x,y)>0$", c="r")
    text(AX, coor=[-2, .1], text=r"$f(x,y)>0$", c="r")
    text(AX, coor=[-2.5, 3.85], text=r"$f(x,y)<0$", c="orange")
    text(AX, coor=[1, 3.85], text=r"$f(x,y)<0$", c="orange")

    
    plt.tight_layout()
    save_file()
    Dtime(START)
    plt.show()