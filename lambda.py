import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt
from scipy import stats
from funcs import peak_fitting, plot_peaks, rad_err, rad_sqd_err

# Pixel ranges are always the same
pixels = np.arange(0, 2048, 1)

plt.rc('legend', fontsize=20)
plt.rc('figure', titlesize=20)
plt.rc('axes', labelsize=20)
plt.rc('font', size=20)

####################################################################
#                                                                  #
#   Data from 8 November - worse than that for 15 or 22 November   #
#                                                                  #
####################################################################

# Import data and assign variables
data_8 = ascii.read("data_exp1_8.txt")
intensity1 = data_8['intensity1']
intensity2 = data_8['intensity2']

# Plot the data
plt.plot(pixels, intensity1, label='Exposure = 6')
plt.plot(pixels, intensity2, label='Exposure = 8')
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with no\nmagnetic field present - as recorded on 8 November')
plt.annotate('Note the peak splitting here,\nthis is most likely due to\nimproper alignment/focusing', xy=(760, 45), xytext=(0, 55), arrowprops=dict(arrowstyle="->"))
plt.legend()
plt.show()

# First recording
plt.plot(pixels, intensity1)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with no\nmagnetic field present - Exposure = 6 only')
plt.show()

# Second recording
plt.plot(pixels, intensity2)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with no\nmagnetic field present - Exposure = 8 only')
plt.show()

#####################################
#   Fit peaks for first recording   #
#####################################

# Fit peaks
peakl1, pixelsl1, errorsl1 = peak_fitting(intensity1, 866, 922, 900)
peakl2, pixelsl2, errorsl2 = peak_fitting(intensity1, 790, 840, 810)
peakl3, pixelsl3, errorsl3 = peak_fitting(intensity1, 738, 778, 750)
peakl4, pixelsl4, errorsl4 = peak_fitting(intensity1, 693, 728, 705)
peakl5, pixelsl5, errorsl5 = peak_fitting(intensity1, 651, 686, 665)
peakl6, pixelsl6, errorsl6 = peak_fitting(intensity1, 614, 650, 630)
peakl7, pixelsl7, errorsl7 = peak_fitting(intensity1, 586, 618, 600)
peakl8, pixelsl8, errorsl8 = peak_fitting(intensity1, 553, 583, 565)
peakl9, pixelsl9, errorsl9 = peak_fitting(intensity1, 525, 556, 540)
peakl10, pixelsl10, errorsl10 = peak_fitting(intensity1, 499, 527, 505)

peakr1, pixelsr1, errorsr1 = peak_fitting(intensity1, 1130, 1187, 1150)
peakr2, pixelsr2, errorsr2 = peak_fitting(intensity1, 1214, 1258, 1240)
peakr3, pixelsr3, errorsr3 = peak_fitting(intensity1, 1272, 1318, 1290)
peakr4, pixelsr4, errorsr4 = peak_fitting(intensity1, 1319, 1358, 1340)
peakr5, pixelsr5, errorsr5 = peak_fitting(intensity1, 1362, 1394, 1380)
peakr6, pixelsr6, errorsr6 = peak_fitting(intensity1, 1400, 1434, 1410)
peakr7, pixelsr7, errorsr7 = peak_fitting(intensity1, 1430, 1463, 1450)
peakr8, pixelsr8, errorsr8 = peak_fitting(intensity1, 1464, 1495, 1480)
peakr9, pixelsr9, errorsr9 = peak_fitting(intensity1, 1493, 1520, 1508)
peakr10, pixelsr10, errorsr10 = peak_fitting(intensity1, 1521, 1549, 1535)

peaksl = [peakl1, peakl2, peakl3, peakl4, peakl5, peakl6, peakl7, peakl8, peakl9, peakl10]
pixelsl = [pixelsl1, pixelsl2, pixelsl3, pixelsl4, pixelsl5, pixelsl6, pixelsl7, pixelsl8, pixelsl9, pixelsl10]
errorsl = [errorsl1, errorsl2, errorsl3, errorsl4, errorsl5, errorsl6, errorsl7, errorsl8, errorsl9, errorsl10]

peaksr = [peakr1, peakr2, peakr3, peakr4, peakr5, peakr6, peakr7, peakr8, peakr9, peakr10]
pixelsr = [pixelsr1, pixelsr2, pixelsr3, pixelsr4, pixelsr5, pixelsr6, pixelsr7, pixelsr8, pixelsr9, pixelsr10]
errorsr = [errorsr1, errorsr2, errorsr3, errorsr4, errorsr5, errorsr6, errorsr7, errorsr8, errorsr9, errorsr10]

# Plot data and peaks
plot_peaks(pixels, intensity1, peaksl, pixelsl, peaksr, pixelsr, 60)

plt.title('Graph of intensity (I) recorded for each pixel (p) with no magnetic\nfield present with peaks fit - Exposure = 6 on 8 November only')
plt.show()

# Calculate radii, errors and plot
radii_arr, error_arr = rad_err(peaksl, errorsl, peaksr, errorsr)

m = np.arange(1, len(radii_arr)+1)

fit = stats.linregress(m, radii_arr**2)
slope_err = np.round(fit.stderr, int(np.abs(np.floor(np.log10(fit.stderr)))))
slope = np.round(fit.slope, int(np.abs(np.floor(np.log10(slope_err)))))

