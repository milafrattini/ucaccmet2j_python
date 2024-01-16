import json 
from csv import DictReader

with open ("precipitation.json", encoding='utf-8') as file: 
    precipitation_list = json.load(file)

#.1 seattle station 
    station_code_seattle = "GHCND:US1WAKG0038" 
    
    seattle_measurements = []

    for dic in precipitation_list: 
        if dic["station"] == station_code_seattle: 
            seattle_measurements.append(dic) 
            dic["date"] = dic["date"].split("-") 
    
    #total precipitation per month, month and corresponding value in dictionary
    total_per_month = {}
    for dic in seattle_measurements:
        if dic["date"][1] in total_per_month:
            total_per_month[dic["date"][1]] = total_per_month[dic["date"][1]] + dic["value"]
        elif dic["date"][1] not in total_per_month: 
               total_per_month[dic["date"][1]] = dic["value"]

    #precipitation values in a list     
    results_monthly_list = []
    for key, value in total_per_month.items():
        results_monthly_list.append(value)

#.2 
    #yearly precipitation in seattle 
    total_per_year = 0 
    
    for month in results_monthly_list: 
        total_per_year = total_per_year + month

    #relative monthly precipitation 
    relative_monthly_precipitation = []
    for m in results_monthly_list:
        ratio = m / total_per_year
        relative_monthly_precipitation.append(round(ratio, 2))
    
    #writing & formatting results
    results = {
        "Seattle": {
            "station": station_code_seattle, 
            "state" : "WA",
            "total_monthly_precipitation" : results_monthly_list,
            "total_yearly_precipitation" : total_per_year, 
            "relative_monthly_precipitation" : relative_monthly_precipitation
        },
    }
    
    with open("results.json", "w") as file:
        json.dump(results, file, indent=3) 

   