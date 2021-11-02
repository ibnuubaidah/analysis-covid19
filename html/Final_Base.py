import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import calendar
sns.set()

df = pd.read_csv("/Volumes/File/ProjectFGA/html/static/dataset/covid_19_indonesia_time_series_all.csv")
df_copy = df.copy()

#Cleaning Part
df_clean = df_copy.drop(columns=['City or Regency', 'Name', 'Item', 'Kind', 'Hidden', 'Special Status', 'Location ISO Code', 
    'Country', 'Continent', 'Location Level', 'Time Zone', 'Total Regencies', 'Total Cities', 'Total Districts', 'Total Rural Villages', 
    'Total Urban Villages', 'Area (km2)', 'Population Density', 'Longitude', 'Latitude', 'New Cases per Million', 'Total Cases per Million', 
    'New Deaths per Million', 'Total Deaths per Million', 'New Active Cases', 'Total Active Cases', 'Location'])
# print(df_clean.info())

df_clean = df_clean.dropna()
#df_clean.duplicated().sum() = 0

# print(df_clean.info())

#Changing date type to Datetime
df_clean['Date'] = pd.to_datetime(df_clean['Date'], format='%m/%d/%Y')
time_series = df_clean.loc[(df_clean['Date'] >= '1/1/2021')].reset_index(drop=True)
# print(time_series.head())

#START GROUPING
days = time_series.groupby('Date')[['New Cases', 'New Deaths', 'New Recovered']].sum().reset_index()
# print(days.head())

#Per-Days
figdays = plt.figure(figsize=(20, 8))
sns.lineplot(days['Date'], days['New Cases'], color='yellow', label="New Cases", lw=3)
sns.lineplot(days['Date'], days['New Recovered'], color='green', label="New Recovered", lw=3)
sns.lineplot(days['Date'], days['New Deaths'], color='red', label="New Deaths", lw=3)
plt.ylabel('Jumlah Kasus')
plt.xlabel("Bulan")
plt.legend()
# plt.show()
figdays.savefig('static/images/perhari.jpeg', dpi = 300)
days = days.rename(columns = {'New Cases':'Cases', 'New Deaths':'Deaths', 'New Recovered':'Recovered'})
days.to_csv("static/tables/days.csv", index=False)

time_series['Month'] = time_series['Date'].dt.month

jan = time_series[time_series['Month'] == 1]
feb = time_series[time_series['Month'] == 2]
mar = time_series[time_series['Month'] == 3]
apr = time_series[time_series['Month'] == 4]
mei = time_series[time_series['Month'] == 5]
jun = time_series[time_series['Month'] == 6]
jul = time_series[time_series['Month'] == 7]

jan_total = jan.groupby('Date')[['New Cases', 'New Deaths', 'New Recovered']].sum()
jan_total.reset_index(inplace=True)
feb_total = feb.groupby('Date')[['New Cases', 'New Deaths', 'New Recovered']].sum()
feb_total.reset_index(inplace=True)
mar_total = mar.groupby('Date')[['New Cases', 'New Deaths', 'New Recovered']].sum()
mar_total.reset_index(inplace=True)
apr_total = apr.groupby('Date')[['New Cases', 'New Deaths', 'New Recovered']].sum()
apr_total.reset_index(inplace=True)
mei_total = mei.groupby('Date')[['New Cases', 'New Deaths', 'New Recovered']].sum()
mei_total.reset_index(inplace=True)
jun_total = jun.groupby('Date')[['New Cases', 'New Deaths', 'New Recovered']].sum()
jun_total.reset_index(inplace=True)
jul_total = jul.groupby('Date')[['New Cases', 'New Deaths', 'New Recovered']].sum()
jul_total.reset_index(inplace=True)

