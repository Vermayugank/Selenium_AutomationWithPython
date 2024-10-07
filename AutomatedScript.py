from selenium.webdriver.common.by import By

def get_weather(driver, days):
    # Check for invalid number of days
    if days < 1 or days > 10:
        return None
    
    # Find the day elements on the page
    day_elements = driver.find_elements(By.CLASS_NAME, 'wr-day')
    
    # Verify we have enough data for the requested number of days
    if len(day_elements) < days:
        return None
    
    weather_data = []
    
    # Loop through the required number of days
    for i in range(days):
        day_element = day_elements[i]
        
        # Extract the weather description (e.g., 'Sunny', 'Thundery Shower')
        weather_description = day_element.find_element(By.CLASS_NAME, 'wr-day__weather-type-description').text
        
        # Extract the maximum temperature
        max_temp_element = day_element.find_element(By.CLASS_NAME, 'wr-day-temperature__high-value')
        max_temp = int(max_temp_element.text.replace("°", ""))  # Remove the degree symbol and convert to int
        
        # Append the tuple (weather_description, max_temp) to the weather_data list
        weather_data.append((weather_description, max_temp))
    
    return weather_data
