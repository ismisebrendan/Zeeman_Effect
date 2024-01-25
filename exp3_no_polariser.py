import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from funcs import peak_fitting, plot_peaks, rad_err, delta_rad, round_sig_fig_uncertainty, plot_peaks_no_labels

# Pixel ranges are always the same
pixels = np.arange(0, 2048, 1)

plt.rc('legend', fontsize=20)
plt.rc('figure', titlesize=20)
plt.rc('axes', labelsize=20)
plt.rc('font', size=20)

# Import intensity data
data = ascii.read('data_exp3_not_polarised.txt')
intensity0 = data['intensity0']
intensity5 = data['intensity5']
intensity6 = data['intensity6']
intensity7 = data['intensity7']

# Plot together
plt.plot(pixels, intensity0, label='Current = 0 A')
plt.plot(pixels, intensity5, label='Current = 5 A')
plt.plot(pixels, intensity6, label='Current = 6 A')
plt.plot(pixels, intensity7, label='Current = 7 A')
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with a longitudinal magnetic field')
plt.legend()
#plt.show()

# Plot separately
plt.plot(pixels, intensity5)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p)\nwith a longitudinal magnetic field for a current of 5 A')
#plt.show()

plt.plot(pixels, intensity6)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p)\nwith a longitudinal magnetic field for a current of 6 A')
#plt.show()

plt.plot(pixels, intensity7)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p)\nwith a longitudinal magnetic field for a current of 7 A')
#plt.show()

###############
#   I = 0 A   #
###############

peakl1, pixelsl1, errorsl1 = peak_fitting(intensity0, 834, 892, 860)
peakl2, pixelsl2, errorsl2 = peak_fitting(intensity0, 764, 808, 780)
peakl3, pixelsl3, errorsl3 = peak_fitting(intensity0, 708, 746, 720)
peakl4, pixelsl4, errorsl4 = peak_fitting(intensity0, 662, 693, 680)
peakl5, pixelsl5, errorsl5 = peak_fitting(intensity0, 626, 652, 640)
peakl6, pixelsl6, errorsl6 = peak_fitting(intensity0, 580, 625, 600)

peakr1, pixelsr1, errorsr1 = peak_fitting(intensity0, 1114, 1172, 1150)
peakr2, pixelsr2, errorsr2 = peak_fitting(intensity0, 1204, 1248, 1220)
peakr3, pixelsr3, errorsr3 = peak_fitting(intensity0, 1262, 1313, 1280)
peakr4, pixelsr4, errorsr4 = peak_fitting(intensity0, 1313, 1344, 1330)
peakr5, pixelsr5, errorsr5 = peak_fitting(intensity0, 1345, 1392, 1370)
peakr6, pixelsr6, errorsr6 = peak_fitting(intensity0, 1384, 1428, 1410)

peaksl = [peakl1, peakl2, peakl3, peakl4, peakl5, peakl6]
pixelsl = [pixelsl1, pixelsl2, pixelsl3, pixelsl4, pixelsl5, pixelsl6]
errorsl = [errorsl1, errorsl2, errorsl3, errorsl4, errorsl5, errorsl6]

peaksr = [peakr1, peakr2, peakr3, peakr4, peakr5, peakr6]
pixelsr = [pixelsr1, pixelsr2, pixelsr3, pixelsr4, pixelsr5, pixelsr6]
errorsr = [errorsr1, errorsr2, errorsr3, errorsr4, errorsr5, errorsr6]

# Plot data and peaks
plot_peaks(pixels, intensity0, peaksl, pixelsl, peaksr, pixelsr, 60, 3)

plt.title('Graph of intensity (I) recorded for each pixel (p) with no\nlongitudinal magnetic field or current present with the peaks fitted')
#plt.show()

# Calculate radii and errors, and store
radii_arr_0A, error_arr_0A = np.abs(rad_err(peaksl, errorsl, peaksr, errorsr))

# Record outer and inner radii
radii_in_arr = np.array([radii_arr_0A])
delta_radii_in_arr = np.array([np.zeros_like(radii_arr_0A)])
rdr_in_arr = np.array([np.zeros_like(radii_arr_0A)])

err_radii_in_arr = np.array([error_arr_0A])
err_delta_radii_in_arr = np.array([np.zeros_like(radii_arr_0A)])
err_rdr_in_arr = np.array([np.zeros_like(radii_arr_0A)])

