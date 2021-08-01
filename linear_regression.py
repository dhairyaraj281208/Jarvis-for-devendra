import pandas as pd
import plotly.express as px


def bla():

    df = pd.read_csv("data1.csv")

    height = df["Height"].tolist()
    weight = df["Weight"].tolist()

    # fig = px.scatter(x=height, y=weight)
    # fig.show()
    m = 1
    c = 0
    y = []
    for x in height:
        y_value = m*x + c
        y.append(y_value)

    # Plotting the points
    # fig = px.scatter(x=height, y=weight)
    # fig.update_layout(shapes=[
    #     dict(
    #         type='line',
    #         y0=min(y), y1=max(y),
    #         x0=min(height), x1=max(height)
    #     )
    # ])
    # # fig.show()

    m = 0.95
    c = -93
    y = []
    for x in height:
        y_value = m*x + c
        y.append(y_value)

    # Plotting the points
    # fig = px.scatter(x=height, y=weight)
    # fig.update_layout(shapes=[
    #     dict(
    #         type='line',
    #         y0=min(y), y1=max(y),
    #         x0=min(height), x1=max(height)
    #     )
    # ])
    # fig.show()
    import numpy as np
    height_array = np.array(height)
    weight_array = np.array(weight)

    # Slope and intercept using pre-built function of Numpy
    m, c = np.polyfit(height_array, weight_array, 1)

    y = []
    for x in height_array:
        y_value = m*x + c
        y.append(y_value)

    # plotting the graph
    # fig = px.scatter(x=height_array, y=weight_array)
    # fig.update_layout(shapes=[
    #     dict(
    #         type='line',
    #         y0=min(y), y1=max(y),
    #         x0=min(height_array), x1=max(height_array)
    #     )
    # ])
    # fig.show()
    x = int(input("You: "))
    y = m * x + c
    print(f"Weight of someone with height {x} is {y}")



