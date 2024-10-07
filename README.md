## Algorithm of the Automation
<ul>
  <li>Navigates to the BBC Weather page for Sofia</li>
  <li>implements a function get_weather(driver, days) which returns the weather conditions for a given number of days. driver is a Selenium driver object and days is the number of days for which to return results.</li>
  <li>The return type is a list containing tuples of type (str, int). The first element in the tuple is the human readable name of the weather, e.g. Sunny, Thundery Shower, etc and the second element is the maximum temperature
</li>
  <li>If days is not a valid value then return None</li>
</ul>
