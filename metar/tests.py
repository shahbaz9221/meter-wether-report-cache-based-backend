# tags=tech,health,history,politics,culture,design,science,startups
import requests
data = {}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
url = "https://tgftp.nws.noaa.gov/data/observations/metar/stations/KHUL.TXT"
response = requests.get(url=url,headers=headers)
temp = str(response.text).split('\n')
# var = "KHUL 140453Z AUTO 15030G10KT 210V290 10SM M01/M05 OVC110 05/01 A2999 RMK AO2 SLP159 T00500011 401391033 COR 1725"
last_observation = temp[0].split()
last_observation =  last_observation[0] + " at " + last_observation[1] + " GMT"

# print(last_observation)
# wether_dict = {
#     'SKC': "Sky Clear",
#     "FEW": "Few 0-2 eights",
#     "SCT": "Scattered 3-4 eights",
#     "BKN": "Broken 5-7 eights",
#     "OVC": "Overcast 8 eights"
    
# }

value = var.split()
for val in value:
    if val.endswith("Z"):
        zulutime = val.replace("Z","")
        data['zulutime'] = zulutime
    
    if val.endswith('KT'):
        direction  = int(val[0:3])
        velocity = int(val[3:5])
        data['direction'] = direction
        data['velocity'] = velocity
        if 'G' in val:
            gust = int(val.split('G')[1].replace("KT",""))
            data['gust'] = gust
    
    if 'V' in val:
        wind_variability = val.split('V')
        data['wind_variablity'] = wind_variability
    
    if val.endswith("SM"):
        prevailing_visibility = int(val.replace("SM",""))
        # print("satute Miles",prevailing_visibility)
        data['prevailing_visibility'] = prevailing_visibility
    
    if val.startswith('R'):
        if '/' in val:
            runway = val.split('/')[0].replace("R","")
            position = runway[-1]
            runway = runway[:-1]
            feet = val.split('/')[1].replace("FT","")
            
            if feet.startswith("M"):
                RVR = "less than {}".format(int(feet.replace("M","")))
                data['RVR'] = RVR
                # print("RVR",RVR)
                
            if feet.startswith('P'):
                RVR = "greater than {}".format(int(feet.replace("P","")))
                # print("RVR",RVR)
                data['RVR'] = RVR
            
            
    if "CLR" == val:
        clear_sky = val
        # print("clear Sky", clear_sky)
        data['sky'] = clear_sky
    
    if "A02" == val:
        automated_observer_by_human = val
        data['automated_observer_by_human'] = automated_observer_by_human
    
    if "AUTO" == val:
        automatical_observer_by_equipment = val
        # print(automatical_observer_by_equipment)
        data['automatical_observer_by_equipment'] = automatical_observer_by_equipment
    
    if '/' in val:
        temperature_h  = val.split('/')[0]
        temperature_l  = val.split('/')[1]
        
        if temperature_h.startswith('M'):
            temperature_h = int(temperature_h.replace("M","")) * (-1)
            
        else:
            temperature_h = int(temperature_h)
        
        if temperature_l.startswith('M'):
            temperature_l = int(temperature_l.replace("M","")) * (-1)
        else:
            temperature_ = int(temperature_l)    
        # print("hight temp",temperature_h)
        # print("low temp", temperature_l)   
        temperature_forentheit = (temperature_h * 9/5) + 32.
        data['high_temperature'] = temperature_h
        data['low_temperature'] = temperature_l  
        data["temperature_forenheit"] = temperature_forentheit  
    
    if val.startswith('A') and len(val) == 5:
        altimeter_setting = int(val.replace('A',""))
        # print("altimeter settings",altimeter_setting)
        data['altimeter_settings'] = altimeter_setting
    
    if 'COR' == val:
        idx = value.index('COR')
        temp = value[idx + 1]
        if not temp.endswith('KT'):
            corrected_observation = temp
            # print(corrected_observation)
            data['corrected_observation'] = corrected_observation
            

print(data)
        
    

    
    


