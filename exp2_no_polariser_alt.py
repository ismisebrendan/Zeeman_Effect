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
data = ascii.read('data_exp2_not_polarised.txt')
intensity0 = data['intensity0']
intensity4 = data['intensity4']
intensity5 = data['intensity5']
intensity6 = data['intensity6']
intensity7 = data['intensity7']

# Plot together
plt.plot(pixels, intensity0, label='Current = 0 A')
plt.plot(pixels, intensity4, label='Current = 4 A')
plt.plot(pixels, intensity5, label='Current = 5 A')
plt.plot(pixels, intensity6, label='Current = 6 A')
plt.plot(pixels, intensity7, label='Current = 7 A')
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p) with a transverse magnetic field')
plt.legend()
plt.show()

# Plot separately
plt.plot(pixels, intensity4)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p)\nwith a transverse magnetic field for a current of 4 A')
plt.show()

plt.plot(pixels, intensity5)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p)\nwith a transverse magnetic field for a current of 5 A')
plt.show()

plt.plot(pixels, intensity6)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p)\nwith a transverse magnetic field for a current of 6 A')
plt.show()

plt.plot(pixels, intensity7)
plt.xlabel('p')
plt.ylabel('I (%)')
plt.title('Graph of intensity (I) recorded for each pixel (p)\nwith a transverse magnetic field for a current of 7 A')
plt.show()

###############
#   I = 0 A   #
###############

# Fit peaks
peakl1, pixelsl1, errorsl1 = peak_fitting(intensity0, 858, 931, 900)
peakl2, pixelsl2, errorsl2 = peak_fitting(intensity0, 779, 834, 800)
peakl3, pixelsl3, errorsl3 = peak_fitting(intensity0, 725, 772, 750)
peakl4, pixelsl4, errorsl4 = peak_fitting(intensity0, 686, 720, 700)
peakl5, pixelsl5, errorsl5 = peak_fitting(intensity0, 641, 682, 660)
peakl6, pixelsl6, errorsl6 = peak_fitting(intensity0, 609, 648, 630)

peakr1, pixelsr1, errorsr1 = peak_fitting(intensity0, 1103, 1178, 1130)
peakr2, pixelsr2, errorsr2 = peak_fitting(intensity0, 1197, 1254, 1220)
peakr3, pixelsr3, errorsr3 = peak_fitting(intensity0, 1255, 1308, 1280)
peakr4, pixelsr4, errorsr4 = peak_fitting(intensity0, 1302, 1351, 1330)
peakr5, pixelsr5, errorsr5 = peak_fitting(intensity0, 1352, 1386, 1370)
peakr6, pixelsr6, errorsr6 = peak_fitting(intensity0, 1387, 1425, 1410)

peaksl = [peakl1, peakl2, peakl3, peakl4, peakl5, peakl6]
pixelsl = [pixelsl1, pixelsl2, pixelsl3, pixelsl4, pixelsl5, pixelsl6]
errorsl = [errorsl1, errorsl2, errorsl3, errorsl4, errorsl5, errorsl6]

peaksr = [peakr1, peakr2, peakr3, peakr4, peakr5, peakr6]
pixelsr = [pixelsr1, pixelsr2, pixelsr3, pixelsr4, pixelsr5, pixelsr6]
errorsr = [errorsr1, errorsr2, errorsr3, errorsr4, errorsr5, errorsr6]

# Plot data and peaks
plot_peaks(pixels, intensity0, peaksl, pixelsl, peaksr, pixelsr, 40)

plt.title('Graph of intensity (I) recorded for each pixel (p) with no\ntransverse magnetic field or current present with the peaks fitted')
plt.show()

# Calculate radii and errors, and store
radii_arr_0A, error_arr_0A = np.abs(rad_err(peaksl, errorsl, peaksr, errorsr))

# Record outer, inner and middle radii
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

radii_mid_arr = np.array([radii_arr_0A])
delta_radii_mid_arr = np.array([np.zeros_like(radii_arr_0A)])
rdr_mid_arr = np.array([np.zeros_like(radii_arr_0A)])