intercept_err = np.round(fit.intercept_stderr, int(np.abs(np.floor(np.log10(fit.intercept_stderr)))))
intercept = np.round(fit.intercept, int(np.abs(np.floor(np.log10(intercept_err)))))

error_arr = rad_sqd_err(radii_arr, error_arr)

plt.scatter(m, radii_arr**2, label='$r_m^2$')
plt.errorbar(m, fit.intercept + fit.slope*m, yerr=error_arr, color='red', label='Fit')
plt.xlabel('m')
plt.ylabel('$r_m^2$ ($m^2$)')
plt.plot([], [], ' ', label='R$^2$='+str(np.round(fit.rvalue, 6)))
plt.plot([], [], ' ', label='$r_m^2$=sm+c')
plt.plot([], [], ' ', label='s='+str(slope)+r'$ \pm $'+str(slope_err)+' $m^2$')
plt.plot([], [], ' ', label='c='+str(intercept)+r'$ \pm $'+str(intercept_err)+' $m^2$')
handles, labels = plt.gca().get_legend_handles_labels()
order = [0,5,1,2,3,4]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
plt.title('The radii of the different rings ($r_m^2$) against m - Exposure = 6 on 8 November')
plt.show()

# Save the radii of the first six peaks and their errors for the second part of the lab

radii_arr = np.abs(radii_arr)

radius_file = open('radii.txt','w')

radius_file.write('radius1  radius2 radius3 radius4 radius5 radius6 \n')
radius_file.write(str(radii_arr[0]) + '\t' + str(radii_arr[1]) + '\t' + str(radii_arr[2]) + '\t' + str(radii_arr[3]) + '\t' + str(radii_arr[4]) + '\t' + str(radii_arr[5]) + '\n')


######################################
#   Fit peaks for second recording   #
######################################

# Fit peaks
peakl1, pixelsl1, errorsl1 = peak_fitting(intensity2, 865, 938, 900)
peakl2, pixelsl2, errorsl2 = peak_fitting(intensity2, 800, 843, 820)
peakl3, pixelsl3, errorsl3 = peak_fitting(intensity2, 745, 781, 760)
peakl4, pixelsl4, errorsl4 = peak_fitting(intensity2, 698, 734, 710)
peakl5, pixelsl5, errorsl5 = peak_fitting(intensity2, 656, 692, 675)
peakl6, pixelsl6, errorsl6 = peak_fitting(intensity2, 624, 655, 630)
peakl7, pixelsl7, errorsl7 = peak_fitting(intensity2, 589, 623, 600)
peakl8, pixelsl8, errorsl8 = peak_fitting(intensity2, 558, 588, 570)
peakl9, pixelsl9, errorsl9 = peak_fitting(intensity2, 531, 561, 540)
peakl10, pixelsl10, errorsl10 = peak_fitting(intensity2, 505, 532, 515)

peakr1, pixelsr1, errorsr1 = peak_fitting(intensity2, 1121, 1196, 1150)
peakr2, pixelsr2, errorsr2 = peak_fitting(intensity2, 1216, 1262, 1240)
peakr3, pixelsr3, errorsr3 = peak_fitting(intensity2, 1280, 1327, 1290)
peakr4, pixelsr4, errorsr4 = peak_fitting(intensity2, 1316, 1362, 1340)
peakr5, pixelsr5, errorsr5 = peak_fitting(intensity2, 1368, 1402, 1380)
peakr6, pixelsr6, errorsr6 = peak_fitting(intensity2, 1404, 1439, 1420)
peakr7, pixelsr7, errorsr7 = peak_fitting(intensity2, 1436, 1470, 1450)
peakr8, pixelsr8, errorsr8 = peak_fitting(intensity2, 1471, 1500, 1480)
peakr9, pixelsr9, errorsr9 = peak_fitting(intensity2, 1497, 1528, 1508)
peakr10, pixelsr10, errorsr10 = peak_fitting(intensity2, 1525, 1554, 1540)

peaksl = [peakl1, peakl2, peakl3, peakl4, peakl5, peakl6, peakl7, peakl8, peakl9, peakl10]
pixelsl = [pixelsl1, pixelsl2, pixelsl3, pixelsl4, pixelsl5, pixelsl6, pixelsl7, pixelsl8, pixelsl9, pixelsl10]
errorsl = [errorsl1, errorsl2, errorsl3, errorsl4, errorsl5, errorsl6, errorsl7, errorsl8, errorsl9, errorsl10]

peaksr = [peakr1, peakr2, peakr3, peakr4, peakr5, peakr6, peakr7, peakr8, peakr9, peakr10]
pixelsr = [pixelsr1, pixelsr2, pixelsr3, pixelsr4, pixelsr5, pixelsr6, pixelsr7, pixelsr8, pixelsr9, pixelsr10]
errorsr = [errorsr1, errorsr2, errorsr3, errorsr4, errorsr5, errorsr6, errorsr7, errorsr8, errorsr9, errorsr10]

# Plot data and peaks

plot_peaks(pixels, intensity2, peaksl, pixelsl, peaksr, pixelsr, 60)
plt.title('Graph of intensity (I) recorded for each pixel (p) with no magnetic\nfield present with peaks fit - Exposure = 8 on 8 November only')
plt.show()

