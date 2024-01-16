import json 

with open ("precipitation.json", encoding='utf-8') as file: 
    precipitation_list = json.load(file)

#.1 seattle
    stations = {}
    total_per_station = {}
    total_per_month= {}

    for dic in precipitation_list: 
            dic["date"] = dic["date"].split("-") 
            if dic["station"] not in stations: 
                stations["station"] = (dic["station"]) 
                if dic["station"] not in total_per_station: 
                    if dic["date"][1] in total_per_month:
                        total_per_month[dic["date"][1]] = total_per_month[dic["date"][1]] + dic["value"]
                        stations["monthly_precipitation"] = total_per_month
                elif dic["date"][1] not in total_per_month: 
                    total_per_month[dic["date"][1]] = dic["value"]
            elif dic["station"] in stations:
                total_per_month[dic["date"][1]] = total_per_month[dic["date"][1]] + dic["value"]
                stations["monthly_precipitation"] = total_per_month
    
    print(stations)
    
    #total precipitation per month
    
    