import numpy as np
import matplotlib.pyplot as plt


# Zad 1,2
def sinus(f, fs):
    dt = 1/fs
    t = np.arange(0, 1, dt)
    s = np.sin(2 * np.pi * f * t)
    return t, s


if __name__ == '__main__':
    # Zad 3
    fig, ((a20, a21), (a30, a45), (a50, a100), (a150, a200), (a250, a1000)) = plt.subplots(5, 2)
    f = 10

    t, s = sinus(f, 20)
    a20.plot(t, s)
    a20.set_title('20 Hz')

    t, s = sinus(f, 21)
    a21.plot(t, s)
    a21.set_title('21 Hz')

    t, s = sinus(f, 30)
    a30.plot(t, s)
    a30.set_title('30 Hz')

    t, s = sinus(f, 45)
    a45.plot(t, s)
    a45.set_title('45 Hz')

    t, s = sinus(f, 50)
    a50.plot(t, s)
    a50.set_title('50 Hz')

    t, s = sinus(f, 100)
    a100.plot(t, s)
    a100.set_title('100 Hz')

    t, s = sinus(f, 150)
    a150.plot(t, s)
    a150.set_title('150 Hz')

    t, s = sinus(f, 200)
    a200.plot(t, s)
    a200.set_title('200 Hz')

    t, s = sinus(f, 250)
    a250.plot(t, s)
    a250.set_title('250 Hz')

    t, s = sinus(f, 1000)
    a1000.plot(t, s)
    a1000.set_title('1000 Hz')

    fig.tight_layout()
    plt.show()

    # Zad 7
    methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
               'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
               'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

    fig, axs = plt.subplots(nrows=3, ncols=6, figsize=(9, 6),
                            subplot_kw={'xticks': [], 'yticks': []})
    img = plt.imread('ikona.png')
    for ax, interp_method in zip(axs.flat, methods):
        ax.imshow(img, interpolation=interp_method, cmap='viridis')
        ax.set_title(str(interp_method))

    plt.savefig('Metody.png')
    plt.tight_layout()
    plt.show()
