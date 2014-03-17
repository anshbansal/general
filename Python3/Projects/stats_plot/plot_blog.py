#! python3
from  matplotlib import pyplot as plt
from datetime import datetime as dt
from my_blog_constants import FILE_NAME


def get_data():
    with open(FILE_NAME) as f:
        data = [line.split(',') for line in f]

    dates, ranks = zip(*data[3:])
    dates = [dt.strptime(line, '%d-%m-%Y') for line in dates]
    return dates, ranks


def show_plot(dates, ranks):
    plt.plot_date(dates, ranks, '.', linestyle = '-')
    plt.gca().invert_yaxis()
    plt.grid(True)
    plt.setp(plt.xticks()[1], rotation=30)
    plt.show()


show_plot(*get_data())
