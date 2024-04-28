#****************************** Importing Required Libararies *********************************
import phonenumbers
from phonenumbers import timezone, carrier, geocoder

number = input("Enter number to track (with +91): ")

if not number.startswith('+'):
    number = '+91' + number  

#***************************** Parsing the data ***********************************************
phone = phonenumbers.parse(number, None)  
time = timezone.time_zones_for_number(phone)
carr = carrier.name_for_number(phone, 'en')
reg = geocoder.description_for_number(phone, 'en')


#**************************** Printing the all information *************************************
print("STD Code: ", phone.country_code)
print("Number: ", phone.national_number)
print("Region: ", time)
print("Carrier: ", carr)
print("Country: ", reg)
