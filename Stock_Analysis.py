
# coding: utf-8

# In[39]:

from pandas_datareader import data
import datetime
from bokeh.plotting import figure, output_file, show

start = datetime.datetime(2016,3,1)
end = datetime.datetime(2016,6,10)

df = data.DataReader(name = "GOOG",data_source = "yahoo", start = start, end = end)


def status(c,o):
    if(c > o):
        value = "Increase"
    elif(c < o):
        value = "Decrease"
    else:
        value = "Equal"
    return value

df["Status"] = [status(c,o) for c,o in zip(df.Close, df.Open)]
df["Middle"] = (df.Open + df.Close)/2
df["Height"] = abs(df.Open - df.Close)


p = figure(x_axis_type = "datetime", width= 1000, height = 300, responsive = True)
p.title.text = " Candle Stick Chart"
p.title.text_font_size='16pt'
p.xaxis.axis_label='Date'
p.yaxis.axis_label='Stock Cost'
p.grid.grid_line_alpha = 0.3

hours_12 = 12 * 60 *60 * 1000

p.segment(df.index , df.High, df.index , df.Low, color="Black")

p.rect(df.index[df.Status =="Increase"], df.Middle[df.Status =="Increase"], hours_12, df.Height[df.Status =="Increase"],fill_color="#D3D3D3",line_color="black")

p.rect(df.index[df.Status =="Decrease"], df.Middle[df.Status =="Decrease"], hours_12, df.Height[df.Status =="Decrease"],fill_color="red",line_color="black")


output_file("CS.html")

show(p)


# In[ ]:



