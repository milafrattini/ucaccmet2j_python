import json 

with open ("precipitation.json", encoding='utf-8') as file: 
    precipitation_list = json.load(file)

#.1 
    station_code_seattle = "GHCND:US1WAKG0038" 
    
    seattle_measurements = []

    for dic in precipitation_list: 
        if dic["station"] == "GHCND:US1WAKG0038": 
            seattle_measurements.append(dic) 
            dic["date"] = dic["date"].split("-") 
    
    #total precipitation per month
    total_per_month = {}
    results_monthly_list = []
    for dic in seattle_measurements:
        if dic["date"][1] in total_per_month:
            total_per_month[dic["date"][1]] = total_per_month[dic["date"][1]] + dic["value"]
        elif dic["date"][1] not in total_per_month: 
               total_per_month[dic["date"][1]] = dic["value"]

    for key, value in total_per_month.items():
        results_monthly_list.append(value)

#.2 
    total_per_year = 0 
    
    for i in results_monthly_list: 
        total_per_year = total_per_year + i

    #relative monthly precipitation 
    relative_monthly_precipitation = []
    for m in results_monthly_list:
        ratio = m / total_per_year
        relative_monthly_precipitation.append(round(ratio, 2))
    
         


