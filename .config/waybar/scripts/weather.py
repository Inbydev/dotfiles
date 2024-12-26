#!/usr/bin/env python

from pyquery import PyQuery
import json

# weather icons
weather_icons = {
    "sunnyDay": "",
    "clearNight": "",
    "cloudyFoggyDay": "",
    "cloudyFoggyNight": "",
    "rainyDay": "",
    "rainyNight": "",
    "snowyIcyDay": "",
    "snowyIcyNight": "",
    "severe": "",
    "default": "",
}

# get location_id
location_id = "CIXX0020"

# get html page
url = "https://weather.com/en-IN/weather/today/l/" + location_id
html_data = PyQuery(url=url)

# current temperature
temp = html_data("span[data-testid='TemperatureValue']").eq(0).text()
temp = temp if temp else "N/A"

# current status phrase
status = html_data("div[data-testid='wxPhrase']").text()
status = f"{status[:16]}.." if status and len(status) > 17 else status or "N/A"

# status code
region_header = html_data("#regionHeader").attr("class")
status_code = "default"
if isinstance(region_header, str):  # Verify if it is a text string
    region_header_parts = region_header.split(" ")
    if len(region_header_parts) > 2:
        status_code_parts = region_header_parts[2].split("-")
        if len(status_code_parts) > 2:
            status_code = status_code_parts[2]

# status icon
icon = weather_icons.get(status_code, weather_icons["default"])

# temperature feels like
temp_feel = html_data(
    "div[data-testid='FeelsLikeSection'] > span > span[data-testid='TemperatureValue']"
).text()
temp_feel_text = f"Feels like {temp_feel}C" if temp_feel else "N/A"

# min-max temperature
temp_min = (
    html_data("div[data-testid='wxData'] > span[data-testid='TemperatureValue']")
    .eq(0)
    .text()
)
temp_max = (
    html_data("div[data-testid='wxData'] > span[data-testid='TemperatureValue']")
    .eq(1)
    .text()
)
temp_min_max = f"  {temp_min or 'N/A'}\t\t\t  {temp_max or 'N/A'}"

# wind speed
wind_data = html_data("span[data-testid='Wind']").text()
wind_speed = ""
if isinstance(wind_data, str):  # Verify if it is a text string
    wind_parts = wind_data.split("\n")
    wind_speed = wind_parts[1] if len(wind_parts) > 1 else "N/A"
wind_text = f"   {wind_speed}"

# humidity
humidity = html_data("span[data-testid='PercentageValue']").text() or "N/A"
humidity_text = f"  {humidity}"

# visibility
visibility = html_data("span[data-testid='VisibilityValue']").text() or "N/A"
visibility_text = f"   {visibility}"

# air quality index
air_quality_index = html_data("text[data-testid='DonutChartValue']").text() or "N/A"

# hourly rain prediction
prediction = html_data("section[aria-label='Hourly Forecast']")(
    "div[data-testid='SegmentPrecipPercentage'] > span"
).text()
if isinstance(prediction, str):  # Verify if it is a text string
    prediction = prediction.replace("Chance of Rain", "")
prediction = f"\n\n     (hourly) {prediction}" if len(prediction) > 0 else "N/A"

# tooltip text
tooltip_text = str.format(
    "\t\t{}\t\t\n{}\n{}\n{}\n\n{}\n{}\n{}{}",
    f'<span size="xx-large">{temp_feel or "N/A"}C</span>',
    f"<big>{icon}</big>",
    f"<big>{status}</big>",
    f"{temp_feel_text}",
    f"<big>{temp_min_max}</big>",
    f"{wind_text}\t\t{humidity_text}",
    f"{visibility_text}\tAQI {air_quality_index}",
    f"<i>{prediction}</i>",
)

# print waybar module data
out_data = {
    "text": f"{icon} {temp_feel or 'N/A'}C",
    "alt": status,
    "tooltip": tooltip_text,
    "class": status_code,
}
print(json.dumps(out_data))
