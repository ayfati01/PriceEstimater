# this app should be able to set a reasonable price
# for a photography session.
# Factors that alter the price:
# - Base price: price set by photographer before
#               anything is added
# - Occasion: type of photography session
#   Ex:
#    - Wedding
#    - Birthday
# - Age: come on, do I need to explain this?
# - Weather: How is the weather going to be during
#            the day and time of the session?

import os
from colorama import Fore
import requests
import datetime
import getpass
import sys
import hashlib
from terminaltables import SingleTable


def report():
    OccasionFactor = float(os.environ.get('Occasion'))
    BasePay        = float(os.getenv('BasePay'))
    AgeLowFactor   = float(os.getenv('AgeLow'))
    AgeMedFactor   = float(os.getenv('AgeMed'))
    AgeHighFactor  = float(os.getenv('AgeHigh'))
    WeatherBad     = float(os.getenv('WeatherBad'))
    WeatherNormal  = float(os.getenv('WeatherNormal'))
    WeatherGood    = float(os.getenv('WeatherNormal'))
    HourFactor     = float(os.getenv('Hour'))
    EditFactor     = float(os.getenv('Edit'))
    LowRate        = float(os.getenv('LowRate'))
    RecommendedRate= float(os.getenv('RecommendedRate'))
    HighRate       = float(os.getenv('HighRate'))

    template = [['Factor', 'Value'],
                ["OccasionFactor", cyan(str(f"{int(round(OccasionFactor*100, 1))}%"))],
                ["BasePay", green("$"+str(int(BasePay)))],
                ["AgeLowFactor", cyan(str(f"{int(round(AgeLowFactor*100, 1))}%"))],
                ["AgeMedFactor", cyan(str(f"{int(round(AgeMedFactor*100, 1))}%"))],
                ["AgeHighFactor", cyan(str(f"{int(round(AgeHighFactor*100, 1))}%"))],
                ["WeatherBad", cyan(str(f"{int(round(WeatherBad*100, 1))}%"))],
                ["WeatherNormal", cyan(str(f"{int(round(WeatherNormal*100, 1))}%"))],
                ["WeatherGood", cyan(str(f"{int(round(WeatherGood*100, 1))}%"))],
                ["HourFactor", cyan(str(f"{int(round(HourFactor*100, 1))}%"))],
                ["EditFactor", cyan(str(f"{int(round(EditFactor*100, 1))}%"))],
                ["LowRate", cyan(str(f"{int(round(LowRate*100, 1))}%"))],
                ["RecommendedRate", cyan(str(f"{int(round(RecommendedRate*100, 1))}%"))],
                ["HighRate", cyan(str(f"{int(round(HighRate*100, 1))}%"))],]

    table = SingleTable(template)
    print(table.table)


def makeEstimate():
    occasion = getOccasion()
    age = getAge()
    weather = getWeather()
    edit = getEdit()
    hours = getHours()
    basePay = getBasePay()

    analyze(
        occasion,
        age,
        weather,
        edit,
        hours,
        basePay)


# Take command

def command():
    print()
    cycle = True
    while cycle:
        print("\nTo start estimate ==> type \'estimate\' \n"
              "To quit             ==> type \'quit\' \n")
        c = input(">>>    ")
        if c == 'report':
            clearScreen()
            report()
        elif c == 'estimate':
            clearScreen()
            makeEstimate()
        elif c == 'quit':
            sys.exit()
        else:
            print("not a valid command")


# Generate a hash key


def generatehashkey(raw_text):
    app_name = "price app"
    text = raw_text + app_name
    text = text[4:-1:len(text) - 6] + text[3:7] + text[0:6:2]
    return hashlib.md5(text.encode()).hexdigest()

# To clear the screen


def clearScreen():
    if sys.platform == 'darwin':
        os.system('clear')
        # To clear a terminal bug
        os.system("export TERM=xterm")
    else:
        os.system('cls')


# Verify key
def verify():
    #   key = "386ab0331bfbbb0de293a9f319144f46"
  #  if key != generatehashkey(raw_text=os.environ['LOGNAME']):
   #     print('''You do not have a valid license to run this program.
    #    Contact ammar at fatihallah.ammar@gmail.com''')
    #    sys.exit()
   # else:
   #     pass
   pass

# Get base pay


def getBasePay():
    return float(os.getenv('BasePay'))


# Get value for occasion