#January
figjan = plt.figure(figsize=(20, 8))
sns.lineplot(jan_total['Date'], jan_total['New Cases'], color='yellow', label="New Cases", lw=3)
sns.lineplot(jan_total['Date'], jan_total['New Recovered'], color='green', label="New Recovered", lw=3)
sns.lineplot(jan_total['Date'], jan_total['New Deaths'], color='red', label="New Deaths", lw=3)
plt.axvline(pd.Timestamp("2021-1-11"), lw=3)
plt.axvline(pd.Timestamp("2021-1-25"),lw=3)
plt.ylabel('Jumlah Kasus')
plt.xlabel("Tanggal")
plt.legend()
# plt.show()
figjan.savefig('static/images/januari.jpeg', dpi = 300)

#February
figfeb = plt.figure(figsize=(20, 8))
sns.lineplot(feb_total['Date'], feb_total['New Cases'], color='yellow', label="New Cases", lw=3)
sns.lineplot(feb_total['Date'], feb_total['New Recovered'], color='green', label="New Recovered", lw=3)
sns.lineplot(feb_total['Date'], feb_total['New Deaths'], color='red', label="New Deaths", lw=3)
plt.axvline(pd.Timestamp("2021-2-8"), lw=3)
plt.ylabel('Jumlah Kasus')
plt.xlabel("Tanggal")
plt.legend()
# plt.show()
figfeb.savefig('static/images/februari.jpeg', dpi = 300)

#March
figmar = plt.figure(figsize=(20, 8))
sns.lineplot(mar_total['Date'], mar_total['New Cases'], color='yellow', label="New Cases", lw=3)
sns.lineplot(mar_total['Date'], mar_total['New Recovered'], color='green', label="New Recovered", lw=3)
sns.lineplot(mar_total['Date'], mar_total['New Deaths'], color='red', label="New Deaths", lw=3)
plt.ylabel('Jumlah Kasus')
plt.xlabel("Tanggal")
plt.legend()
# plt.show()
figmar.savefig('static/images/maret.jpeg', dpi = 300)

#April
figapr = plt.figure(figsize=(20, 8))
sns.lineplot(apr_total['Date'], apr_total['New Cases'], color='yellow', label="New Cases", lw=3)
sns.lineplot(apr_total['Date'], apr_total['New Recovered'], color='green', label="New Recovered", lw=3)
sns.lineplot(apr_total['Date'], apr_total['New Deaths'], color='red', label="New Deaths", lw=3)
plt.ylabel('Jumlah Kasus')
plt.xlabel("Tanggal")
plt.legend()
# plt.show()
figapr.savefig('static/images/april.jpeg', dpi = 300)

#Mei
figmei = plt.figure(figsize=(20, 8))
sns.lineplot(mei_total['Date'], mei_total['New Cases'], color='yellow', label="New Cases", lw=3)
sns.lineplot(mei_total['Date'], mei_total['New Recovered'], color='green', label="New Recovered", lw=3)
sns.lineplot(mei_total['Date'], mei_total['New Deaths'], color='red', label="New Deaths", lw=3)
plt.ylabel('Jumlah Kasus')
plt.xlabel("Tanggal")
plt.legend()
# plt.show()
figmei.savefig('static/images/mei.jpeg', dpi = 300)

#Juny
figjun = plt.figure(figsize=(20, 8))
sns.lineplot(jun_total['Date'], jun_total['New Cases'], color='yellow', label="New Cases", lw=3)
sns.lineplot(jun_total['Date'], jun_total['New Recovered'], color='green', label="New Recovered", lw=3)
sns.lineplot(jun_total['Date'], jun_total['New Deaths'], color='red', label="New Deaths", lw=3)
plt.axvline(pd.Timestamp("2021-6-28"), lw=3)
plt.ylabel('Jumlah Kasus')
plt.xlabel("Tanggal")
plt.legend()
# plt.show()
figjun.savefig('static/images/juni.jpeg', dpi = 300)