# Calculate radii, errors and plot
radii_arr, error_arr = rad_err(peaksl, errorsl, peaksr, errorsr)

m = np.arange(1, len(radii_arr)+1)

fit = stats.linregress(m, radii_arr**2)
slope_err = np.round(fit.stderr, int(np.abs(np.floor(np.log10(fit.stderr)))))
slope = np.round(fit.slope, int(np.abs(np.floor(np.log10(slope_err)))))

intercept_err = np.round(fit.intercept_stderr, int(np.abs(np.floor(np.log10(fit.intercept_stderr)))))
intercept = np.round(fit.intercept, int(np.abs(np.floor(np.log10(intercept_err)))))

error_arr = rad_sqd_err(radii_arr, error_arr)

plt.scatter(m, radii_arr**2, label='$r_m^2$')
plt.errorbar(m, fit.intercept + fit.slope*m, yerr=error_arr, color='red', label='Fit')
plt.xlabel('m')
plt.ylabel('$r_m^2$ ($m^2$)')
plt.plot([], [], ' ', label='R$^2$='+str(np.round(fit.rvalue, 6)))
plt.plot([], [], ' ', label='$r_m^2$=sm+c')
plt.plot([], [], ' ', label='s='+str(slope)+r'$ \pm $'+str(slope_err)+' $m^2$')
plt.plot([], [], ' ', label='c='+str(intercept)+r'$ \pm $'+str(intercept_err)+' $m^2$')
handles, labels = plt.gca().get_legend_handles_labels()
order = [0,5,1,2,3,4]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
plt.title('The radii of the different rings ($r_m^2$) against m - Exposure = 8 on 8 November')
plt.show()

# Save the radii of the first six peaks for the second part of the lab
radii_arr = np.abs(radii_arr)
radius_file.write(str(radii_arr[0]) + '\t' + str(radii_arr[1]) + '\t' + str(radii_arr[2]) + '\t' + str(radii_arr[3]) + '\t' + str(radii_arr[4]) + '\t' + str(radii_arr[5]) + '\n')


#############################
#                           #
#   Data from 15 November   #
#                           #
#############################

# Import data and assign variables
data_15 = ascii.read("data_exp1_15.txt")
intensity1 = data_15['intensity1']
intensity2 = data_15['intensity2']
intensity3 = data_15['intensity3']
intensity4 = data_15['intensity4']

# Plot the data together
plt.plot(pixels, intensity1, label='First recording')
plt.plot(pixels, intensity2, label='Second recording')
plt.plot(pixels, intensity3, label='Third recording')
plt.plot(pixels, intensity4, label='Fourth recording')
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with no\nmagnetic field present - as recorded on 15 November')
plt.legend()
plt.show()

# First recording
plt.plot(pixels, intensity1)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with no\nmagnetic field present - first recording on 15 November only')
plt.show()

# Second recording
plt.plot(pixels, intensity2)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with no\nmagnetic field present - second recording on 15 November only')
plt.show()

# Third recording
plt.plot(pixels, intensity3)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with no\nmagnetic field present - third recording on 15 November only')
plt.show()

# Fourth recording
plt.plot(pixels, intensity4)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with no\nmagnetic field present - fourth recording on 15 November only')
plt.show()

#####################################
#   Fit peaks for first recording   #
#####################################

# Fit peaks
peakl1, pixelsl1, errorsl1 = peak_fitting(intensity1, 866, 929, 900)
peakl2, pixelsl2, errorsl2 = peak_fitting(intensity1, 790, 840, 815)
peakl3, pixelsl3, errorsl3 = peak_fitting(intensity1, 733, 776, 750)
peakl4, pixelsl4, errorsl4 = peak_fitting(intensity1, 687, 726, 700)
peakl5, pixelsl5, errorsl5 = peak_fitting(intensity1, 649, 684, 660)
peakl6, pixelsl6, errorsl6 = peak_fitting(intensity1, 616, 646, 630)
peakl7, pixelsl7, errorsl7 = peak_fitting(intensity1, 580, 615, 590)
peakl8, pixelsl8, errorsl8 = peak_fitting(intensity1, 550, 583, 560)
peakl9, pixelsl9, errorsl9 = peak_fitting(intensity1, 521, 553, 530)
peakl10, pixelsl10, errorsl10 = peak_fitting(intensity1, 495, 524, 505)

peakr1, pixelsr1, errorsr1 = peak_fitting(intensity1, 1102, 1176, 1130)
peakr2, pixelsr2, errorsr2 = peak_fitting(intensity1, 1196, 1250, 1220)
peakr3, pixelsr3, errorsr3 = peak_fitting(intensity1, 1260, 1309, 1280)
peakr4, pixelsr4, errorsr4 = peak_fitting(intensity1, 1310, 1353, 1330)
peakr5, pixelsr5, errorsr5 = peak_fitting(intensity1, 1348, 1389, 1370)
peakr6, pixelsr6, errorsr6 = peak_fitting(intensity1, 1390, 1427, 1410)
peakr7, pixelsr7, errorsr7 = peak_fitting(intensity1, 1428, 1456, 1440)
peakr8, pixelsr8, errorsr8 = peak_fitting(intensity1, 1457, 1490, 1470)
peakr9, pixelsr9, errorsr9 = peak_fitting(intensity1, 1487, 1516, 1500)
peakr10, pixelsr10, errorsr10 = peak_fitting(intensity1, 1517, 1545, 1530)