err_radii_mid_arr = np.array([error_arr_0A])
err_delta_radii_mid_arr = np.array([np.zeros_like(radii_arr_0A)])
err_rdr_mid_arr = np.array([np.zeros_like(radii_arr_0A)])

###################
#   Fit I = 4 A   #
###################

# Fit peaks - only one peak is visible
peakl1mid, pixelsl1mid, errorsl1mid = peak_fitting(intensity4, 872, 898, 885)
peakl2mid, pixelsl2mid, errorsl2mid = peak_fitting(intensity4, 798, 809, 805)
peakl3mid, pixelsl3mid, errorsl3mid = peak_fitting(intensity4, 740, 752, 745)
peakl4mid, pixelsl4mid, errorsl4mid = peak_fitting(intensity4, 693, 706, 700)
peakl5mid, pixelsl5mid, errorsl5mid = peak_fitting(intensity4, 653, 665, 660)
peakl6mid, pixelsl6mid, errorsl6mid = peak_fitting(intensity4, 616, 626, 620)

peakr1mid, pixelsr1mid, errorsr1mid = peak_fitting(intensity4, 1136, 1154, 1144)
peakr2mid, pixelsr2mid, errorsr2mid = peak_fitting(intensity4, 1216, 1234, 1225)
peakr3mid, pixelsr3mid, errorsr3mid = peak_fitting(intensity4, 1277, 1289, 1285)
peakr4mid, pixelsr4mid, errorsr4mid = peak_fitting(intensity4, 1326, 1335, 1330)
peakr5mid, pixelsr5mid, errorsr5mid = peak_fitting(intensity4, 1366, 1378, 1370)
peakr6mid, pixelsr6mid, errorsr6mid = peak_fitting(intensity4, 1403, 1415, 1410)

peakslmid = [peakl1mid, peakl2mid, peakl3mid, peakl4mid, peakl5mid, peakl6mid]
pixelslmid = [pixelsl1mid, pixelsl2mid, pixelsl3mid, pixelsl4mid, pixelsl5mid, pixelsl6mid]
errorslmid = [errorsl1mid, errorsl2mid, errorsl3mid, errorsl4mid, errorsl5mid, errorsl6mid]

peaksrmid = [peakr1mid, peakr2mid, peakr3mid, peakr4mid, peakr5mid, peakr6mid]
pixelsrmid = [pixelsr1mid, pixelsr2mid, pixelsr3mid, pixelsr4mid, pixelsr5mid, pixelsr6mid]
errorsrmid = [errorsr1mid, errorsr2mid, errorsr3mid, errorsr4mid, errorsr5mid, errorsr6mid]

# Plot data and peaks
plot_peaks(pixels, intensity4, peakslmid, pixelslmid, peaksrmid, pixelsrmid, 40)
plt.title('Graph of intensity (I) recorded for each pixel (p) with a transverse\nmagnetic field for a current of 4 A with the peaks fitted')
plt.show()

# Calculate radii and delta r
radius_mid_arr, error_mid_arr = np.abs(rad_err(peakslmid, errorslmid, peaksrmid, errorsrmid))

del_radius_mid, err_del_radius_mid, rdr_mid, err_rdr_mid = delta_rad(radii_arr_0A, error_arr_0A, radius_mid_arr, error_mid_arr)

# Store the radii, delta radii and rdr and their errors
radii_in_arr = np.append(radii_in_arr, np.zeros_like(radii_arr_0A))
delta_radii_in_arr = np.append(delta_radii_in_arr, np.zeros_like(radii_arr_0A))
rdr_in_arr = np.append(rdr_in_arr, np.zeros_like(radii_arr_0A))

err_radii_in_arr = np.append(err_radii_in_arr, np.zeros_like(radii_arr_0A))
err_delta_radii_in_arr = np.append(err_delta_radii_in_arr, np.zeros_like(radii_arr_0A))
err_rdr_in_arr = np.append(err_rdr_in_arr, np.zeros_like(radii_arr_0A))

