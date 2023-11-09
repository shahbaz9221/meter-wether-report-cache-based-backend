
def get_last_observation(response) -> str:
    """
    Extracts the last observation timestamp from the API response.

    Args:
    response: The API response containing weather data.

    Returns:
    str: The formatted last observation timestamp.
    """
    try:
        date_and_time = str(response.text).split('\n')[0].split()
        last_observation = f"{date_and_time[0]} at {date_and_time[1]} GMT"
        return last_observation

    except Exception as e:
        # Handle exceptions
        raise Exception(f"Error in get_last_observation: {str(e)}")



def get_wind_direction_and_velocity(data) -> str:
    """
    Extracts wind direction and velocity information from the raw data.

    Args:
    data (str): Raw data containing wind information.

    Returns:
    str: Formatted wind direction and velocity information.
    """
    try:
        direction = int(data[0:3])
        velocity = int(data[3:5])
        gust = ""

        if 'G' in data:
            gust = int(data.split('G')[1].replace("KT", ""))

        if gust:
            return f"Direction: {direction} ({velocity} knots) with {gust} knots gust."
        else:
            return f"Direction: {direction} ({velocity} knots)"

    except ValueError as ve:
        # Handle value-related errors
        raise ValueError(f"Error in get_wind_direction_and_velocity: {str(ve)}")

    except Exception as e:
        # Handle other exceptions
        raise Exception(f"Error in get_wind_direction_and_velocity: {str(e)}")



def get_temperature(data) -> str:
    """
    Extracts temperature information from the raw data.

    Args:
    data (str): Raw data containing temperature information.

    Returns:
    str: Formatted temperature information in Celsius and Fahrenheit.
    """
    try:
        temperature_h = data.split('/')[0]
        temperature_l = data.split('/')[1]

        temperature_h = int(temperature_h.replace("M", "")) * (-1) if temperature_h.startswith('M') else int(temperature_h)
        temperature_l = int(temperature_l.replace("M", "")) * (-1) if temperature_l.startswith('M') else int(temperature_l)

        temperature_fahrenheit = (temperature_h * 9/5) + 32

        return f"{temperature_h}°C ({temperature_fahrenheit}°F)"

    except ValueError as ve:
        # Handle value-related errors
        raise ValueError(f"Error in get_temperature: {str(ve)}")

    except Exception as e:
        # Handle other exceptions
        raise Exception(f"Error in get_temperature: {str(e)}")