def getOccasion():
    print('''on a scale from 1 to 5 \nhow special is the session for the client?\n''')
    cycle = True
    while cycle:
        try:
            number = int(input(">>>    "))
            while number < 1 or number > 5:
                if number < 1:
                    print("the number you set is too low, set a higher number!\n")
                elif number > 5:
                    print("the number you set is too high, set a smaller number!\n")
                print('''on a scale from 1 to 5 \nhow special is the session for the client?\n''')
                number = int(input(">>>    "))
            print("\nOccasion mark set to {}\n".format(number))
            cycle = False
            return number
        except ValueError:
            print("Sorry, the value you entered is not a number. please try again")


# Get age of client


def getAge():
    print('''What\'s the age of your client?\n''')
    cycle = True
    while cycle:
        try:
            age = int(input(">>>    "))
            print("\nAge set to {}\n".format(age))
            cycle = False
            return age
        except ValueError:
            print("Sorry, the value you entered is not a number. please try again")


# Get weather


def getWeather():
    print("on a scale from 1 to 3, from WORST to BEST.\n"
          "How is the weather looking on the day of the photoshoot?\n")
    cycle = True
    while cycle:
        try:
            weather = int(input(">>>    "))
            if weather <= 9:
                while weather > 3:
                    print("Choose a number from 1 to 3, from WORST to BEST.")
                    print('''\nHow is the weather looking on the day of the photoshoot?\n''')
                    weather = int(input(">>>    "))
                else:
                    pass

            print("\nweather set to {}\n".format(weather))
            cycle = False
            return weather
        except ValueError:
            print("Sorry, the value you entered is not a number. please try again")


# Get 'edit or not'


def getEdit():
    print("Will you be editing the photos?\n Yes => 1, No => ENTER\n")
    cycle = True
    while cycle:
        try:
            edit = input(">>>   ")
            print("Edit is set to {}\n".format(edit if edit else "no edit"))
            cycle = False
            return edit
        except ValueError:
            print("Sorry, the value you entered is not a number. please try again")


# Get hours


def getHours():
    print("How many hours will the session last?\n")
    cycle = True
    while cycle:
        try:
            hours = int(input(">>>  "))
            cycle = False
            return hours
        except ValueError:
            print("Sorry, the value you entered is not a number. please try again")


# Email related

def send_email(info):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox0e48ae61dd724db49fd04a9f7c7644ab.mailgun.org/messages",
        auth=("api", "key-6a5a0ba282ac7d5e464724491f160e23"),
        data={"from": "priceapp@sandbox0e48ae61dd724db49fd04a9f7c7644ab.mailgun.org",
              "to": ["fatihallah.ammar@gmail.com"],
              "subject": "Price lookup detected",
              "text": "{}".format(info)})


# ascii animal


def ascii_animal(lowest, recommended, highest, cancellation):
    return f"< Price: Lowest => ${red(str(round(lowest)))} >\n" \
           f"< Price: Recommended => ${green(str(round(recommended)))} >\n" \
           f"< Price: Highest => ${blue(str(round(highest)))} >\n" \
           f"< Cancellation fee => ${cyan(str(round(cancellation)))} >\n" \
           "                 \\\n" \
           "                  \\\n" \
           "                   \\\n" \
           "                    \\\n" \
           "               ___,A.A_  __\n" \
           "               \\   ,   7\"_/\n" \
           "                ~\"T(  r r)\n" \
           "                  | \\    Y\n" \
           "                  |  ~\\ .|\n" \
           "                  |   |`-'\n" \
           "                  |   |\n" \
           "                  |   |\n" \
           "                  |   |\n" \
           "                  |   |\n" \
           "                  j   l\n" \
           "                 /     \\\n" \
           "                Y       Y\n" \
           "                l   \\ : |\n" \
           "                /\\   )( (\n" \
           "               /  \\  I| |\\\n" \
           "              Y    I l| | Y\n" \
           "              j    ( )( ) l\n" \
           "             / .    \\ ` | |\\\n" \
           "            Y   \\    i  | ! Y\n" \
           "            l   .\\_  I  |/  |\n" \
           "             \\ /   [\\[][]/] j\n" \
           "          ~~~~~~~~~~~~~~~~~~~~~~~\n"


# Get username


def getUsername():
    return getpass.getuser()


# Get date and time


def getDatetime():
    return datetime.datetime.now().strftime("On %A at %I:%M:%S %p")