radii_out_arr = np.array([radii_arr_0A])
delta_radii_out_arr = np.array([np.zeros_like(radii_arr_0A)])
rdr_out_arr = np.array([np.zeros_like(radii_arr_0A)])

err_radii_out_arr = np.array([error_arr_0A])
err_delta_radii_out_arr = np.array([np.zeros_like(radii_arr_0A)])
err_rdr_out_arr = np.array([np.zeros_like(radii_arr_0A)])


###################
#   Fit I = 5 A   #
###################

# Fit peaks
peakl1in, pixelsl1in, errorsl1in = peak_fitting(intensity5, 864, 914, 880)
peakl1out, pixelsl1out, errorsl1out = peak_fitting(intensity5, 817, 863, 840)
peakl2in, pixelsl2in, errorsl2in = peak_fitting(intensity5, 782, 816, 800)
peakl2out, pixelsl2out, errorsl2out = peak_fitting(intensity5, 751, 784, 770)
peakl3in, pixelsl3in, errorsl3in = peak_fitting(intensity5, 726, 753, 735)
peakl3out, pixelsl3out, errorsl3out = peak_fitting(intensity5, 702, 728, 715)
peakl4in, pixelsl4in, errorsl4in = peak_fitting(intensity5, 679, 701, 690)
peakl4out, pixelsl4out, errorsl4out = peak_fitting(intensity5, 659, 681, 670)
peakl5in, pixelsl5in, errorsl5in = peak_fitting(intensity5, 639, 658, 645)
peakl5out, pixelsl5out, errorsl5out = peak_fitting(intensity5, 619, 639, 630)
peakl6in, pixelsl6in, errorsl6in = peak_fitting(intensity5, 602, 621, 610)
peakl6out, pixelsl6out, errorsl6out = peak_fitting(intensity5, 585, 603, 595)

peakr1in, pixelsr1in, errorsr1in = peak_fitting(intensity5, 1097, 1149, 1120)
peakr1out, pixelsr1out, errorsr1out = peak_fitting(intensity5, 1149, 1193, 1160)
peakr2in, pixelsr2in, errorsr2in = peak_fitting(intensity5, 1188, 1226, 1210)
peakr2out, pixelsr2out, errorsr2out = peak_fitting(intensity5, 1225, 1254, 1235)
peakr3in, pixelsr3in, errorsr3in = peak_fitting(intensity5, 1256, 1281, 1270)
peakr3out, pixelsr3out, errorsr3out = peak_fitting(intensity5, 1282, 1307, 1290)
peakr4in, pixelsr4in, errorsr4in = peak_fitting(intensity5, 1306, 1328, 1320)
peakr4out, pixelsr4out, errorsr4out = peak_fitting(intensity5, 1328, 1350, 1335)
peakr5in, pixelsr5in, errorsr5in = peak_fitting(intensity5, 1350, 1369, 1360)
peakr5out, pixelsr5out, errorsr5out = peak_fitting(intensity5, 1369, 1389, 1375)
peakr6in, pixelsr6in, errorsr6in = peak_fitting(intensity5, 1387, 1406, 1395)
peakr6out, pixelsr6out, errorsr6out = peak_fitting(intensity5, 1405, 1422, 1410)

peakslin = [peakl1in, peakl2in, peakl3in, peakl4in, peakl5in, peakl6in]
pixelslin = [pixelsl1in, pixelsl2in, pixelsl3in, pixelsl4in, pixelsl5in, pixelsl6in]
errorslin = [errorsl1in, errorsl2in, errorsl3in, errorsl4in, errorsl5in, errorsl6in]

peakslout = [peakl1out, peakl2out, peakl3out, peakl4out, peakl5out, peakl6out]
pixelslout = [pixelsl1out, pixelsl2out, pixelsl3out, pixelsl4out, pixelsl5out, pixelsl6out]
errorslout = [errorsl1out, errorsl2out, errorsl3out, errorsl4out, errorsl5out, errorsl6out]

peaksrin = [peakr1in, peakr2in, peakr3in, peakr4in, peakr5in, peakr6in]
pixelsrin = [pixelsr1in, pixelsr2in, pixelsr3in, pixelsr4in, pixelsr5in, pixelsr6in]
errorsrin = [errorsr1in, errorsr2in, errorsr3in, errorsr4in, errorsr5in, errorsr6in]

