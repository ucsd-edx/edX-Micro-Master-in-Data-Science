from datetime import date
from numpy import shape
from matplotlib.dates import MonthLocator, DateFormatter
class YearPlotter:
    def __init__(self):
        start=365*1+1
        self.dates=[date.fromordinal(i) for i in range(start,start+365)]
        self.monthsFmt = DateFormatter("%b")
        self.months = MonthLocator(range(1, 13), bymonthday=1, interval=1)

    def plot(self,T,fig,ax,label='',title=None):
        if shape(T)[0] != 365:
            raise ValueError("First dimension of T should be 365. Shape(T)="+str(shape(T)))
        ax.plot(self.dates,T,label=label);
        ax.xaxis.set_major_locator(self.months)
        ax.xaxis.set_major_formatter(self.monthsFmt)
        if not title is None:
            ax.set_title(title)
        # rotate and align the tick labels so they look better
        fig.autofmt_xdate()
        ax.grid()
        