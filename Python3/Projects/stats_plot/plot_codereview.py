#! python3
from  matplotlib import pyplot as plt
from datetime import datetime as dt
from codereview_constants import FILE_NAME


def get_data():
    with open(FILE_NAME) as f:
        data = [line[:-1].split(',') for line in f]

    dates, ques, ans, perc, users, visits = zip(*data[3:])
    dates = [dt.strptime(line, '%d-%m-%Y') for line in dates]
    return dates, ques, ans, perc, users, visits


def show_plot(dates, ques, ans, perc, users, visits):
    plt.plot_date(dates, visits, '.', linestyle = '-')
    plt.grid(True)
    plt.setp(plt.xticks()[1], rotation=30)
    plt.show()


show_plot(*get_data())
