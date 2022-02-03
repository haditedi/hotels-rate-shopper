import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def plot_chart(x_axis,y_axis):

    plt.style.use('seaborn')

    x_axis = np.array(x_axis)

    y_axis = np.array(y_axis).astype(np.double)
    y_mask = np.isfinite(y_axis)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
    plt.plot_date(x_axis[y_mask], y_axis[y_mask], linestyle='solid', label="HOTEL M" )
    
    plt.xlabel("DATE")
    plt.ylabel("RATE (£)")
    plt.title("HOTEL RATE SHOPPER")
    plt.tight_layout()
    plt.legend()
    plt.show()