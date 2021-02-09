import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot
#x,y传入你的数据。
data = [go.Bar(
            x=[],
            y=[],
            orientation = 'h'
)]
layout = go.Layout(
            title = '输入你的标题'
    )
figure = go.Figure(data = data, layout = layout)
pyplt(figure, filename='1.html')