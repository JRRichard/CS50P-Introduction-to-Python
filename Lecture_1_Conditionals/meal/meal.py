def main():
    # Ask user for time
    time_check = input("What time is it? ")
    if time_check.endswith("a.m."):
        meal_time = convert(time_check.removesuffix("a.m."))
    elif time_check.endswith("p.m."):
        meal_time = convert(time_check.removesuffix("p.m."))
    else:
        meal_time = convert (time_check)

    # Define meal time based on converted time
    if 18.0 <= meal_time <= 19.0 or meal_time==7.0 and time_check.endswith("p.m."):
        print ("dinner time")
    elif 7.0 <= meal_time <= 8.0:
        print ("breakfast time")
    elif 12.0 <= meal_time <= 13.0:
        print ("lunch time")
    


def convert(time):
    hour, fraction =  time.split(":")
    sub = float(hour) + float(fraction)/60
    return sub


if __name__ == "__main__":
    main()
