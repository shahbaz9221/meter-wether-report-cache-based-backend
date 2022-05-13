
def get_last_observation(response) -> str:
    date_and_time = str(response.text).split('\n')[0].split()
    last_observation =   date_and_time[0] + " at " +  date_and_time[1] + " GMT"
    return last_observation


def get_wind_direction_and_velocity(data) -> str:    
    direction  = int(data[0:3])
    velocity = int(data[3:5])
    gust = ""
    
    if 'G' in data:
        gust = int(data.split('G')[1].replace("KT",""))
    
    if gust:
        return f"direction {direction} ({velocity} knot) and {gust} gust."
    else:
        return f"direction {direction} ({velocity} knot)"


def get_temperature(data) -> str:
    
    temperature_h  = data.split('/')[0]
    temperature_l  = data.split('/')[1]
    
    if temperature_h.startswith('M'):
        temperature_h = int(temperature_h.replace("M","")) * (-1)
        
    else:
        temperature_h = int(temperature_h)
    
    if temperature_l.startswith('M'):
        temperature_l = int(temperature_l.replace("M","")) * (-1)
    else:
        temperature_l = int(temperature_l)      
    
    temperature_forentheit = (temperature_h * 9/5) + 32
    return f"{temperature_h}C ({temperature_forentheit} F)"
