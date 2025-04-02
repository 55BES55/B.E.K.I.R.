import datetime as dt
def now():
    current_time = dt.datetime.now().strftime("%H:%M")
    print(current_time)

if __name__ == "__main__":
    now()