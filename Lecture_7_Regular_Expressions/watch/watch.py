import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    html_site = s.strip()
    if re.search(r'^<iframe(?:.)*></iframe>$', html_site): # Search for desired iframe structure
        # Returns None if not in the right structure within iframe
        desired_format = re.search(r"http(?:s)?:\/\/(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9]+)", html_site) # Search specifically for url with "embed"
        # Returns None if youtube.com\embed not in url
        if desired_format:
            return "https://youtu.be/" + desired_format.group(1)
            #result = "https://youtu.be/" + desired_format.group(1)
        #return result


if __name__ == "__main__":
    main()
