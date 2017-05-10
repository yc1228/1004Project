
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from scipy.stats.stats import pearsonr
import plotly.plotly as py
import plotly.graph_objs as go 
import plotly 
plotly.offline.init_notebook_mode()


from plotly import tools
import matplotlib.pyplot as plt

'''Calculate Correlation Between Two Variables'''
def calc_corr(s1,s2):
    return(pearsonr(s1,s2)[0])

'''Calculate correlation between poverty rate and crime rate'''
ind1 = [2,4,5,6,7,8,9]
p = [float(i) for i in poverty['Staten Island'].loc[ind1]]
corr_Bronx = calc_corr(df_Bronx['Count'],poverty['Bronx'])
corr_Brook = calc_corr(df_Brooklyn['Count'],poverty['Brooklyn'])
corr_Queens = calc_corr(df_Queens['Count'],poverty['Queens'])
corr_Manhattan = calc_corr(df_Manhattan['Count'],poverty['Manhattan'])
corr_SI = calc_corr(df_SI['Count'],p)
print(corr_Bronx,corr_Brook,corr_Queens,corr_Manhattan,corr_SI)

'''Function that plots poverty vs. crime'''
def plot_corr(x,s1,s2,borough):
    trace1 = go.Scatter(
        x=x,
        y=s1,
        name='Crime Count'
    )
    trace2 = go.Scatter(
        x=x,
        y=s2,
        name='Poverty Rate',
        yaxis='y2'
    )
    data = [trace1, trace2]
    layout = go.Layout(
        title='Poverty Rate vs. Crime Count_'+borough,
        yaxis=dict(
            title='Crime Count'
        ),
        yaxis2=dict(
            title='Poverty Rate',
            titlefont=dict(
                color='rgb(148, 103, 189)'
            ),
            tickfont=dict(
                color='rgb(148, 103, 189)'
            ),
            overlaying='y',
            side='right'
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.iplot(fig)


def plot_poverty(borough_name):
    new_data=df[df['borough']==borough_name.upper()]
    trace1 = go.Bar(x=poverty['Year'], y=poverty[borough_name],name = str(borough_name)+' Poverty rate',yaxis='y',opacity = 0.5)
    trace2 = go.Scatter(x=poverty['Year'], y=df['Count'],name = str(borough_name)+' Crime Count',yaxis='y2',mode = 'lines+markers',opacity = 0.9)
    data=[trace1,trace2]
    layout = go.Layout(title = 'Time Series Plot for '+str(borough_name)+' Crime Count Vs. Poverty Rate', annotations=[
        dict(x=xi,y=yi,
             text=str(int(yi))+'%',
             xanchor='center',
             yanchor='bottom',
             showarrow=False,
        ) for xi, yi in zip(poverty['Year'], poverty[borough_name])],yaxis=dict(title='poverty rate'),yaxis2=dict(title='Crime Count', overlaying='y',side='right'))
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.iplot(fig)


'''Plot Temperature vs. Crime Type for Year 2006~2015'''
hover_text_06 = []
bubble_size_06 = []

for ind in df_06.index:
    hover_text_06.append(('Crime Type: {crime}<br>'+
                      'Number of Crimes: {Count}<br>'+
                      'Temp_bin: {Temp_bin}<br>'+
                      'Year: {year}').format(crime=df_06.loc[ind]['crime'],
                                            Count=df_06.loc[ind]['Count'],
                                            Temp_bin=df_06.loc[ind]['Temp_bin'],
                                            year=2006))
    bubble_size_06.append(math.sqrt(df_06.loc[ind]['Count']))

df_06['text'] = hover_text_06
df_06['size'] = bubble_size_06

hover_text_07 = []
bubble_size_07 = []

for ind in df_07.index:
    hover_text_07.append(('Crime Type: {crime}<br>'+
                      'Number of Crimes: {Count}<br>'+
                      'Temp_bin: {Temp_bin}<br>'+
                      'Year: {year}').format(crime=df_07.loc[ind]['crime'],
                                            Count=df_07.loc[ind]['Count'],
                                            Temp_bin=df_07.loc[ind]['Temp_bin'],
                                            year=2007))
    bubble_size_07.append(math.sqrt(df_07.loc[ind]['Count']))

df_07['text'] = hover_text_07
df_07['size'] = bubble_size_07

hover_text_08 = []
bubble_size_08 = []

for ind in df_08.index:
    hover_text_08.append(('Crime Type: {crime}<br>'+
                      'Number of Crimes: {Count}<br>'+
                      'Temp_bin: {Temp_bin}<br>'+
                      'Year: {year}').format(crime=df_08.loc[ind]['crime'],
                                            Count=df_08.loc[ind]['Count'],
                                            Temp_bin=df_08.loc[ind]['Temp_bin'],
                                            year=2008))
    bubble_size_08.append(math.sqrt(df_08.loc[ind]['Count']))

df_08['text'] = hover_text_08
df_08['size'] = bubble_size_08

hover_text_09 = []
bubble_size_09 = []

for ind in df_09.index:
    hover_text_09.append(('Crime Type: {crime}<br>'+
                      'Number of Crimes: {Count}<br>'+
                      'Temp_bin: {Temp_bin}<br>'+
                      'Year: {year}').format(crime=df_09.loc[ind]['crime'],
                                            Count=df_09.loc[ind]['Count'],
                                            Temp_bin=df_09.loc[ind]['Temp_bin'],
                                            year=2009))
    bubble_size_09.append(math.sqrt(df_09.loc[ind]['Count']))

df_09['text'] = hover_text_09
df_09['size'] = bubble_size_09

hover_text_10 = []
bubble_size_10 = []

for ind in df_10.index:
    hover_text_10.append(('Crime Type: {crime}<br>'+
                      'Number of Crimes: {Count}<br>'+
                      'Temp_bin: {Temp_bin}<br>'+
                      'Year: {year}').format(crime=df_10.loc[ind]['crime'],
                                            Count=df_10.loc[ind]['Count'],
                                            Temp_bin=df_10.loc[ind]['Temp_bin'],
                                            year=2010))
    bubble_size_10.append(math.sqrt(df_10.loc[ind]['Count']))

df_10['text'] = hover_text_10
df_10['size'] = bubble_size_10

hover_text_11 = []
bubble_size_11 = []

for ind in df_11.index:
    hover_text_11.append(('Crime Type: {crime}<br>'+
                      'Number of Crimes: {Count}<br>'+
                      'Temp_bin: {Temp_bin}<br>'+
                      'Year: {year}').format(crime=df_11.loc[ind]['crime'],
                                            Count=df_11.loc[ind]['Count'],
                                            Temp_bin=df_11.loc[ind]['Temp_bin'],
                                            year=2011))
    bubble_size_11.append(math.sqrt(df_11.loc[ind]['Count']))

df_11['text'] = hover_text_11
df_11['size'] = bubble_size_11

hover_text_12 = []
bubble_size_12 = []

for ind in df_12.index:
    hover_text_12.append(('Crime Type: {crime}<br>'+
                      'Number of Crimes: {Count}<br>'+
                      'Temp_bin: {Temp_bin}<br>'+
                      'Year: {year}').format(crime=df_12.loc[ind]['crime'],
                                            Count=df_12.loc[ind]['Count'],
                                            Temp_bin=df_12.loc[ind]['Temp_bin'],
                                            year=2012))
    bubble_size_12.append(math.sqrt(df_12.loc[ind]['Count']))

df_12['text'] = hover_text_12
df_12['size'] = bubble_size_12

hover_text_13 = []
bubble_size_13 = []

for ind in df_13.index:
    hover_text_13.append(('Crime Type: {crime}<br>'+
                      'Number of Crimes: {Count}<br>'+
                      'Temp_bin: {Temp_bin}<br>'+
                      'Year: {year}').format(crime=df_13.loc[ind]['crime'],
                                            Count=df_13.loc[ind]['Count'],
                                            Temp_bin=df_13.loc[ind]['Temp_bin'],
                                            year=2013))
    bubble_size_13.append(math.sqrt(df_13.loc[ind]['Count']))

df_13['text'] = hover_text_13
df_13['size'] = bubble_size_13

hover_text_14 = []
bubble_size_14 = []

for ind in df_14.index:
    hover_text_14.append(('Crime Type: {crime}<br>'+
                      'Number of Crimes: {Count}<br>'+
                      'Temp_bin: {Temp_bin}<br>'+
                      'Year: {year}').format(crime=df_14.loc[ind]['crime'],
                                            Count=df_14.loc[ind]['Count'],
                                            Temp_bin=df_14.loc[ind]['Temp_bin'],
                                            year=2014))
    bubble_size_14.append(math.sqrt(df_14.loc[ind]['Count']))

df_14['text'] = hover_text_14
df_14['size'] = bubble_size_14

hover_text_15 = []
bubble_size_15 = []

for ind in df_15.index:
    hover_text_15.append(('Crime Type: {crime}<br>'+
                      'Number of Crimes: {Count}<br>'+
                      'Temp_bin: {Temp_bin}<br>'+
                      'Year: {year}').format(crime=df_15.loc[ind]['crime'],
                                            Count=df_15.loc[ind]['Count'],
                                            Temp_bin=df_15.loc[ind]['Temp_bin'],
                                            year=2015))
    bubble_size_15.append(math.sqrt(df_15.loc[ind]['Count']))

df_15['text'] = hover_text_15
df_15['size'] = bubble_size_15

trace0 = go.Scatter(
    x=df_06['crime'],
    y=df_06['Temp_bin'],
    mode='markers',
    name='2006',
    text=df_06['text'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_06['size'],
        line=dict(
            width=2
        ),
    )
)

trace1 = go.Scatter(
    x=df_07['crime'],
    y=df_07['Temp_bin'],
    mode='markers',
    name='2007',
    text=df_07['text'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_07['size'],
        line=dict(
            width=2
        ),
    )
)
trace2 = go.Scatter(
    x=df_08['crime'],
    y=df_08['Temp_bin'],
    mode='markers',
    name='2008',
    text=df_08['text'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_07['size'],
        line=dict(
            width=2
        ),
    )
)

trace3 = go.Scatter(
    x=df_09['crime'],
    y=df_09['Temp_bin'],
    mode='markers',
    name='2009',
    text=df_09['text'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_07['size'],
        line=dict(
            width=2
        ),
    )
)

trace4 = go.Scatter(
    x=df_10['crime'],
    y=df_10['Temp_bin'],
    mode='markers',
    name='2010',
    text=df_07['text'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_07['size'],
        line=dict(
            width=2
        ),
    )
)

trace5 = go.Scatter(
    x=df_11['crime'],
    y=df_11['Temp_bin'],
    mode='markers',
    name='2011',
    text=df_11['text'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_07['size'],
        line=dict(
            width=2
        ),
    )
)

trace6 = go.Scatter(
    x=df_12['crime'],
    y=df_12['Temp_bin'],
    mode='markers',
    name='2012',
    text=df_12['text'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_07['size'],
        line=dict(
            width=2
        ),
    )
)

trace7 = go.Scatter(
    x=df_13['crime'],
    y=df_13['Temp_bin'],
    mode='markers',
    name='2013',
    text=df_13['text'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_07['size'],
        line=dict(
            width=2
        ),
    )
)

trace8 = go.Scatter(
    x=df_14['crime'],
    y=df_14['Temp_bin'],
    mode='markers',
    name='2014',
    text=df_14['text'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_07['size'],
        line=dict(
            width=2
        ),
    )
)

trace9 = go.Scatter(
    x=df_15['crime'],
    y=df_15['Temp_bin'],
    mode='markers',
    name='2015',
    text=df_15['text'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=df_07['size'],
        line=dict(
            width=2
        ),
    )
)

layout = go.Layout(
    title='Temperature vs. Crime',
    xaxis=dict(
        autotick=True,
        tickangle=45,
        title='Crime Type',
        gridcolor='rgb(255, 255, 255)',
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
        tickfont=dict(
            family='Old Standard TT, serif',
            size=10,
            color='black'
        )
    ),
    yaxis=dict(
        title='Temperature_Bin',
        gridcolor='rgb(255, 255, 255)',
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
        range=[0,8]
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)

data=[trace0,trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8,trace9]
fig = go.Figure(data=data,layout=layout)
plotly.offline.iplot(fig)