radii_out_arr = np.append(radii_out_arr, np.zeros_like(radii_arr_0A))
delta_radii_out_arr = np.append(delta_radii_out_arr, np.zeros_like(radii_arr_0A))
rdr_out_arr = np.append(rdr_out_arr, np.zeros_like(radii_arr_0A))

err_radii_out_arr = np.append(err_radii_out_arr, np.zeros_like(radii_arr_0A))
err_delta_radii_out_arr = np.append(err_delta_radii_out_arr, np.zeros_like(radii_arr_0A))
err_rdr_out_arr = np.append(err_rdr_out_arr, np.zeros_like(radii_arr_0A))

radii_mid_arr = np.append(radii_mid_arr, radius_mid_arr)
delta_radii_mid_arr = np.append(delta_radii_mid_arr, del_radius_mid)
rdr_mid_arr = np.append(rdr_mid_arr, rdr_mid)

err_radii_mid_arr = np.append(err_radii_mid_arr, error_mid_arr)
err_delta_radii_mid_arr = np.append(err_delta_radii_mid_arr, err_del_radius_mid)
err_rdr_mid_arr = np.append(err_rdr_mid_arr, err_rdr_mid)

###################
#   Fit I = 5 A   #
###################

# Fit peaks
peakl1mid, pixelsl1mid, errorsl1mid = peak_fitting(intensity5, 869, 896, 880)
peakl2mid, pixelsl2mid, errorsl2mid = peak_fitting(intensity5, 794, 807, 800)
peakl3mid, pixelsl3mid, errorsl3mid = peak_fitting(intensity5, 738, 750, 745)
peakl4mid, pixelsl4mid, errorsl4mid = peak_fitting(intensity5, 692, 704, 700)
peakl5mid, pixelsl5mid, errorsl5mid = peak_fitting(intensity5, 651, 664, 660)
peakl6mid, pixelsl6mid, errorsl6mid = peak_fitting(intensity5, 615, 627, 620)

peakr1mid, pixelsr1mid, errorsr1mid = peak_fitting(intensity5, 1137, 1167, 1150)
peakr2mid, pixelsr2mid, errorsr2mid = peak_fitting(intensity5, 1216, 1240, 1230)
peakr3mid, pixelsr3mid, errorsr3mid = peak_fitting(intensity5, 1276, 1296, 1290)
peakr4mid, pixelsr4mid, errorsr4mid = peak_fitting(intensity5, 1325, 1342, 1330)
peakr5mid, pixelsr5mid, errorsr5mid = peak_fitting(intensity5, 1368, 1382, 1375)
peakr6mid, pixelsr6mid, errorsr6mid = peak_fitting(intensity5, 1405, 1416, 1410)

peakl1in, pixelsl1in, errorsl1in = peak_fitting(intensity5, 891, 930, 895)
peakl1out, pixelsl1out, errorsl1out = peak_fitting(intensity5, 846, 869, 860)
peakl2in, pixelsl2in, errorsl2in = peak_fitting(intensity5, 812, 833, 815)
peakl2out, pixelsl2out, errorsl2out = peak_fitting(intensity5, 783, 797, 795)
peakl3in, pixelsl3in, errorsl3in = peak_fitting(intensity5, 751, 766, 755)
peakl3out, pixelsl3out, errorsl3out = peak_fitting(intensity5, 730, 740, 735)
peakl4in, pixelsl4in, errorsl4in = peak_fitting(intensity5, 704, 722, 705)
peakl4out, pixelsl4out, errorsl4out = peak_fitting(intensity5, 682, 693, 690)
peakl5in, pixelsl5in, errorsl5in = peak_fitting(intensity5, 662, 678, 665)
peakl5out, pixelsl5out, errorsl5out = peak_fitting(intensity5, 643, 652, 650)
peakl6in, pixelsl6in, errorsl6in = peak_fitting(intensity5, 625, 639, 625)
peakl6out, pixelsl6out, errorsl6out = peak_fitting(intensity5, 603, 617, 615)

