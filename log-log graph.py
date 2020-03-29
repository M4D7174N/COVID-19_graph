import matplotlib.pyplot as plt
from io import StringIO
from cycler import cycler
import csv 
import copy
import urllib.request

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
  
# initializing the titles and rows list 
countries_cumul = []
countries_new = []
countries_cumul_avg = []
countries_new_avg = []
country = []
rows = [] 
  
# reading csv file 
data = urllib.request.urlopen(url).read().decode('ascii', 'ignore')
datafile = StringIO(data)
csvReader = csv.reader(datafile)

for row in csvReader:
    rows.append(row)

for i in range(1, len(rows)):
    countries_cumul.append(list(map(int, rows[i][4:])))
    country.append(rows[i][1])

countries_new = copy.deepcopy(countries_cumul)
countries_cumul_avg = copy.deepcopy(countries_cumul)
countries_new_avg = copy.deepcopy(countries_new)

for i in range(0, len(countries_cumul)):
    countries_cumul_avg[i][0] =  0
    countries_new_avg[i][0] =  0
    for j in range (1, len(countries_cumul[i])):

            countries_new[i][j] = countries_cumul[i][j] - countries_cumul[i][j-1]
            countries_cumul_avg[i][j] =  (countries_cumul[i][j] + countries_cumul[i][j-1]) / 2
            countries_new_avg[i][j] =  (countries_new[i][j] + countries_new[i][j-1]) / 2

India_cumul = list(map(int, rows[132][4:]))
India_new = India_cumul.copy()

for i in range(1,len(India_cumul)):
    India_new[i] = India_cumul[i] - India_cumul[i-1]


plt.rc('axes', prop_cycle=(cycler('color', ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', 
    '#00ffff', '#000000', '#808080', '#800000',	'#808000',	'#008000',
    '#008080',	'#000080',	'#800080'])))
for i in range(0, len(countries_cumul)):
    if countries_cumul_avg[i][len(countries_cumul_avg[i])-1] > 5000:
        plt.plot(countries_cumul_avg[i], countries_new_avg[i], label = country[i])

# naming the x axis 
plt.xlabel('Total Infected') 
# naming the y axis 
plt.ylabel('New infected') 
  
# giving a title to my graph 
plt.title('log-log graph') 


plt.yscale("log")
plt.xscale("log")
plt.legend()
plt.savefig(r"C:\Users\Sanjeet\Documents\py_projects\COVID-19 Visual\Figure_1.png", dpi = 400)
#plt.show()