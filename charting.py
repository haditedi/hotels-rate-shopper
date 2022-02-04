import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def plot_chart(*axis):

    plt.style.use('seaborn')

    h_x_axis = np.array(axis[0])

    #USING NUMPY TO MASK SO THAT CHART WILL PLOT THROUGH MISSING DATA
    h_y_axis = np.array(axis[1]).astype(np.double)
    h_y_mask = np.isfinite(h_y_axis)

    m_y_axis = np.array(axis[2]).astype(np.double)
    m_y_mask = np.isfinite(m_y_axis)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
    plt.plot_date(h_x_axis[h_y_mask], h_y_axis[h_y_mask], linestyle='solid', label="HOTEL H" )
    plt.plot_date(h_x_axis[m_y_mask], m_y_axis[m_y_mask], linestyle='solid', label="HOTEL M" )
    
    plt.xlabel("DATE")
    plt.ylabel("RATE (£)")
    plt.title("HOTEL RATE SHOPPER")
    plt.tight_layout()
    plt.legend()
    plt.show()