peakr1in, pixelsr1in, errorsr1in = peak_fitting(intensity5, 1100, 1137, 1130)
peakr1out, pixelsr1out, errorsr1out = peak_fitting(intensity5, 1165, 1190, 1170)
peakr2in, pixelsr2in, errorsr2in = peak_fitting(intensity5, 1203, 1219, 1215)
peakr2out, pixelsr2out, errorsr2out = peak_fitting(intensity5, 1238, 1256, 1240)
peakr3in, pixelsr3in, errorsr3in = peak_fitting(intensity5, 1261, 1280, 1275)
peakr3out, pixelsr3out, errorsr3out = peak_fitting(intensity5, 1293, 1308, 1295)
peakr4in, pixelsr4in, errorsr4in = peak_fitting(intensity5, 1313, 1328, 1325)
peakr4out, pixelsr4out, errorsr4out = peak_fitting(intensity5, 1339, 1351, 1340)
peakr5in, pixelsr5in, errorsr5in = peak_fitting(intensity5, 1354, 1370, 1365)
peakr5out, pixelsr5out, errorsr5out = peak_fitting(intensity5, 1380, 1390, 1385)
peakr6in, pixelsr6in, errorsr6in = peak_fitting(intensity5, 1395, 1407, 1405)
peakr6out, pixelsr6out, errorsr6out = peak_fitting(intensity5, 1417, 1427, 1420)

peakslin = [peakl1in, peakl2in, peakl3in, peakl4in, peakl5in, peakl6in]
pixelslin = [pixelsl1in, pixelsl2in, pixelsl3in, pixelsl4in, pixelsl5in, pixelsl6in]
errorslin = [errorsl1in, errorsl2in, errorsl3in, errorsl4in, errorsl5in, errorsl6in]

peaksrin = [peakr1in, peakr2in, peakr3in, peakr4in, peakr5in, peakr6in]
pixelsrin = [pixelsr1in, pixelsr2in, pixelsr3in, pixelsr4in, pixelsr5in, pixelsr6in]
errorsrin = [errorsr1in, errorsr2in, errorsr3in, errorsr4in, errorsr5in, errorsr6in]

peakslout = [peakl1out, peakl2out, peakl3out, peakl4out, peakl5out, peakl6out]
pixelslout = [pixelsl1out, pixelsl2out, pixelsl3out, pixelsl4out, pixelsl5out, pixelsl6out]
errorslout = [errorsl1out, errorsl2out, errorsl3out, errorsl4out, errorsl5out, errorsl6out]

peaksrout = [peakr1out, peakr2out, peakr3out, peakr4out, peakr5out, peakr6out]
pixelsrout = [pixelsr1out, pixelsr2out, pixelsr3out, pixelsr4out, pixelsr5out, pixelsr6out]
errorsrout = [errorsr1out, errorsr2out, errorsr3out, errorsr4out, errorsr5out, errorsr6out]

peakslmid = [peakl1mid, peakl2mid, peakl3mid, peakl4mid, peakl5mid, peakl6mid]
pixelslmid = [pixelsl1mid, pixelsl2mid, pixelsl3mid, pixelsl4mid, pixelsl5mid, pixelsl6mid]
errorslmid = [errorsl1mid, errorsl2mid, errorsl3mid, errorsl4mid, errorsl5mid, errorsl6mid]

peaksrmid = [peakr1mid, peakr2mid, peakr3mid, peakr4mid, peakr5mid, peakr6mid]
pixelsrmid = [pixelsr1mid, pixelsr2mid, pixelsr3mid, pixelsr4mid, pixelsr5mid, pixelsr6mid]
errorsrmid = [errorsr1mid, errorsr2mid, errorsr3mid, errorsr4mid, errorsr5mid, errorsr6mid]


# Plot data and peaks
plot_peaks(pixels, intensity5, peakslin, pixelslin, peaksrin, pixelsrin, 40, 6)
plot_peaks_no_labels(pixels, intensity5, peakslmid, pixelslmid, peaksrmid, pixelsrmid, 38, 6)
plot_peaks_no_labels(pixels, intensity5, peakslout, pixelslout, peaksrout, pixelsrout, 36, 6)
plt.title('Graph of intensity (I) recorded for each pixel (p) with a transverse\nmagnetic field for a current of 5 A with the peaks fitted')
plt.show()

