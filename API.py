import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import requests
url = "https://www.imf.org/external/datamapper/api/v1/NGDP_RPCH/IND"
response = requests.get(url)
a = dict(response.json())

IND= a["values"]["NGDP_RPCH"]["IND"]
print(IND)

print(IND.keys())

df = pd.DataFrame({
    'year': [x for x in IND.keys()],
    'GDP': [y for y in IND.values()]
})

print(df)

sns.lineplot(x= 'year', y = 'GDP', data=df)
plt.tick_params(axis='x', rotation = 45)
plt.show()

# POPULATION OF BHUTAN

url = "https://www.imf.org/external/datamapper/api/v1/LP/BTN"
response = requests.get(url)
a = dict(response.json())
print(a)

BTN = a['values']['LP']['BTN']
print(BTN)

df = pd.DataFrame(
    {'year': [x for x in BTN.keys()],
     'Population': [y for y in BTN.values()] 
    })

sns.barplot(x = 'year', y = 'Population', data= df,width = 0.6)
plt.xlabel("Year")
plt.ylabel("Population in millions")
plt.tick_params(axis='x', rotation = 45)
plt.show()


# Comparsion of Population in China and India 

url = "https://www.imf.org/external/datamapper/api/v1/LP/CHN/IND"
response = requests.get(url)
a = dict(response.json())
print(a)

india = a['values']['LP']['IND']
china = a['values']['LP']['CHN']

print(india)
print(china)

dfind = pd.DataFrame(
    {'YEAR': [x for x in india.keys()],
     'POPULATION': [y for y in india.values()]
     })

dfchi = pd.DataFrame(
    {'YEAR': [ a for a in china.keys()],
     'POPULATION': [b for b in china.values()]
})

print(dfind)
print(dfchi)

sns.lineplot(x ='YEAR', y = 'POPULATION', data = dfind, color = 'red')
sns.lineplot(x ='YEAR', y = 'POPULATION', data = dfchi, color = 'blue')
plt.tick_params(axis= 'x', rotation = 45)
plt.xlabel("Years")
plt.ylabel("Population in Millions")
plt.show()