#July
figjul = plt.figure(figsize=(20, 8))
sns.lineplot(jul_total['Date'], jul_total['New Cases'], color='yellow', label="New Cases", lw=3)
sns.lineplot(jul_total['Date'], jul_total['New Recovered'], color='green', label="New Recovered", lw=3)
sns.lineplot(jul_total['Date'], jul_total['New Deaths'], color='red', label="New Deaths", lw=3)
plt.ylabel('Jumlah Kasus')
plt.xlabel("Tanggal")
plt.legend()
# plt.show()
figjul.savefig('static/images/juli.jpeg', dpi = 300)

#New Total Cases per-Month
per_month = time_series.groupby("Month")[['New Cases', 'New Recovered', 'New Deaths']].sum()
per_month.reset_index(inplace = True)
#Make new column for named month
per_month['Month'] = per_month['Month'].apply(lambda x: calendar.month_abbr[x]) 

figmonth = plt.figure(figsize=(20, 8))
plt.plot(per_month['Month'], per_month['New Cases'], color='yellow', label="New Cases", lw= 3)
plt.plot(per_month['Month'], per_month['New Recovered'], color='green', label="New Recovered", lw=3)
plt.plot(per_month['Month'], per_month['New Deaths'], color='red', label="New Deaths", lw=3)
plt.ylabel('Jumlah Kasus')
plt.xlabel("Bulan")
plt.legend()
# plt.plot()
figmonth.savefig('static/images/perbulan.jpeg', dpi = 300)
per_month = per_month.rename(columns = {'New Cases':'Cases', 'New Deaths':'Deaths', 'New Recovered':'Recovered'})
per_month.to_csv('static/tables/months.csv', index=False)

figmonth_cases = plt.figure(figsize=(20, 8))
plt.plot(per_month['Month'], per_month['Cases'], color='yellow', label="New Cases", lw= 3)
plt.ylabel('Jumlah Kasus')
plt.xlabel("Bulan")
plt.legend()
# plt.plot()
figmonth_cases.savefig('static/images/kasusperbulan.jpeg', dpi = 300)

figmonth_recovered = plt.figure(figsize=(20, 8))
plt.plot(per_month['Month'], per_month['Recovered'], color='green', label="New Recovered", lw=3)
plt.ylabel('Jumlah Kasus')
plt.xlabel("Bulan")
plt.legend()
# plt.plot()
figmonth_recovered.savefig('static/images/sembuhperbulan.jpeg', dpi = 300)

figmonth_deaths = plt.figure(figsize=(20, 8))
plt.plot(per_month['Month'], per_month['Deaths'], color='red', label="New Deaths", lw=3)
plt.ylabel('Jumlah Kasus')
plt.xlabel("Bulan")
plt.legend()
# plt.plot()
figmonth_deaths.savefig('static/images/matiperbulan.jpeg', dpi = 300)

#By Province
df_group = df_clean.groupby('Island')[['New Cases', 'New Deaths', 'New Recovered']].sum()

new_group = df_clean.groupby(['Island','Province'])[['New Cases', 'New Deaths', 'New Recovered']].sum()
new_group.reset_index(inplace=True)
new_group.set_index('New Cases', inplace = True)
new_group.sort_values(by="New Cases", ascending=False, inplace=True)
new_group.reset_index(inplace=True)

fig_province = plt.figure(figsize=(20, 8))

plt.bar(new_group['Province'], new_group['New Cases'], color='yellow', label='New Cases');
plt.bar(new_group['Province'], new_group['New Recovered'], color = 'green', label='New Recovered');
plt.bar(new_group['Province'], new_group['New Deaths'], color = 'red', label='New Deaths' );
plt.xlabel('Provinsi')
plt.ylabel('Jumlah Kasus')
plt.legend()
plt.xticks(rotation=90)
fig_province.savefig('static/images/perprovinsi.jpg', dpi = 300)
new_group = new_group.rename(columns = {'New Cases':'Cases', 'New Deaths':'Deaths', 'New Recovered':'Recovered'})
new_group.to_csv('static/tables/province.csv', index=False)