peaksrout = [peakr1out, peakr2out, peakr3out, peakr4out, peakr5out, peakr6out]
pixelsrout = [pixelsr1out, pixelsr2out, pixelsr3out, pixelsr4out, pixelsr5out, pixelsr6out]
errorsrout = [errorsr1out, errorsr2out, errorsr3out, errorsr4out, errorsr5out, errorsr6out]

# Plot data and peaks
plot_peaks(pixels, intensity5, peakslin, pixelslin, peaksrin, pixelsrin, 55, 6)
plot_peaks_no_labels(pixels, intensity5, peakslout, pixelslout, peaksrout, pixelsrout, 52, 6)
plt.title('Graph of intensity (I) recorded for each pixel (p) with a longitudinal\nmagnetic field for a current of 5 A with the peaks fitted')
#plt.show()

# Calculate radii and delta r
radius_in_arr, error_in_arr = np.abs(rad_err(peakslin, errorslin, peaksrin, errorsrin))
radius_out_arr, error_out_arr = np.abs(rad_err(peakslout, errorslout, peaksrout, errorsrout))

del_radius_in, err_del_radius_in, rdr_in, err_rdr_in = delta_rad(radii_arr_0A, error_arr_0A, radius_in_arr, error_in_arr)
del_radius_out, err_del_radius_out, rdr_out, err_rdr_out = delta_rad(radii_arr_0A, error_arr_0A, radius_out_arr, error_out_arr)

# Store the radii, delta radii and rdr and their errors
radii_in_arr = np.append(radii_in_arr, radius_in_arr)
delta_radii_in_arr = np.append(delta_radii_in_arr, del_radius_in)
rdr_in_arr = np.append(rdr_in_arr, rdr_in)

err_radii_in_arr = np.append(err_radii_in_arr, error_in_arr)
err_delta_radii_in_arr = np.append(err_delta_radii_in_arr, err_del_radius_in)
err_rdr_in_arr = np.append(err_rdr_in_arr, err_rdr_in)

radii_out_arr = np.append(radii_out_arr, radius_out_arr)
delta_radii_out_arr = np.append(delta_radii_out_arr, del_radius_out)
rdr_out_arr = np.append(rdr_out_arr, rdr_out)

err_radii_out_arr = np.append(err_radii_out_arr, error_out_arr)
err_delta_radii_out_arr = np.append(err_delta_radii_out_arr, err_del_radius_out)
err_rdr_out_arr = np.append(err_rdr_out_arr, err_rdr_out)

plt.plot(rdr_in)
#plt.show()

plt.plot(rdr_out)
#plt.show()

###################
#   Fit I = 6 A   #
###################

# Fit peaks
peakl1in, pixelsl1in, errorsl1in = peak_fitting(intensity6, 866, 914, 880)
peakl1out, pixelsl1out, errorsl1out = peak_fitting(intensity6, 820, 865, 840)
peakl2in, pixelsl2in, errorsl2in = peak_fitting(intensity6, 781, 819, 800)
peakl2out, pixelsl2out, errorsl2out = peak_fitting(intensity6, 754, 783, 770)
peakl3in, pixelsl3in, errorsl3in = peak_fitting(intensity6, 725, 753, 735)
peakl3out, pixelsl3out, errorsl3out = peak_fitting(intensity6, 702, 727, 715)
peakl4in, pixelsl4in, errorsl4in = peak_fitting(intensity6, 682, 701, 690)
peakl4out, pixelsl4out, errorsl4out = peak_fitting(intensity6, 657, 681, 670)
peakl5in, pixelsl5in, errorsl5in = peak_fitting(intensity6, 640, 660, 645)
peakl5out, pixelsl5out, errorsl5out = peak_fitting(intensity6, 620, 639, 630)
peakl6in, pixelsl6in, errorsl6in = peak_fitting(intensity6, 603, 621, 610)
peakl6out, pixelsl6out, errorsl6out = peak_fitting(intensity6, 586, 602, 595)