peaksl = [peakl1, peakl2, peakl3, peakl4, peakl5, peakl6, peakl7, peakl8, peakl9, peakl10]
pixelsl = [pixelsl1, pixelsl2, pixelsl3, pixelsl4, pixelsl5, pixelsl6, pixelsl7, pixelsl8, pixelsl9, pixelsl10]
errorsl = [errorsl1, errorsl2, errorsl3, errorsl4, errorsl5, errorsl6, errorsl7, errorsl8, errorsl9, errorsl10]

peaksr = [peakr1, peakr2, peakr3, peakr4, peakr5, peakr6, peakr7, peakr8, peakr9, peakr10]
pixelsr = [pixelsr1, pixelsr2, pixelsr3, pixelsr4, pixelsr5, pixelsr6, pixelsr7, pixelsr8, pixelsr9, pixelsr10]
errorsr = [errorsr1, errorsr2, errorsr3, errorsr4, errorsr5, errorsr6, errorsr7, errorsr8, errorsr9, errorsr10]

# Plot data and peaks
plot_peaks(pixels, intensity1, peaksl, pixelsl, peaksr, pixelsr, 40)

plt.title('Graph of intensity (I) recorded for each pixel (p) with no magnetic\nfield present with peaks fit - first recording on 15 November only')
plt.show()

# Calculate radii, errors and plot
radii_arr, error_arr = rad_err(peaksl, errorsl, peaksr, errorsr)

m = np.arange(1, len(radii_arr)+1)

fit = stats.linregress(m, radii_arr**2)
slope_err = np.round(fit.stderr, int(np.abs(np.floor(np.log10(fit.stderr)))))
slope = np.round(fit.slope, int(np.abs(np.floor(np.log10(slope_err)))))

intercept_err = np.round(fit.intercept_stderr, int(np.abs(np.floor(np.log10(fit.intercept_stderr)))))
intercept = np.round(fit.intercept, int(np.abs(np.floor(np.log10(intercept_err)))))

error_arr = rad_sqd_err(radii_arr, error_arr)

plt.scatter(m, radii_arr**2, label='$r_m^2$')
plt.errorbar(m, fit.intercept + fit.slope*m, yerr=error_arr, color='red', label='Fit')
plt.xlabel('m')
plt.ylabel('$r_m^2$ ($m^2$)')
plt.plot([], [], ' ', label='R$^2$='+str(np.round(fit.rvalue, 6)))
plt.plot([], [], ' ', label='$r_m^2$=sm+c')
plt.plot([], [], ' ', label='s='+str(slope)+r'$ \pm $'+str(slope_err)+' $m^2$')
plt.plot([], [], ' ', label='c='+str(intercept)+r'$ \pm $'+str(intercept_err)+' $m^2$')
handles, labels = plt.gca().get_legend_handles_labels()
order = [0,5,1,2,3,4]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
plt.title('The radii of the different rings ($r_m^2$) against m - first recording on November 15')
plt.show()

# Save the radii of the first six peaks for the second part of the lab
radii_arr = np.abs(radii_arr)
radius_file.write(str(radii_arr[0]) + '\t' + str(radii_arr[1]) + '\t' + str(radii_arr[2]) + '\t' + str(radii_arr[3]) + '\t' + str(radii_arr[4]) + '\t' + str(radii_arr[5]) + '\n')

######################################
#   Fit peaks for second recording   #
######################################

# Fit peaks
peakl1, pixelsl1, errorsl1 = peak_fitting(intensity2, 858, 931, 900)
peakl2, pixelsl2, errorsl2 = peak_fitting(intensity2, 779, 834, 800)
peakl3, pixelsl3, errorsl3 = peak_fitting(intensity2, 725, 772, 750)
peakl4, pixelsl4, errorsl4 = peak_fitting(intensity2, 686, 720, 700)
peakl5, pixelsl5, errorsl5 = peak_fitting(intensity2, 641, 682, 660)
peakl6, pixelsl6, errorsl6 = peak_fitting(intensity2, 609, 648, 630)
peakl7, pixelsl7, errorsl7 = peak_fitting(intensity2, 577, 608, 590)
peakl8, pixelsl8, errorsl8 = peak_fitting(intensity2, 545, 577, 560)
peakl9, pixelsl9, errorsl9 = peak_fitting(intensity2, 517, 548, 530)
peakl10, pixelsl10, errorsl10 = peak_fitting(intensity2, 489, 519, 505)

