def main():
    fruit_input = input("Item: ").lower()
    if calorie_count(fruit_input)!= None:
        print("Calories: ", calorie_count(fruit_input))

fruit_list = [
    {"fruit":"apple","Calories":130},
    {"fruit":"avocado","Calories":50},
    {"fruit":"banana","Calories":110},
    {"fruit":"cantaloupe","Calories":50},
    {"fruit":"greapfruit","Calories":60},
    {"fruit":"grapes","Calories":90},
    {"fruit":"honeydew melon","Calories":50},
    {"fruit":"kiwifruit","Calories":90},
    {"fruit":"lemon","Calories":15},
    {"fruit":"lime","Calories":20},
    {"fruit":"nectarine","Calories":60},
    {"fruit":"orange","Calories":80},
    {"fruit":"peach","Calories":60},
    {"fruit":"pear","Calories":100},
    {"fruit":"pineapple","Calories":50},
    {"fruit":"plums","Calories":70},
    {"fruit":"strawberries","Calories":50},
    {"fruit":"sweet cherries","Calories":100},
    {"fruit":"tangerine","Calories":50},
    {"fruit":"watermelon","Calories":80}
]

def calorie_count(requested):
    for item in fruit_list:
        if item["fruit"] == requested:
             return( item["Calories"])
        

if __name__=="__main__":
    main()