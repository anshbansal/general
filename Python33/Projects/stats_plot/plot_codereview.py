#! python3
from  matplotlib import pyplot as plt
from datetime import datetime as dt
from codereview_constants import FILE_NAME


def get_data():
    with open(FILE_NAME) as f:
        data = [line for line in f]

    data = [line[:-1].split(',') for line in data[3:]]

    dates = [dt.strptime(line[0], '%d-%m-%Y') for line in data]
    ques = [int(line[1]) for line in data]
    ans =  [int(line[2]) for line in data]
    perc = [int(line[3]) for line in data]
    users = [int(line[4]) for line in data]
    visits = [int(line[5]) for line in data]

    return dates, ques, ans, perc, users, visits


def show_plot(dates, ques, ans, perc, users, visits):
    plt.plot_date(dates, visits, '.', linestyle = '-')
    plt.grid(True)
    plt.setp(plt.xticks()[1], rotation=30)
    plt.show()


show_plot(*get_data())