peakr1, pixelsr1, errorsr1 = peak_fitting(intensity2, 1103, 1178, 1130)
peakr2, pixelsr2, errorsr2 = peak_fitting(intensity2, 1197, 1254, 1220)
peakr3, pixelsr3, errorsr3 = peak_fitting(intensity2, 1255, 1308, 1280)
peakr4, pixelsr4, errorsr4 = peak_fitting(intensity2, 1302, 1351, 1330)
peakr5, pixelsr5, errorsr5 = peak_fitting(intensity2, 1352, 1386, 1370)
peakr6, pixelsr6, errorsr6 = peak_fitting(intensity2, 1387, 1425, 1410)
peakr7, pixelsr7, errorsr7 = peak_fitting(intensity2, 1426, 1457, 1440)
peakr8, pixelsr8, errorsr8 = peak_fitting(intensity2, 1455, 1489, 1470)
peakr9, pixelsr9, errorsr9 = peak_fitting(intensity2, 1485, 1517, 1500)
peakr10, pixelsr10, errorsr10 = peak_fitting(intensity2, 1514, 1542, 1530)

peaksl = [peakl1, peakl2, peakl3, peakl4, peakl5, peakl6, peakl7, peakl8, peakl9, peakl10]
pixelsl = [pixelsl1, pixelsl2, pixelsl3, pixelsl4, pixelsl5, pixelsl6, pixelsl7, pixelsl8, pixelsl9, pixelsl10]
errorsl = [errorsl1, errorsl2, errorsl3, errorsl4, errorsl5, errorsl6, errorsl7, errorsl8, errorsl9, errorsl10]

peaksr = [peakr1, peakr2, peakr3, peakr4, peakr5, peakr6, peakr7, peakr8, peakr9, peakr10]
pixelsr = [pixelsr1, pixelsr2, pixelsr3, pixelsr4, pixelsr5, pixelsr6, pixelsr7, pixelsr8, pixelsr9, pixelsr10]
errorsr = [errorsr1, errorsr2, errorsr3, errorsr4, errorsr5, errorsr6, errorsr7, errorsr8, errorsr9, errorsr10]

# Plot data and peaks
plot_peaks(pixels, intensity2, peaksl, pixelsl, peaksr, pixelsr, 40)

plt.title('Graph of intensity (I) recorded for each pixel (p) with no magnetic\nfield present with peaks fit - second recording on 15 November only')
plt.show()

# Calculate radii, errors and plot
radii_arr, error_arr = rad_err(peaksl, errorsl, peaksr, errorsr)

m = np.arange(1, len(radii_arr)+1)

fit = stats.linregress(m, radii_arr**2)
slope_err = np.round(fit.stderr, int(np.abs(np.floor(np.log10(fit.stderr)))))
slope = np.round(fit.slope, int(np.abs(np.floor(np.log10(slope_err)))))

intercept_err = np.round(fit.intercept_stderr, int(np.abs(np.floor(np.log10(fit.intercept_stderr)))))
intercept = np.round(fit.intercept, int(np.abs(np.floor(np.log10(intercept_err)))))

error_arr = rad_sqd_err(radii_arr, error_arr)

plt.scatter(m, radii_arr**2, label='$r_m^2$')
plt.errorbar(m, fit.intercept + fit.slope*m, yerr=error_arr, color='red', label='Fit')
plt.xlabel('m')
plt.ylabel('$r_m^2$ ($m^2$)')
plt.plot([], [], ' ', label='R$^2$='+str(np.round(fit.rvalue, 6)))
plt.plot([], [], ' ', label='$r_m^2$=sm+c')
plt.plot([], [], ' ', label='s='+str(slope)+r'$ \pm $'+str(slope_err)+' $m^2$')
plt.plot([], [], ' ', label='c='+str(intercept)+r'$ \pm $'+str(intercept_err)+' $m^2$')
handles, labels = plt.gca().get_legend_handles_labels()
order = [0,5,1,2,3,4]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
plt.title('The radii of the different rings ($r_m^2$) against m - second recording on November 15')
plt.show()


# Save the radii of the first six peaks for the second part of the lab
radii_arr = np.abs(radii_arr)
radius_file.write(str(radii_arr[0]) + '\t' + str(radii_arr[1]) + '\t' + str(radii_arr[2]) + '\t' + str(radii_arr[3]) + '\t' + str(radii_arr[4]) + '\t' + str(radii_arr[5]) + '\n')

#####################################
#   Fit peaks for third recording   #
#####################################

# Fit peaks
peakl1, pixelsl1, errorsl1 = peak_fitting(intensity3, 848, 907, 870)
peakl2, pixelsl2, errorsl2 = peak_fitting(intensity3, 776, 836, 800)
peakl3, pixelsl3, errorsl3 = peak_fitting(intensity3, 726, 763, 750)
peakl4, pixelsl4, errorsl4 = peak_fitting(intensity3, 680, 714, 700)
peakl5, pixelsl5, errorsl5 = peak_fitting(intensity3, 642, 676, 660)
peakl6, pixelsl6, errorsl6 = peak_fitting(intensity3, 603, 639, 620)
peakl7, pixelsl7, errorsl7 = peak_fitting(intensity3, 571, 607, 590)
peakl8, pixelsl8, errorsl8 = peak_fitting(intensity3, 544, 575, 560)
peakl9, pixelsl9, errorsl9 = peak_fitting(intensity3, 514, 542, 530)
peakl10, pixelsl10, errorsl10 = peak_fitting(intensity3, 486, 512, 505)

