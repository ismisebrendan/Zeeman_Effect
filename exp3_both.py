import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii

# Font stuff
plt.rc('legend', fontsize=20)
plt.rc('figure', titlesize=20)
plt.rc('axes', labelsize=20)
plt.rc('font', size=18)

# Pixel ranges are always the same
pixels = np.arange(0, 2048, 1)

# Import data
data = ascii.read('data_exp3_both.txt')
intensitywo = data['intensitywo']
intensity00 = data['intensity00']
intensity030 = data['intensity030']
intensity060 = data['intensity060']
intensity090 = data['intensity090']

intensity300 = data['intensity300']
intensity3030 = data['intensity3030']
intensity3060 = data['intensity3060']
intensity3090 = data['intensity3090']

intensity600 = data['intensity600']
intensity6030 = data['intensity6030']
intensity6060 = data['intensity6060']
intensity6090 = data['intensity6090']

intensity900 = data['intensity900']
intensity9030 = data['intensity9030']
intensity9060 = data['intensity9060']
intensity9090 = data['intensity9090']

data_non = ascii.read('data_exp3_not_polarised.txt')
intensity7 = data_non['intensity7']


plt.plot(pixels, intensity7, label='No polariser, I = 7.0 A', linestyle='dotted', linewidth=5)
plt.plot(pixels, intensity00, label='intensity 00')
plt.plot(pixels, intensitywo, label='intensity wo')
plt.plot(pixels, intensity00, label=r'$\theta$ = 0$^{\circ}$, $\phi$ = 0$^{\circ}$', linewidth=5)
plt.plot(pixels, intensity030, label=r'$\theta$ = 30$^{\circ}$, $\phi$ = 0$^{\circ}$', linewidth=5)
plt.plot(pixels, intensity060, label=r'$\theta$ = 60$^{\circ}$, $\phi$ = 0$^{\circ}$', linewidth=5)
plt.plot(pixels, intensity090, label=r'$\theta$ = 90$^{\circ}$, $\phi$ = 0$^{\circ}$', linewidth=5)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with a longitudinal magnetic field present when\nthe light was passed through a linear polariser at angle $\\theta$ and a quarter wave plate at angle $\\phi$')
plt.legend(loc=8)
plt.show()


plt.plot(pixels, intensity7, label='No polariser, I = 7.0 A', linestyle='dotted', linewidth=5)
plt.plot(pixels, intensity300, label=r'$\theta$ = 0$^{\circ}$, $\phi$ = 30$^{\circ}$', linewidth=5)
plt.plot(pixels, intensity3030, label=r'$\theta$ = 30$^{\circ}$, $\phi$ = 30$^{\circ}$', linewidth=5)
plt.plot(pixels, intensity3060, label=r'$\theta$ = 60$^{\circ}$, $\phi$ = 30$^{\circ}$', linewidth=5)
plt.plot(pixels, intensity3090, label=r'$\theta$ = 90$^{\circ}$, $\phi$ = 30$^{\circ}$', linewidth=5)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with a longitudinal magnetic field present when\nthe light was passed through a linear polariser at angle $\\theta$ and a quarter wave plate at angle $\\phi$')
plt.xlim([850, 1240])
plt.legend(loc=8)
plt.show()


plt.plot(pixels, intensity7, label='No polariser, I = 7.0 A', linestyle='dotted', linewidth=5)
plt.plot(pixels, intensity600, label=r'$\theta$ = 0$^{\circ}$, $\phi$ = 60$^{\circ}$', linewidth=5)
plt.plot(pixels, intensity6030, label=r'$\theta$ = 30$^{\circ}$, $\phi$ = 60$^{\circ}$', linewidth=5)
plt.plot(pixels, intensity6060, label=r'$\theta$ = 60$^{\circ}$, $\phi$ = 60$^{\circ}$', linewidth=5)
plt.plot(pixels, intensity6090, label=r'$\theta$ = 90$^{\circ}$, $\phi$ = 60$^{\circ}$', linewidth=5)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with a longitudinal magnetic field present when\nthe light was passed through a linear polariser at angle $\\theta$ and a quarter wave plate at angle $\\phi$')
plt.xlim([850, 1240])
plt.legend(loc=8)
plt.show()


plt.plot(pixels, intensity7, label='No polariser, I = 7.0 A', linestyle='dotted', linewidth=5)
plt.plot(pixels, intensity900, label=r'$\theta$ = 0$^{\circ}$, $\phi$ = 90$^{\circ}$', linewidth=5)
plt.plot(pixels, intensity9030, label=r'$\theta$ = 30$^{\circ}$, $\phi$ = 90$^{\circ}$', linewidth=5)
plt.plot(pixels, intensity9060, label=r'$\theta$ = 60$^{\circ}$, $\phi$ = 90$^{\circ}$', linewidth=5)
plt.plot(pixels, intensity9090, label=r'$\theta$ = 90$^{\circ}$, $\phi$ = 90$^{\circ}$', linewidth=5)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with a longitudinal magnetic field present when\nthe light was passed through a linear polariser at angle $\\theta$ and a quarter wave plate at angle $\\phi$')
plt.xlim([850, 1240])
plt.legend(loc=8)
plt.show()