peakr1in, pixelsr1in, errorsr1in = peak_fitting(intensity6, 1094, 1151, 1120)
peakr1out, pixelsr1out, errorsr1out = peak_fitting(intensity6, 1149, 1192, 1160)
peakr2in, pixelsr2in, errorsr2in = peak_fitting(intensity6, 1190, 1227, 1210)
peakr2out, pixelsr2out, errorsr2out = peak_fitting(intensity6, 1226, 1255, 1235)
peakr3in, pixelsr3in, errorsr3in = peak_fitting(intensity6, 1256, 1282, 1270)
peakr3out, pixelsr3out, errorsr3out = peak_fitting(intensity6, 1282, 1307, 1290)
peakr4in, pixelsr4in, errorsr4in = peak_fitting(intensity6, 1306, 1329, 1320)
peakr4out, pixelsr4out, errorsr4out = peak_fitting(intensity6, 1329, 1350, 1335)
peakr5in, pixelsr5in, errorsr5in = peak_fitting(intensity6, 1349, 1369, 1360)
peakr5out, pixelsr5out, errorsr5out = peak_fitting(intensity6, 1370, 1388, 1375)
peakr6in, pixelsr6in, errorsr6in = peak_fitting(intensity6, 1388, 1406, 1395)
peakr6out, pixelsr6out, errorsr6out = peak_fitting(intensity6, 1406, 1423, 1410)

peakslin = [peakl1in, peakl2in, peakl3in, peakl4in, peakl5in, peakl6in]
pixelslin = [pixelsl1in, pixelsl2in, pixelsl3in, pixelsl4in, pixelsl5in, pixelsl6in]
errorslin = [errorsl1in, errorsl2in, errorsl3in, errorsl4in, errorsl5in, errorsl6in]

peakslout = [peakl1out, peakl2out, peakl3out, peakl4out, peakl5out, peakl6out]
pixelslout = [pixelsl1out, pixelsl2out, pixelsl3out, pixelsl4out, pixelsl5out, pixelsl6out]
errorslout = [errorsl1out, errorsl2out, errorsl3out, errorsl4out, errorsl5out, errorsl6out]

peaksrin = [peakr1in, peakr2in, peakr3in, peakr4in, peakr5in, peakr6in]
pixelsrin = [pixelsr1in, pixelsr2in, pixelsr3in, pixelsr4in, pixelsr5in, pixelsr6in]
errorsrin = [errorsr1in, errorsr2in, errorsr3in, errorsr4in, errorsr5in, errorsr6in]

peaksrout = [peakr1out, peakr2out, peakr3out, peakr4out, peakr5out, peakr6out]
pixelsrout = [pixelsr1out, pixelsr2out, pixelsr3out, pixelsr4out, pixelsr5out, pixelsr6out]
errorsrout = [errorsr1out, errorsr2out, errorsr3out, errorsr4out, errorsr5out, errorsr6out]

# Plot data and peaks
plot_peaks(pixels, intensity6, peakslin, pixelslin, peaksrin, pixelsrin, 55, 6)
plot_peaks_no_labels(pixels, intensity6, peakslout, pixelslout, peaksrout, pixelsrout, 52, 6)
plt.title('Graph of intensity (I) recorded for each pixel (p) with a longitudinal\nmagnetic field for a current of 6 A with the peaks fitted')
#plt.show()

# Calculate radii and delta r
radius_in_arr, error_in_arr = np.abs(rad_err(peakslin, errorslin, peaksrin, errorsrin))
radius_out_arr, error_out_arr = np.abs(rad_err(peakslout, errorslout, peaksrout, errorsrout))

del_radius_in, err_del_radius_in, rdr_in, err_rdr_in = delta_rad(radii_arr_0A, error_arr_0A, radius_in_arr, error_in_arr)
del_radius_out, err_del_radius_out, rdr_out, err_rdr_out = delta_rad(radii_arr_0A, error_arr_0A, radius_out_arr, error_out_arr)

# Store the radii, delta radii and rdr and their errors
radii_in_arr = np.append(radii_in_arr, radius_in_arr)
delta_radii_in_arr = np.append(delta_radii_in_arr, del_radius_in)
rdr_in_arr = np.append(rdr_in_arr, rdr_in)

err_radii_in_arr = np.append(err_radii_in_arr, error_in_arr)
err_delta_radii_in_arr = np.append(err_delta_radii_in_arr, err_del_radius_in)
err_rdr_in_arr = np.append(err_rdr_in_arr, err_rdr_in)

radii_out_arr = np.append(radii_out_arr, radius_out_arr)
delta_radii_out_arr = np.append(delta_radii_out_arr, del_radius_out)
rdr_out_arr = np.append(rdr_out_arr, rdr_out)

err_radii_out_arr = np.append(err_radii_out_arr, error_out_arr)
err_delta_radii_out_arr = np.append(err_delta_radii_out_arr, err_del_radius_out)
err_rdr_out_arr = np.append(err_rdr_out_arr, err_rdr_out)

plt.plot(rdr_in)
#plt.show()

