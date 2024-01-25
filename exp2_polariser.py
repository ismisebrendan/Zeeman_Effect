import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii

# Font stuff
plt.rc('legend', fontsize=20)
plt.rc('figure', titlesize=20)
plt.rc('axes', labelsize=20)
plt.rc('font', size=20)

# Pixel ranges are always the same
pixels = np.arange(0, 2048, 1)

# Import data
data = ascii.read('data_exp2_polarised.txt')
intensitywo = data['intensitywo']
intensityw = data['intensityw']
intensity0 = data['intensity0']
intensity30 = data['intensity30']
intensity60 = data['intensity60']
intensity90 = data['intensity90']
intensityn30 = data['intensityn30']
intensityn60 = data['intensityn60']
intensityn90 = data['intensityn90']

data = ascii.read('data_exp2_not_polarised.txt')
intensity7 = data['intensity7']

# Positive angles
plt.plot(pixels, intensity7, label='No polariser, I = 7.0 A', linestyle='dotted', linewidth=5)
plt.plot(pixels, intensity0, label=r'$\theta$ = 0$^{\circ}$, I = 7.0 A', linewidth=5)
plt.plot(pixels, intensity30, label=r'$\theta$ = 30$^{\circ}$, I = 7.0 A', linewidth=5)
plt.plot(pixels, intensity60, label=r'$\theta$ = 60$^{\circ}$, I = 7.0 A', linewidth=5)
plt.plot(pixels, intensity90, label=r'$\theta$ = 90$^{\circ}$, I = 7.0 A', linewidth=5)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with a transverse magnetic\nfield present when the light was passed through a linear polariser at angle $\\theta$')
plt.xlim([830, 1200])
plt.legend(loc=8)
plt.show()

# Negative angles
plt.plot(pixels, intensity7, label='No polariser, I = 7.0 A', linestyle='dotted', linewidth=5)
plt.plot(pixels, intensity0, label=r'$\theta$ = 0$^{\circ}$, I = 7.0 A', linewidth=5)
plt.plot(pixels, intensityn30, label=r'$\theta$ = -30$^{\circ}$, I = 7.0 A', linewidth=5)
plt.plot(pixels, intensityn60, label=r'$\theta$ = -60$^{\circ}$, I = 7.0 A', linewidth=5)
plt.plot(pixels, intensityn90, label=r'$\theta$ = -90$^{\circ}$, I = 7.0 A', linewidth=5)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with a transverse magnetic\nfield present when the light was passed through a linear polariser at angle $\\theta$')
plt.xlim([830, 1200])
plt.legend(loc=8)
plt.show()