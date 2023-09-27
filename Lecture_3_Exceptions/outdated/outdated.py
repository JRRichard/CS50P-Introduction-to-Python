def main():
    outdated()

# List of acceptable input for months of the year
months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}


def outdated():
    while True:
        try:
            date = input("Date: ")
            if ("/") in date:
                date_list = date.strip().split("/")
                if int(date_list[0])<=12 and int(date_list[1])<=31 and int(date_list[2]) and len(date_list[2])==4:
                    mm = int(date_list[0])
                    dd = int(date_list[1])
                    yyyy = date_list[2]
                    print(f"{yyyy}-{mm:02}-{dd:02}")
                    break
                else:
                    pass
            elif (",") in date:
                date = date.strip().replace(" ", "/").replace(",","")
                date_list = date.split("/")
                if date_list[0] in months and int(date_list[1])<=31 and int(date_list[2]) and len(date_list[2])==4:
                    mm = months[date_list[0]]
                    dd = int(date_list[1])
                    yyyy = date_list[2]
                    print(f"{yyyy}-{mm}-{dd:02}")
                    break

            else:
                pass
        except:
            pass
        else:
            pass
    return None


if __name__ =="__main__":
    main()
