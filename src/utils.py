def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours)}h:{int(minutes)}m:{int(seconds)}s"

def meters_to_kilometers(meters):
    kilometers = meters / 1000
    return f"{round(kilometers, 3)} km"