# Calculate radii and delta r
radius_arr, error_arr = np.abs(rad_err(peaksl, errorsl, peaksr, errorsr))

del_radius, err_del_radius, rdr, err_rdr = delta_rad(radii_arr_0A, error_arr_0A, radius_arr, error_arr)

# Store the radii, delta radii and rdr and their errors
radii_arr = np.append(radii_arr, radius_arr)
delta_radii_arr = np.append(delta_radii_arr, del_radius)
rdr_arr = np.append(rdr_arr, rdr)

err_radii_arr = np.append(err_radii_arr, error_arr)
err_delta_radii_arr = np.append(err_delta_radii_arr, err_del_radius)
err_rdr_arr = np.append(err_rdr_arr, err_rdr)



###################
#   Fit I = 6 A   #
###################

# Fit peaks
peakl1, pixelsl1, errorsl1 = peak_fitting(intensity6, 868, 889, 880)
peakl2, pixelsl2, errorsl2 = peak_fitting(intensity6, 793, 808, 800)
peakl3, pixelsl3, errorsl3 = peak_fitting(intensity6, 739, 750, 745)
peakl4, pixelsl4, errorsl4 = peak_fitting(intensity6, 693, 705, 700)
peakl5, pixelsl5, errorsl5 = peak_fitting(intensity6, 651, 664, 660)
peakl6, pixelsl6, errorsl6 = peak_fitting(intensity6, 615, 627, 620)

peakr1, pixelsr1, errorsr1 = peak_fitting(intensity6, 1135, 1167, 1150)
peakr2, pixelsr2, errorsr2 = peak_fitting(intensity6, 1217, 1244, 1230)
peakr3, pixelsr3, errorsr3 = peak_fitting(intensity6, 1279, 1298, 1290)
peakr4, pixelsr4, errorsr4 = peak_fitting(intensity6, 1325, 1342, 1330)
peakr5, pixelsr5, errorsr5 = peak_fitting(intensity6, 1368, 1379, 1375)
peakr6, pixelsr6, errorsr6 = peak_fitting(intensity6, 1407, 1416, 1410)

peaksl = [peakl1, peakl2, peakl3, peakl4, peakl5, peakl6]
pixelsl = [pixelsl1, pixelsl2, pixelsl3, pixelsl4, pixelsl5, pixelsl6]
errorsl = [errorsl1, errorsl2, errorsl3, errorsl4, errorsl5, errorsl6]

peaksr = [peakr1, peakr2, peakr3, peakr4, peakr5, peakr6]
pixelsr = [pixelsr1, pixelsr2, pixelsr3, pixelsr4, pixelsr5, pixelsr6]
errorsr = [errorsr1, errorsr2, errorsr3, errorsr4, errorsr5, errorsr6]

# Plot data and peaks
plot_peaks(pixels, intensity6, peaksl, pixelsl, peaksr, pixelsr, 40)
plt.title('Graph of intensity (I) recorded for each pixel (p) with a transverse\nmagnetic field for a current of 6 A with the peaks fitted')
plt.show()

# Calculate radii and delta r
radius_arr, error_arr = np.abs(rad_err(peaksl, errorsl, peaksr, errorsr))

del_radius, err_del_radius, rdr, err_rdr = delta_rad(radii_arr_0A, error_arr_0A, radius_arr, error_arr)

# Store the radii, delta radii and rdr and their errors
radii_arr = np.append(radii_arr, radius_arr)
delta_radii_arr = np.append(delta_radii_arr, del_radius)
rdr_arr = np.append(rdr_arr, rdr)

err_radii_arr = np.append(err_radii_arr, error_arr)
err_delta_radii_arr = np.append(err_delta_radii_arr, err_del_radius)
err_rdr_arr = np.append(err_rdr_arr, err_rdr)



###################
#   Fit I = 7 A   #
###################