plt.plot(rdr_out)
plt.show()

###################
#   Fit I = 7 A   #
###################

# Fit peaks
peakl1in, pixelsl1in, errorsl1in = peak_fitting(intensity7, 874, 932, 900)
peakl1out, pixelsl1out, errorsl1out = peak_fitting(intensity7, 833, 873, 850)
peakl2in, pixelsl2in, errorsl2in = peak_fitting(intensity7, 800, 833, 810)
peakl2out, pixelsl2out, errorsl2out = peak_fitting(intensity7, 766, 797, 780)
peakl3in, pixelsl3in, errorsl3in = peak_fitting(intensity7, 742, 767, 750)
peakl3out, pixelsl3out, errorsl3out = peak_fitting(intensity7, 715, 742, 730)
peakl4in, pixelsl4in, errorsl4in = peak_fitting(intensity7, 694, 717, 705)
peakl4out, pixelsl4out, errorsl4out = peak_fitting(intensity7, 672, 696, 680)
peakl5in, pixelsl5in, errorsl5in = peak_fitting(intensity7, 653, 673, 660)
peakl5out, pixelsl5out, errorsl5out = peak_fitting(intensity7, 633, 655, 640)
peakl6in, pixelsl6in, errorsl6in = peak_fitting(intensity7, 618, 635, 625)
peakl6out, pixelsl6out, errorsl6out = peak_fitting(intensity7, 599, 617, 610)

peakr1in, pixelsr1in, errorsr1in = peak_fitting(intensity7, 1106, 1154, 1130)
peakr1out, pixelsr1out, errorsr1out = peak_fitting(intensity7, 1165, 1205, 1180)
peakr2in, pixelsr2in, errorsr2in = peak_fitting(intensity7, 1206, 1242, 1220)
peakr2out, pixelsr2out, errorsr2out = peak_fitting(intensity7, 1241, 1271, 1250)
peakr3in, pixelsr3in, errorsr3in = peak_fitting(intensity7, 1269, 1298, 1280)
peakr3out, pixelsr3out, errorsr3out = peak_fitting(intensity7, 1296, 1321, 1305)
peakr4in, pixelsr4in, errorsr4in = peak_fitting(intensity7, 1320, 1344, 1330)
peakr4out, pixelsr4out, errorsr4out = peak_fitting(intensity7, 1343, 1364, 1350)
peakr5in, pixelsr5in, errorsr5in = peak_fitting(intensity7, 1364, 1384, 1370)
peakr5out, pixelsr5out, errorsr5out = peak_fitting(intensity7, 1384, 1403, 1390)
peakr6in, pixelsr6in, errorsr6in = peak_fitting(intensity7, 1402, 1421, 1410)
peakr6out, pixelsr6out, errorsr6out = peak_fitting(intensity7, 1420, 1438, 1430)

peakslin = [peakl1in, peakl2in, peakl3in, peakl4in, peakl5in, peakl6in]
pixelslin = [pixelsl1in, pixelsl2in, pixelsl3in, pixelsl4in, pixelsl5in, pixelsl6in]
errorslin = [errorsl1in, errorsl2in, errorsl3in, errorsl4in, errorsl5in, errorsl6in]

peakslout = [peakl1out, peakl2out, peakl3out, peakl4out, peakl5out, peakl6out]
pixelslout = [pixelsl1out, pixelsl2out, pixelsl3out, pixelsl4out, pixelsl5out, pixelsl6out]
errorslout = [errorsl1out, errorsl2out, errorsl3out, errorsl4out, errorsl5out, errorsl6out]

peaksrin = [peakr1in, peakr2in, peakr3in, peakr4in, peakr5in, peakr6in]
pixelsrin = [pixelsr1in, pixelsr2in, pixelsr3in, pixelsr4in, pixelsr5in, pixelsr6in]
errorsrin = [errorsr1in, errorsr2in, errorsr3in, errorsr4in, errorsr5in, errorsr6in]

peaksrout = [peakr1out, peakr2out, peakr3out, peakr4out, peakr5out, peakr6out]
pixelsrout = [pixelsr1out, pixelsr2out, pixelsr3out, pixelsr4out, pixelsr5out, pixelsr6out]
errorsrout = [errorsr1out, errorsr2out, errorsr3out, errorsr4out, errorsr5out, errorsr6out]

