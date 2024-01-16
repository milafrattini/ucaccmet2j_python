import json 

with open ("precipitation.json", encoding='utf-8') as file: 
    precipitation_list = json.load(file)

    station_code_seattle = "GHCND:US1WAKG0038" 
    
    seattle_measurements = []

    for dic in precipitation_list: 
        if dic["station"] == "GHCND:US1WAKG0038": 
            seattle_measurements.append(dic) 
            dic["date"] = dic["date"].split("-") 
    
    total_per_month = {}
    results_list = []
    
    for dic in seattle_measurements:
        if dic["date"][1] in total_per_month:
            total_per_month[dic["date"][1]] = total_per_month[dic["date"][1]] + dic["value"]
        elif dic["date"][1] not in total_per_month: 
               total_per_month[dic["date"][1]] = dic["value"]
    
    for key, value in total_per_month.items():
        results_list.append(value)
    
    with open("results.json", "w") as file:
        json.dump(results_list, file, indent=3) 
    

        

