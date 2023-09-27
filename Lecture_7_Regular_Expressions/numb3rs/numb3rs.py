import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",ip): # Needs to start with a number (^) and needs to end after 4 sets of number ($)
        while True:
            try:
            
                ip_list = ip.split(".")
                for num in ip_list:
                    if int(num)< 0 or int (num)>255:
                        return False
                    
                return True

            except ValueError:
                return False
        
    else:
        return False


if __name__=="__main__":
    main()