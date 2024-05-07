from datetime import datetime, timedelta

# Your current time in California (PST or PDT, UTC-8 or UTC-7 depending on Daylight Saving)
california_time = datetime.strptime("14:12", "%H:%M")

# The time difference you're looking for
time_difference = timedelta(hours=7)

# The time in the other time zone
other_time_zone_time = california_time + time_difference

# Print the result
time = other_time_zone_time.strftime("%H:%M")
print(time)