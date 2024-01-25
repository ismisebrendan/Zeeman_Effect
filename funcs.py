import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# The function to be fit
def gaussian(x, a, b, c, d):
    return a * np.exp(-((x-b)/c)**2) + d

# Fitting data to the function
# intensity - input data
# start - start fitting from here
# end - stop fitting here
# amplitude - initial guess at a
# centre - initial guess at b
# thickness - initial guess at c
# base - initial guess at d

def peak_fitting(intensity, start, end, centre, amplitude=10, thickness=1, base=1):
    peak_range = np.arange(start,end+1,1)
    fitting = opt.curve_fit(gaussian, peak_range, intensity[peak_range], p0=[amplitude, centre, thickness, base])
    fit_params = fitting[0]
    # Standard deviation of each component
    fit_error = np.sqrt(np.diag(fitting[1]))

    return fit_params, peak_range, fit_error

# Round to the first significant figure of the uncertainty
def round_sig_fig_uncertainty(value, uncertainty):
    if uncertainty == 0:
        return value, uncertainty
    else:
        value_out = np.round(value, int(np.abs(np.floor(np.log10(uncertainty)))))
        uncertainty_out = np.round(uncertainty, int(np.abs(np.floor(np.log10(uncertainty)))))

        return value_out, uncertainty_out

def plot_peaks(pixels, data, peaksl, pixelsl, peaksr, pixelsr, max_y, spacing=2):
    # Plot data and peaks
    plt.plot(pixels, data, label='Data', color='blue', marker='.', markersize=2, linewidth=1)

    for i in range(len(peaksl)):
        # Plot
        plt.plot(pixelsl[i], gaussian(pixelsl[i], peaksl[i][0], peaksl[i][1], peaksl[i][2], peaksl[i][3]), color='red')
        plt.plot(pixelsr[i], gaussian(pixelsr[i], peaksr[i][0], peaksr[i][1], peaksr[i][2], peaksr[i][3]), color='red')
        
        # Get one red line on legend
        if i == 0:
            plt.plot(pixelsl[i], gaussian(pixelsl[i], peaksl[i][0], peaksl[i][1], peaksl[i][2], peaksl[i][3]), color='red', label='Peak fits')

        
        # Annotate
        plt.annotate("p = " + str(int(np.rint(peaksl[i][1]))), xy=(peaksl[i][1], peaksl[i][0] + peaksl[i][3]), xytext=(0, max_y-i*spacing), arrowprops=dict(arrowstyle="->"))
        plt.annotate("p = " + str(int(np.rint(peaksr[i][1]))), xy=(peaksr[i][1], peaksr[i][0] + peaksr[i][3]), xytext=(1900, max_y-i*spacing), arrowprops=dict(arrowstyle="->"))

    plt.xlabel('p')
    plt.ylabel('I (%)')
    plt.legend(loc=3)

def plot_peaks_no_labels(pixels, data, peaksl, pixelsl, peaksr, pixelsr, max_y, spacing=2):
    for i in range(len(peaksl)):
        # Plot
        plt.plot(pixelsl[i], gaussian(pixelsl[i], peaksl[i][0], peaksl[i][1], peaksl[i][2], peaksl[i][3]), color='red')
        plt.plot(pixelsr[i], gaussian(pixelsr[i], peaksr[i][0], peaksr[i][1], peaksr[i][2], peaksr[i][3]), color='red')
        
        # Annotate
        plt.annotate("p = " + str(int(np.rint(peaksl[i][1]))), xy=(peaksl[i][1], peaksl[i][0] + peaksl[i][3]), xytext=(0, max_y-i*spacing), arrowprops=dict(arrowstyle="->"))
        plt.annotate("p = " + str(int(np.rint(peaksr[i][1]))), xy=(peaksr[i][1], peaksr[i][0] + peaksr[i][3]), xytext=(1900, max_y-i*spacing), arrowprops=dict(arrowstyle="->"))

# Function to find the radii and errors
def rad_err(peaksl, errorsl, peaksr, errorsr):
    # Arrays of radii and errors
    radii_arr = np.array([])
    error_arr = np.array([])
    for i in range(len(peaksl)):
        radius = (peaksl[i][1] - peaksr[i][1])/2 * 14e-6 # metres
        error = np.sqrt(errorsl[i][1]**2 + errorsr[i][1]**2)/2 * 14e-6 # metres

        radii_arr = np.append(radii_arr, radius)
        error_arr = np.append(error_arr, error)
        
    return radii_arr, error_arr

# Find the change in radius
def delta_rad(radius0, errors0, radius_new, errors_new):
    del_radius = np.array([])
    err_del_radius = np.array([])
    rdr = np.array([])
    err_rdr = np.array([])
    
    for i in range(len(radius_new)):
        rad_diff = radius_new[i] - radius0[i]
        err_diff = np.sqrt(errors0[i]**2 + errors_new[i]**2)

        del_radius = np.append(del_radius, rad_diff)
        err_del_radius = np.append(err_del_radius, err_diff)
    
        rdr = np.append(rdr, radius_new[i]*del_radius[i])
        err_rdr = np.append(err_rdr, rdr[i] * np.sqrt((errors_new[i]/radius_new[i])**2 + (err_del_radius[i]/del_radius[i])**2))

    return del_radius, np.abs(err_del_radius), rdr, np.abs(err_rdr)