def analyze(occasion, age, weather, edit, hours, BP):

    OccasionFactor = float(os.getenv('Occasion'))
    BasePay         = BP
    AgeLowFactor    = float(os.getenv('AgeLow'))
    AgeMedFactor    = float(os.getenv('AgeMed'))
    AgeHighFactor   = float(os.getenv('AgeHigh'))
    WeatherBad      = float(os.getenv('WeatherBad'))
    WeatherNormal   = float(os.getenv('WeatherNormal'))
    WeatherGood     = float(os.getenv('WeatherNormal'))
    HourFactor      = float(os.getenv('Hour'))
    EditFactor      = float(os.getenv('Edit'))
    LowRate         = float(os.getenv('LowRate'))
    RecommendedRate = float(os.getenv('RecommendedRate'))
    HighRate        = float(os.getenv('HighRate'))

    # For the hidden gem

    if weather > 3:
        weather = list(map(int, str(weather)))[0]
        egg = True
    else:
        egg = False
    # For template at the end of procedure

    baseHours = hours
    baseWeather = weather
    baseEdit = edit
    baseOccasion = occasion
    baseAge = age

    # Figure out what kind of weather

    if weather == 1:
        baseWeather = "Good"
    elif weather == 2:
        baseWeather = "Mediocre"
    elif weather == 3:
        baseWeather = "Bad"

    # Figure out edit

    if edit:
        baseEdit = "YES"
    else:
        baseEdit = "NO"

    # Figure out the occasion

    if baseOccasion == 1:
        baseOccasion = "NOT FORMAL"
    elif baseOccasion == 2:
        baseOccasion = "FORMAL"
    elif baseOccasion == 3:
        baseOccasion = "KINDA SPECIAL"
    elif baseOccasion == 4:
        baseOccasion = "SPECIAL"
    elif baseOccasion == 5:
        baseOccasion = "VERY SPECIAL"

    # Occasion factor
    occasion *= OccasionFactor


    # Age factor
    if age <= 16:
        age = AgeLowFactor
    elif 18 <= age <= 37:
        age = AgeMedFactor
    else:
        age = AgeHighFactor

    # Weather factor
    if weather == 1:
        weather = WeatherBad
    elif weather == 2:
        weather = WeatherNormal
    else:
        weather = WeatherGood

    # Edit factor
    if edit:
        edit = EditFactor

    else:
        pass

    percentage = float(occasion) + float(age) + float(weather) + float(edit)

    # Hour factor
    hours *= HourFactor

    price = round(percentage * BP * hours, 1)

    lowest = price * LowRate
    recommended = price * RecommendedRate
    highest = price * HighRate
    cancellation = recommended * 0.13

    # Email template
    email_data = f'''Occasion: {baseOccasion}
Hours: {baseHours}
Edit: {baseEdit}
Age: {baseAge}
Weather: {baseWeather}
Multiplier: {str(round(percentage))}
Lowest price: ${str(round(lowest))}
Recommended price: ${str(round(recommended))}
Highest price: ${str(round(highest))}
Cancellation: ${str(round(cancellation))}
                 '''

    table_data = [["Factor", "value"],
                  ["Occasion", baseOccasion],
                  ["Hours", baseHours],
                  ["Edit", baseEdit],
                  ["Age", baseAge],
                  ["Weather", baseWeather],
                  ["Multiplier", yellow(str(round(percentage)))],
                  ["LowRate", cyan(str(LowRate))],
                  ["RecommendedRate", cyan(str(RecommendedRate))],
                  ["HighRate", cyan(str(HighRate))],
                  ["Price: Lowest", red("$" + str(round(lowest)))],
                  ["Price: Recommended", green("$" + str(round(recommended)))],
                  ["Price: Highest", blue("$" + str(round(highest)))],
                  ["Cancellation fee", cyan("$" + str(round(cancellation)))],
                  ]
    table = SingleTable(table_data)
    clearScreen()

    if egg:
        template = ascii_animal(lowest=lowest,
                                recommended=recommended,
                                highest=highest,
                                cancellation=cancellation)

        print(template)
    else:
        print(table.table)

    # Send email, include date and time, and username.

    send_email("{}\nUser: {}\n----------------\n{}".format(getDatetime(),
                                                           getUsername(),
                                                           email_data))


# Text colors


def red(text):
    return Fore.RED + str(text) + Fore.RESET


def green(text):
    return Fore.GREEN + str(text) + Fore.RESET


def blue(text):
    return Fore.BLUE + str(text) + Fore.RESET


def yellow(text):
    return Fore.YELLOW + str(text) + Fore.RESET


def cyan(text):
    return Fore.CYAN + str(text) + Fore.RESET