# Plot data and peaks
plot_peaks(pixels, intensity7, peakslin, pixelslin, peaksrin, pixelsrin, 55, 6)
plot_peaks_no_labels(pixels, intensity7, peakslout, pixelslout, peaksrout, pixelsrout, 52, 6)
plt.title('Graph of intensity (I) recorded for each pixel (p) with a longitudinal\nmagnetic field for a current of 7 A with the peaks fitted')
plt.show()

# Calculate radii and delta r
radius_in_arr, error_in_arr = np.abs(rad_err(peakslin, errorslin, peaksrin, errorsrin))
radius_out_arr, error_out_arr = np.abs(rad_err(peakslout, errorslout, peaksrout, errorsrout))

del_radius_in, err_del_radius_in, rdr_in, err_rdr_in = delta_rad(radii_arr_0A, error_arr_0A, radius_in_arr, error_in_arr)
del_radius_out, err_del_radius_out, rdr_out, err_rdr_out = delta_rad(radii_arr_0A, error_arr_0A, radius_out_arr, error_out_arr)

# Store the radii, delta radii and rdr and their errors
radii_in_arr = np.append(radii_in_arr, radius_in_arr).reshape((4,6))
delta_radii_in_arr = np.append(delta_radii_in_arr, del_radius_in).reshape((4,6))
rdr_in_arr = np.append(rdr_in_arr, rdr_in).reshape((4,6))

err_radii_in_arr = np.abs(np.append(err_radii_in_arr, error_in_arr).reshape((4,6)))
err_delta_radii_in_arr = np.abs(np.append(err_delta_radii_in_arr, err_del_radius_in).reshape((4,6)))
err_rdr_in_arr = np.abs(np.append(err_rdr_in_arr, err_rdr_in).reshape((4,6)))

radii_out_arr = np.append(radii_out_arr, radius_out_arr).reshape((4,6))
delta_radii_out_arr = np.append(delta_radii_out_arr, del_radius_out).reshape((4,6))
rdr_out_arr = np.append(rdr_out_arr, rdr_out).reshape((4,6))

err_radii_out_arr = np.abs(np.append(err_radii_out_arr, error_out_arr).reshape((4,6)))
err_delta_radii_out_arr = np.abs(np.append(err_delta_radii_out_arr, err_del_radius_out).reshape((4,6)))
err_rdr_out_arr = np.abs(np.append(err_rdr_out_arr, err_rdr_out).reshape((4,6)))

plt.plot(rdr_in)
plt.show()

plt.plot(rdr_out)
plt.show()


output_file = open('exp3_no_polariser_output.txt','w')
output_file.write('Inner rings')

for i in range(len(radii_in_arr)):
    if i == 0:
        output_file.write('Radii,\tDelta r,\tr Delta r \n')
        output_file.write('I = '+str(i)+' A\n')
    else:
        output_file.write('I = '+str(i+4)+' A\n')
    for j in range(len(radii_in_arr[i])):
        r, err_r = round_sig_fig_uncertainty(radii_in_arr[i][j], err_radii_in_arr[i][j])
        dr, err_dr = round_sig_fig_uncertainty(delta_radii_in_arr[i][j], err_delta_radii_in_arr[i][j])
        rdr, err_rdr = round_sig_fig_uncertainty(rdr_in_arr[i][j], err_rdr_in_arr[i][j])

        output_file.write(str(j+1) + ' & ' + str(r) + '$\pm$' + str(err_r) + ' & ' + str(dr) + '$\pm$' + str(err_dr) + ' & ' + str(rdr) + '$\pm$' + str(err_rdr) + ' \\\\ \n')

output_file.write('Outer rings')

for i in range(len(radii_out_arr)):
    if i == 0:
        output_file.write('I = '+str(i)+' A\n')
    else:
        output_file.write('I = '+str(i+4)+' A\n')
    for j in range(len(radii_out_arr[i])):
        r, err_r = round_sig_fig_uncertainty(radii_out_arr[i][j], err_radii_out_arr[i][j])
        dr, err_dr = round_sig_fig_uncertainty(delta_radii_out_arr[i][j], err_delta_radii_out_arr[i][j])
        rdr, err_rdr = round_sig_fig_uncertainty(rdr_out_arr[i][j], err_rdr_out_arr[i][j])

        output_file.write(str(j+1) + ' & ' + str(r) + '$\pm$' + str(err_r) + ' & ' + str(dr) + '$\pm$' + str(err_dr) + ' & ' + str(rdr) + '$\pm$' + str(err_rdr) + ' \\\\ \n')


output_file.close()