peakr1, pixelsr1, errorsr1 = peak_fitting(intensity3, 1119, 1188, 1150)
peakr2, pixelsr2, errorsr2 = peak_fitting(intensity3, 1205, 1263, 1220)
peakr3, pixelsr3, errorsr3 = peak_fitting(intensity3, 1266, 1313, 1280)
peakr4, pixelsr4, errorsr4 = peak_fitting(intensity3, 1314, 1356, 1330)
peakr5, pixelsr5, errorsr5 = peak_fitting(intensity3, 1352, 1394, 1370)
peakr6, pixelsr6, errorsr6 = peak_fitting(intensity3, 1395, 1430, 1410)
peakr7, pixelsr7, errorsr7 = peak_fitting(intensity3, 1426, 1462, 1440)
peakr8, pixelsr8, errorsr8 = peak_fitting(intensity3, 1458, 1492, 1475)
peakr9, pixelsr9, errorsr9 = peak_fitting(intensity3, 1489, 1521, 1505)
peakr10, pixelsr10, errorsr10 = peak_fitting(intensity3, 1518, 1547, 1530)

peaksl = [peakl1, peakl2, peakl3, peakl4, peakl5, peakl6, peakl7, peakl8, peakl9, peakl10]
pixelsl = [pixelsl1, pixelsl2, pixelsl3, pixelsl4, pixelsl5, pixelsl6, pixelsl7, pixelsl8, pixelsl9, pixelsl10]
errorsl = [errorsl1, errorsl2, errorsl3, errorsl4, errorsl5, errorsl6, errorsl7, errorsl8, errorsl9, errorsl10]

peaksr = [peakr1, peakr2, peakr3, peakr4, peakr5, peakr6, peakr7, peakr8, peakr9, peakr10]
pixelsr = [pixelsr1, pixelsr2, pixelsr3, pixelsr4, pixelsr5, pixelsr6, pixelsr7, pixelsr8, pixelsr9, pixelsr10]
errorsr = [errorsr1, errorsr2, errorsr3, errorsr4, errorsr5, errorsr6, errorsr7, errorsr8, errorsr9, errorsr10]

# Plot data and peaks
plot_peaks(pixels, intensity3, peaksl, pixelsl, peaksr, pixelsr, 40)

plt.title('Graph of intensity (I) recorded for each pixel (p) with no magnetic\nfield present with peaks fit - third recording on 15 November only')
plt.show()

# Calculate radii, errors and plot
radii_arr, error_arr = rad_err(peaksl, errorsl, peaksr, errorsr)

m = np.arange(1, len(radii_arr)+1)

fit = stats.linregress(m, radii_arr**2)
slope_err = np.round(fit.stderr, int(np.abs(np.floor(np.log10(fit.stderr)))))
slope = np.round(fit.slope, int(np.abs(np.floor(np.log10(slope_err)))))

intercept_err = np.round(fit.intercept_stderr, int(np.abs(np.floor(np.log10(fit.intercept_stderr)))))
intercept = np.round(fit.intercept, int(np.abs(np.floor(np.log10(intercept_err)))))

error_arr = rad_sqd_err(radii_arr, error_arr)

plt.scatter(m, radii_arr**2, label='$r_m^2$')
plt.errorbar(m, fit.intercept + fit.slope*m, yerr=error_arr, color='red', label='Fit')
plt.xlabel('m')
plt.ylabel('$r_m^2$ ($m^2$)')
plt.plot([], [], ' ', label='R$^2$='+str(np.round(fit.rvalue, 6)))
plt.plot([], [], ' ', label='$r_m^2$=sm+c')
plt.plot([], [], ' ', label='s='+str(slope)+r'$ \pm $'+str(slope_err)+' $m^2$')
plt.plot([], [], ' ', label='c='+str(intercept)+r'$ \pm $'+str(intercept_err)+' $m^2$')
handles, labels = plt.gca().get_legend_handles_labels()
order = [0,5,1,2,3,4]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
plt.title('The radii of the different rings ($r_m^2$) against m - third recording on November 15')
plt.show()


# Save the radii of the first six peaks for the second part of the lab
radii_arr = np.abs(radii_arr)
radius_file.write(str(radii_arr[0]) + '\t' + str(radii_arr[1]) + '\t' + str(radii_arr[2]) + '\t' + str(radii_arr[3]) + '\t' + str(radii_arr[4]) + '\t' + str(radii_arr[5]) + '\n')


######################################
#   Fit peaks for fourth recording   #
######################################

# Fit peaks
peakl1, pixelsl1, errorsl1 = peak_fitting(intensity4, 834, 892, 860)
peakl2, pixelsl2, errorsl2 = peak_fitting(intensity4, 764, 808, 780)
peakl3, pixelsl3, errorsl3 = peak_fitting(intensity4, 708, 746, 720)
peakl4, pixelsl4, errorsl4 = peak_fitting(intensity4, 662, 693, 680)
peakl5, pixelsl5, errorsl5 = peak_fitting(intensity4, 626, 652, 640)
peakl6, pixelsl6, errorsl6 = peak_fitting(intensity4, 580, 625, 600)
peakl7, pixelsl7, errorsl7 = peak_fitting(intensity4, 548, 590, 570)
peakl8, pixelsl8, errorsl8 = peak_fitting(intensity4, 528, 558, 540)
peakl9, pixelsl9, errorsl9 = peak_fitting(intensity4, 500, 518, 510)
peakl10, pixelsl10, errorsl10 = peak_fitting(intensity4, 474, 493, 480)

