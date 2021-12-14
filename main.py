import matplotlib.pyplot as plt
import matplotlib.patches as pth

def plotRectangles(data, num):
    fig, ax = plt.subplots()
    for i in range(len(data)):
        x1_low = data[i][0][0]
        x1_high = data[i][0][1]
        x2_low = data[i][1][0]
        x2_high = data[i][1][1]
        if (i % num) == 0 and i != 0:
            ax.add_patch(
                pth.Rectangle((x1_low, x2_low), (x1_high - x1_low), (x2_high - x2_low),
                              linewidth=1, edgecolor='r', facecolor='none'))
        if (i % num) == 1:
            ax.add_patch(
                pth.Rectangle((x1_low, x2_low), (x1_high - x1_low), (x2_high - x2_low),
                              linewidth=1, edgecolor='b', facecolor='none'))
        if i == 0:
            ax.add_patch(
                pth.Rectangle((x1_low, x2_low), (x1_high - x1_low), (x2_high - x2_low),
                              linewidth=1, edgecolor='g', facecolor='none'))

    ax.plot()
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.legend(["Начальное приближение", "Приближение к ответу"])
    plt.show()

data1 = [[[2. / 21, 26. / 21], [-4. / 3, 2. / 3]],
        [[0.33333, 0.33333], [-0.66667, 0.33333]],
        [[2.2204 * 10 ** (-16), 0.5], [-0.5, 0.16667]],
        [[-1.1102 * 10 ** (-16), 0.5], [-0.5, 0.16667]]]

data2 = [[[2. / 21, 26. / 21], [-4. / 3, 2. / 3]],
         [[0.33333, 0.66667], [-0.66667, 0.33333]],
         [[-0.33333, 1], [-0.33333, 5.5511 * 10 ** (-17)]],
         [[2.2204 * 10 ** (-16), 0.5], [-0.5, 0.33333]],
         [[-0.33333, 1], [-0.33333, -5.5511 * 10 ** (-17)]],
         [[-1.1102e-16, 0.5], [-0.5, 0.4]],
         [[-0.25, 1], [-0.33333, -5.5511 * 10 ** (-17)]],
         [[-1.1102 * 10 ** (-16), 0.5], [-0.5, 0.4]],
         [[-0.25, 1], [-0.33333, 0]],
         [[1.1102 * 10 ** (-16), 0.5], [-0.5, 0.33333]],
         [[-0.33333, 1], [-0.33333, 0]],
         [[1.6653 * 10 ** (-16), 0.5], [-0.5, 0.33333]],
         [[-0.33333, 1], [-0.33333, 0]]]

plotRectangles(data1, 1)
plotRectangles(data2, 2)
