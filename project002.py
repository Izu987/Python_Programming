"""Build a Time Calculator Project
"""
def add_time(start, duration, day=None):
    # Define list of days for reference.
    days_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    # --- Parse the start time ---
    # Split into time and period parts (AM/PM)
    time_part, period = start.split()
    start_hour_str, start_minute_str = time_part.split(':')
    start_hour = int(start_hour_str)
    start_minute = int(start_minute_str)

    # Convert start time to 24-hour format (in minutes)
    if period.upper() == "PM" and start_hour != 12:
        start_hour += 12
    if period.upper() == "AM" and start_hour == 12:
        start_hour = 0

    start_total_minutes = start_hour * 60 + start_minute

    # --- Parse the duration time ---
    dur_hour_str, dur_minute_str = duration.split(':')
    dur_hour = int(dur_hour_str)
    dur_minute = int(dur_minute_str)
    duration_total_minutes = dur_hour * 60 + dur_minute

    # --- Add duration to start time ---
    new_total_minutes = start_total_minutes + duration_total_minutes
    days_later = new_total_minutes // (24 * 60)
    new_minutes_in_day = new_total_minutes % (24 * 60)

    # --- Convert back to hours and minutes in 24-hour format ---
    new_hour_24 = new_minutes_in_day // 60
    new_minute = new_minutes_in_day % 60

    # --- Convert back to 12-hour format ---
    if new_hour_24 == 0:
        new_hour = 12
        new_period = "AM"
    elif new_hour_24 < 12:
        new_hour = new_hour_24
        new_period = "AM"
    elif new_hour_24 == 12:
        new_hour = 12
        new_period = "PM"
    else:
        new_hour = new_hour_24 - 12
        new_period = "PM"

    # Format the new time string.
    new_time = f"{new_hour}:{new_minute:02d} {new_period}"

    # --- Calculate the new day of week if provided ---
    if day:
        day_index = days_list.index(day.lower())
        new_day_index = (day_index + days_later) % 7
        new_day = days_list[new_day_index].capitalize()
        new_time += f", {new_day}"

    # --- Append information about the number of days later ---
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

# --- Testing with provided examples ---
print(add_time('3:00 PM', '7:00'))                   # 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))         # 2:02 PM, Monday
print(add_time('11:43 AM', '00:20'))                  # 12:03 PM
print(add_time('10:10 PM', '3:30'))                   # 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))       # 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))                  # 7:42 AM (9 days later)