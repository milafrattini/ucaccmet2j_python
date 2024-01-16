#.3 all of the above, for each station 
import json 
from csv import DictReader

with open ("precipitation.json", encoding='utf-8') as file: 
    precipitation_list = json.load(file)

with open('stations.csv') as file:
    reader = DictReader(file)
    stations = list(reader)

total_per_year = []
results = { } 

#looping through list of stations
for station in stations: 

    measurements = []

    #code per current station 
    for dic in precipitation_list: 
        if dic["station"] == station["Station"]: 
            measurements.append(dic) 
            dic["date"] = dic["date"].split("-") 
  
    #month with corresponding total precipitation value (dictionary)   
    total_per_month = {}
    for dic in measurements:
        if dic["date"][1] in total_per_month:
            total_per_month[dic["date"][1]] = total_per_month[dic["date"][1]] + dic["value"]
        elif dic["date"][1] not in total_per_month: 
               total_per_month[dic["date"][1]] = dic["value"]

    #monthly precipitation (dictionary to list)
    results_monthly_list = []
    for key, value in total_per_month.items():
        results_monthly_list.append(value)

    #total precipitation in a year
    total_per_year_per_location = 0 
    for month_value in results_monthly_list: 
        total_per_year_per_location = total_per_year_per_location + month_value

    #relative monthly precipitation 
    relative_monthly_precipitation = []
    for month_value in results_monthly_list:
        ratio = month_value / total_per_year_per_location
        relative_monthly_precipitation.append(round(ratio, 2))
    
    #relative yearly precipitation 
        
    #writing & formatting results
    results[station["Location"]] = {
            "station": station["Station"], 
            "state" : station["State"],
            "total_monthly_precipitation" : results_monthly_list,
            "total_yearly_precipitation" : total_per_year_per_location, 
            "relative_monthly_precipitation" : relative_monthly_precipitation

        }
    
    with open("results.json", "w") as file:
        json.dump(results, file, indent=3) 

   