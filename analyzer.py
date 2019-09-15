import matplotlib.pyplot as plt
import csv





def main():
    y = []
    x = []
    filename = 'can_client.csv'
    with open(filename, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            if row[0] not in y:
                y.append(row[0])
            if (row[1]) == "RT_COOLANTTEMP1(LIM)":
                x.append(row[2])
    print(x)

    plt.plot(y, x, label='Coolant Temperatures')
    plt.xlabel('x')
    plt.ylabel('Coolant')
    plt.legend()
    plt.show()

    return


if __name__ == '__main__':
    main()
