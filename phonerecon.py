import os
import phonenumbers
from phonenumbers import carrier,timezone,geocoder


banner = '''
______ _                     ______                     
| ___ \ |                    | ___ \                    
| |_/ / |__   ___  _ __   ___| |_/ /___  ___ ___  _ __  
|  __/| '_ \ / _ \| '_ \ / _ \    // _ \/ __/ _ \| '_ \ 
| |   | | | | (_) | | | |  __/ |\ \  __/ (_| (_) | | | |
\_|   |_| |_|\___/|_| |_|\___\_| \_\___|\___\___/|_| |_|

'''

clearConsole = lambda: print('\n' * 150)

clearConsole()
print(banner)
data = str(input(">Enter phone number(with Country code(Ex. +91)):"))
phone_number = phonenumbers.parse(data)

print("\n##################################")
print("|      Phone Number Details      |")
print("##################################\n")
print("Valid Number:", str(phonenumbers.is_valid_number(phone_number)))
print("Carrier Name:", str(carrier.name_for_number(phone_number, "en")))
print("Timezone:", str(timezone.time_zones_for_number(phone_number)))
print("Geolocation:", str(geocoder.description_for_number(phone_number, "en")))