peakr1, pixelsr1, errorsr1 = peak_fitting(intensity4, 1114, 1172, 1150)
peakr2, pixelsr2, errorsr2 = peak_fitting(intensity4, 1204, 1248, 1220)
peakr3, pixelsr3, errorsr3 = peak_fitting(intensity4, 1262, 1313, 1280)
peakr4, pixelsr4, errorsr4 = peak_fitting(intensity4, 1313, 1344, 1330)
peakr5, pixelsr5, errorsr5 = peak_fitting(intensity4, 1345, 1392, 1370)
peakr6, pixelsr6, errorsr6 = peak_fitting(intensity4, 1384, 1428, 1410)
peakr7, pixelsr7, errorsr7 = peak_fitting(intensity4, 1419, 1451, 1440)
peakr8, pixelsr8, errorsr8 = peak_fitting(intensity4, 1460, 1489, 1470)
peakr9, pixelsr9, errorsr9 = peak_fitting(intensity4, 1481, 1517, 1500)
peakr10, pixelsr10, errorsr10 = peak_fitting(intensity4, 1518, 1539, 1530)

peaksl = [peakl1, peakl2, peakl3, peakl4, peakl5, peakl6, peakl7, peakl8, peakl9, peakl10]
pixelsl = [pixelsl1, pixelsl2, pixelsl3, pixelsl4, pixelsl5, pixelsl6, pixelsl7, pixelsl8, pixelsl9, pixelsl10]
errorsl = [errorsl1, errorsl2, errorsl3, errorsl4, errorsl5, errorsl6, errorsl7, errorsl8, errorsl9, errorsl10]

peaksr = [peakr1, peakr2, peakr3, peakr4, peakr5, peakr6, peakr7, peakr8, peakr9, peakr10]
pixelsr = [pixelsr1, pixelsr2, pixelsr3, pixelsr4, pixelsr5, pixelsr6, pixelsr7, pixelsr8, pixelsr9, pixelsr10]
errorsr = [errorsr1, errorsr2, errorsr3, errorsr4, errorsr5, errorsr6, errorsr7, errorsr8, errorsr9, errorsr10]

# Plot data and peaks
plot_peaks(pixels, intensity4, peaksl, pixelsl, peaksr, pixelsr, 60, 3)

plt.title('Graph of intensity (I) recorded for each pixel (p) with no magnetic\nfield present with peaks fit - fourth recording on 15 November only')
plt.show()

# Calculate radii, errors and plot
radii_arr, error_arr = rad_err(peaksl, errorsl, peaksr, errorsr)

m = np.arange(1, len(radii_arr)+1)

fit = stats.linregress(m, radii_arr**2)
slope_err = np.round(fit.stderr, int(np.abs(np.floor(np.log10(fit.stderr)))))
slope = np.round(fit.slope, int(np.abs(np.floor(np.log10(slope_err)))))

intercept_err = np.round(fit.intercept_stderr, int(np.abs(np.floor(np.log10(fit.intercept_stderr)))))
intercept = np.round(fit.intercept, int(np.abs(np.floor(np.log10(intercept_err)))))

error_arr = rad_sqd_err(radii_arr, error_arr)

plt.scatter(m, radii_arr**2, label='$r_m^2$')
plt.errorbar(m, fit.intercept + fit.slope*m, yerr=error_arr, color='red', label='Fit')
plt.xlabel('m')
plt.ylabel('$r_m^2$ ($m^2$)')
plt.plot([], [], ' ', label='R$^2$='+str(np.round(fit.rvalue, 6)))
plt.plot([], [], ' ', label='$r_m^2$=sm+c')
plt.plot([], [], ' ', label='s='+str(slope)+r'$ \pm $'+str(slope_err)+' $m^2$')
plt.plot([], [], ' ', label='c='+str(intercept)+r'$ \pm $'+str(intercept_err)+' $m^2$')
handles, labels = plt.gca().get_legend_handles_labels()
order = [0,5,1,2,3,4]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
plt.title('The radii of the different rings ($r_m^2$) against m - fourth recording on November 15')
plt.show()


# Save the radii of the first six peaks for the second part of the lab
radii_arr = np.abs(radii_arr)
radius_file.write(str(radii_arr[0]) + '\t' + str(radii_arr[1]) + '\t' + str(radii_arr[2]) + '\t' + str(radii_arr[3]) + '\t' + str(radii_arr[4]) + '\t' + str(radii_arr[5]) + '\n')




############################
#                           #
#   Data from 22 November   #
#                           #
#############################

# Import data and assign variables
data_22 = ascii.read("data_exp1_22.txt")
intensity1 = data_22['intensity1']

# Plot the data together
plt.plot(pixels, intensity1, label='First recording')
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with no\nmagnetic field present - as recorded on 22 November')
plt.show()

#####################################
#   Fit peaks for first recording   #
#####################################

