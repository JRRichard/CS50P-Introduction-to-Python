import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    try:
        matches = re.search(r"^([0-9]*[0-9])*:?(\d[0-9]*)* ([A|P])[M] to ([0-9]*[0-9])*:?(\d[0-9]*)* ([A|P])[M]$", s)
        if matches:
            start_hour = int(matches.group(1))
            end_hour = int(matches.group(4))

            if start_hour > 12 or end_hour > 12:
                raise ValueError

            if matches.group(2) == None:
                minute_begin = "00"
            elif matches.group(2) and int(matches.group(2))<60:
                minute_begin = (matches.group(2))
            else:
                raise ValueError

            if 0 < start_hour < 12 and matches.group(3) == "P":
                hour_begin = str(start_hour + 12)
            elif start_hour == 12 and matches.group(3) == "P":
                hour_begin = "12"
            elif start_hour == 12 and matches.group(3) == "A":
                hour_begin = "00"
            elif 0 < start_hour <= 9:
                hour_begin = "0" + str(start_hour)
            else:
                hour_begin = str(start_hour)

            if matches.group(5) == None:
                minute_end = "00"
            elif matches.group(5) and int(matches.group(5))<60:
                minute_end = (matches.group(5))
            else:
                raise ValueError

            if 0 < end_hour < 12 and matches.group(6) == "P":
                hour_end = str(end_hour + 12)
            elif end_hour == 12 and matches.group(6) == "P":
                hour_end = "12"
            elif end_hour == 12 and matches.group(6) == "A":
                hour_end = "00"
            elif 0 < end_hour <= 9:
                hour_end = "0" + str(end_hour)
            else:
                hour_end = str(end_hour)

            return hour_begin + ":" + minute_begin + " to " + hour_end + ":" + minute_end
        else:
            raise ValueError

    except ValueError:
        raise


if __name__ == "__main__":
    main()