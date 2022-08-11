# Importing libraries
import re
import requests
import pandas as pd
import plotly.express as px
import statsmodels.formula.api as smf
import plotly.graph_objects as go




# Importing dataframe
df = pd.read_csv('https://raw.githubusercontent.com/casperrosenlof/project/main/pyhton_project.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/casperrosenlof/project/main/allcountries.csv')
df2.head()
df3 = pd.read_csv('https://raw.githubusercontent.com/casperrosenlof/project/main/happiness.csv')
df3.head()


# Cleaning Dataset
df.area = df.area.str.capitalize()


# Maps - Europe
# Average Wealth
fig1 = px.choropleth(locations=df["area"], color = df['average_wealth'].astype(float), locationmode = 'country names', color_continuous_scale = px.colors.sequential.algae)#, colorbar_title = "EUR €")
fig1.update_layout(title_text = '2019 Europe - Average Wealth per Adult', geo_scope='europe')
fig1.update_geos(projection_type="equirectangular")
fig1.show()

# DESI
fig2 = go.Figure(data=go.Choropleth(locations=df2["area"], z = df2['average_wealth'].astype(float), locationmode = 'country names', colorscale = 'Ice', reversescale=True, colorbar_title = "EUR €",))
fig2.update_layout(title_text = '2019 World - Average Wealth per Adult')
fig2.update_geos(projection_type="equirectangular")
fig2.show()




# Histograms
hist1 = px.histogram(df, x="average_wealth", nbins=15, template="simple_white", color_discrete_sequence=['seagreen'],  labels={'x':'Avarage Wealth'})
hist1.show()

hist2 = px.histogram(df2, x="average_wealth", nbins=15, template="simple_white", color_discrete_sequence=['#3D5FA8'], labels={'x':'Avarage Wealth'})
hist2.show()


# Scatter Plot - Happiness vs. Wealth
scatter1 = px.scatter(df3, x='average_wealth', y='happiness', trendline="lowess", color_discrete_sequence=['seagreen'])
scatter1.show()



# Regression - Wealth to all variable factors
reg1 = smf.ols('average_wealth ~ hdi + gdp_capita + taxation + housing_index + desi + hicp + adult_percentage', data=df)
reg1 = reg1.fit()
reg1.summary()
print(reg1.summary())