# Fit peaks
peakl1, pixelsl1, errorsl1 = peak_fitting(intensity1, 854, 905, 880)
peakl2, pixelsl2, errorsl2 = peak_fitting(intensity1, 785, 824, 800)
peakl3, pixelsl3, errorsl3 = peak_fitting(intensity1, 730, 766, 750)
peakl4, pixelsl4, errorsl4 = peak_fitting(intensity1, 679, 720, 700)
peakl5, pixelsl5, errorsl5 = peak_fitting(intensity1, 644, 678, 660)
peakl6, pixelsl6, errorsl6 = peak_fitting(intensity1, 607, 640, 630)
peakl7, pixelsl7, errorsl7 = peak_fitting(intensity1, 580, 606, 590)
peakl8, pixelsl8, errorsl8 = peak_fitting(intensity1, 548, 576, 560)
peakl9, pixelsl9, errorsl9 = peak_fitting(intensity1, 517, 545, 530)
peakl10, pixelsl10, errorsl10 = peak_fitting(intensity1, 492, 521, 505)

peakr1, pixelsr1, errorsr1 = peak_fitting(intensity1, 1162, 1206, 1180)
peakr2, pixelsr2, errorsr2 = peak_fitting(intensity1, 1242, 1277, 1250)
peakr3, pixelsr3, errorsr3 = peak_fitting(intensity1, 1288, 1332, 1310)
peakr4, pixelsr4, errorsr4 = peak_fitting(intensity1, 1342, 1385, 1360)
peakr5, pixelsr5, errorsr5 = peak_fitting(intensity1, 1386, 1423, 1400)
peakr6, pixelsr6, errorsr6 = peak_fitting(intensity1, 1412, 1449, 1440)
peakr7, pixelsr7, errorsr7 = peak_fitting(intensity1, 1450, 1481, 1470)
peakr8, pixelsr8, errorsr8 = peak_fitting(intensity1, 1488, 1512, 1500)
peakr9, pixelsr9, errorsr9 = peak_fitting(intensity1, 1518, 1545, 1530)
peakr10, pixelsr10, errorsr10 = peak_fitting(intensity1, 1546, 1572, 1555)

peaksl = [peakl1, peakl2, peakl3, peakl4, peakl5, peakl6, peakl7, peakl8, peakl9, peakl10]
pixelsl = [pixelsl1, pixelsl2, pixelsl3, pixelsl4, pixelsl5, pixelsl6, pixelsl7, pixelsl8, pixelsl9, pixelsl10]
errorsl = [errorsl1, errorsl2, errorsl3, errorsl4, errorsl5, errorsl6, errorsl7, errorsl8, errorsl9, errorsl10]

peaksr = [peakr1, peakr2, peakr3, peakr4, peakr5, peakr6, peakr7, peakr8, peakr9, peakr10]
pixelsr = [pixelsr1, pixelsr2, pixelsr3, pixelsr4, pixelsr5, pixelsr6, pixelsr7, pixelsr8, pixelsr9, pixelsr10]
errorsr = [errorsr1, errorsr2, errorsr3, errorsr4, errorsr5, errorsr6, errorsr7, errorsr8, errorsr9, errorsr10]

# Plot data and peaks
plot_peaks(pixels, intensity1, peaksl, pixelsl, peaksr, pixelsr, 35)

plt.title('Graph of intensity (I) recorded for each pixel (p) with no magnetic\nfield present with peaks fit - as recorded on November 22')
plt.show()

# Calculate radii, errors and plot
radii_arr, error_arr = rad_err(peaksl, errorsl, peaksr, errorsr)

m = np.arange(1, len(radii_arr)+1)

fit = stats.linregress(m, radii_arr**2)
slope_err = np.round(fit.stderr, int(np.abs(np.floor(np.log10(fit.stderr)))))
slope = np.round(fit.slope, int(np.abs(np.floor(np.log10(slope_err)))))

intercept_err = np.round(fit.intercept_stderr, int(np.abs(np.floor(np.log10(fit.intercept_stderr)))))
intercept = np.round(fit.intercept, int(np.abs(np.floor(np.log10(intercept_err)))))

error_arr = rad_sqd_err(radii_arr, error_arr)

plt.scatter(m, radii_arr**2, label='$r_m^2$')
plt.errorbar(m, fit.intercept + fit.slope*m, yerr=error_arr, color='red', label='Fit')
plt.xlabel('m')
plt.ylabel('$r_m^2$ ($m^2$)')
plt.plot([], [], ' ', label='R$^2$='+str(np.round(fit.rvalue, 6)))
plt.plot([], [], ' ', label='$r_m^2$=sm+c')
plt.plot([], [], ' ', label='s='+str(slope)+r'$ \pm $'+str(slope_err)+' $m^2$')
plt.plot([], [], ' ', label='c='+str(intercept)+r'$ \pm $'+str(intercept_err)+' $m^2$')
handles, labels = plt.gca().get_legend_handles_labels()
order = [0,5,1,2,3,4]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
plt.title('The radii of the different rings ($r_m^2$) against m - as recorded on November 22')
plt.show()

# Save the radii of the first six peaks for the second part of the lab
radii_arr = np.abs(radii_arr)
radius_file.write(str(radii_arr[0]) + '\t' + str(radii_arr[1]) + '\t' + str(radii_arr[2]) + '\t' + str(radii_arr[3]) + '\t' + str(radii_arr[4]) + '\t' + str(radii_arr[5]) + '\n')


################
# Output radii #
################

radius_file.close()