# Fit peaks
peakl1, pixelsl1, errorsl1 = peak_fitting(intensity7, 865, 887, 880)
peakl2, pixelsl2, errorsl2 = peak_fitting(intensity7, 795, 810, 800)
peakl3, pixelsl3, errorsl3 = peak_fitting(intensity7, 740, 752, 745)
peakl4, pixelsl4, errorsl4 = peak_fitting(intensity7, 693, 705, 700)
peakl5, pixelsl5, errorsl5 = peak_fitting(intensity7, 650, 663, 655)
peakl6, pixelsl6, errorsl6 = peak_fitting(intensity7, 614, 627, 620)

peakr1, pixelsr1, errorsr1 = peak_fitting(intensity7, 1137, 1167, 1150)
peakr2, pixelsr2, errorsr2 = peak_fitting(intensity7, 1218, 1242, 1230)
peakr3, pixelsr3, errorsr3 = peak_fitting(intensity7, 1279, 1298, 1290)
peakr4, pixelsr4, errorsr4 = peak_fitting(intensity7, 1326, 1343, 1335)
peakr5, pixelsr5, errorsr5 = peak_fitting(intensity7, 1369, 1383, 1375)
peakr6, pixelsr6, errorsr6 = peak_fitting(intensity7, 1407, 1418, 1410)

peaksl = [peakl1, peakl2, peakl3, peakl4, peakl5, peakl6]
pixelsl = [pixelsl1, pixelsl2, pixelsl3, pixelsl4, pixelsl5, pixelsl6]
errorsl = [errorsl1, errorsl2, errorsl3, errorsl4, errorsl5, errorsl6]

peaksr = [peakr1, peakr2, peakr3, peakr4, peakr5, peakr6]
pixelsr = [pixelsr1, pixelsr2, pixelsr3, pixelsr4, pixelsr5, pixelsr6]
errorsr = [errorsr1, errorsr2, errorsr3, errorsr4, errorsr5, errorsr6]

# Plot data and peaks
plot_peaks(pixels, intensity7, peaksl, pixelsl, peaksr, pixelsr, 40)
plt.title('Graph of intensity (I) recorded for each pixel (p) with a transverse\nmagnetic field for a current of 7 A with the peaks fitted')
plt.show()

# Calculate radii and delta r
radius_arr, error_arr = np.abs(rad_err(peaksl, errorsl, peaksr, errorsr))

del_radius, err_del_radius, rdr, err_rdr = delta_rad(radii_arr_0A, error_arr_0A, radius_arr, error_arr)

# Store the radii, delta radii and rdr and their errors
radii_arr = np.append(radii_arr, radius_arr).reshape((5,6))
delta_radii_arr = np.append(delta_radii_arr, del_radius).reshape((5,6))
rdr_arr = np.append(rdr_arr, rdr).reshape((5,6))

err_radii_arr = np.abs(np.append(err_radii_arr, error_arr).reshape((5,6)))
err_delta_radii_arr = np.abs(np.append(err_delta_radii_arr, err_del_radius).reshape((5,6)))
err_rdr_arr = np.abs(np.append(err_rdr_arr, err_rdr).reshape((5,6)))





output_file = open('exp2_no_polariser_output.txt','w')

for i in range(len(radii_arr)):
    if i == 0:
        output_file.write('Radii,\tDelta r,\tr Delta r \n')
        output_file.write('I = '+str(i)+' A\n')
    else:
        output_file.write('I = '+str(i+3)+' A\n')
    for j in range(len(radii_arr[i])):
        r, err_r = round_sig_fig_uncertainty(radii_arr[i][j], err_radii_arr[i][j])
        dr, err_dr = round_sig_fig_uncertainty(delta_radii_arr[i][j], err_delta_radii_arr[i][j])
        rdr, err_rdr = round_sig_fig_uncertainty(rdr_arr[i][j], err_rdr_arr[i][j])

        output_file.write(str(j+1) + ' & ' + str(r) + '$\pm$' + str(err_r) + ' & ' + str(dr) + '$\pm$' + str(err_dr) + ' & ' + str(rdr) + '$\pm$' + str(err_rdr) + ' \\\\ \n')

output_file.close()
