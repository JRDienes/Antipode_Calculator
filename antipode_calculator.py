# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 00:52:48 2020

@author: jackson

written in python
"""

#------Dependencies

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim


"""---------this is the imput so you can search adresses--------------------------"""

geolocator = Nominatim(user_agent="JacksonDienes")
ladd1 = input("Address, State, or Country: ")
ladd1 = str(ladd1)
ladd1 = ladd1.capitalize()
exact_location = geolocator.geocode(ladd1)
print(round(exact_location.latitude, 2), round(exact_location.longitude, 2))


"""--------------This is to input coords manually--------------------------------"""

# lat = input("Input Latitude: ")
# lat = float(lat)
# lat_direction = input("N - S: ")
# lat_direction = str(lat_direction)
# long = input("Input Longitute: ")
# long = float(long)
# long_direction = input("E - W: ")
# long_direction = str(long_direction)
# location = input("What is the name of your city? ")
# location = str(location)

"""--------------------FUNCTIONS-------------------------------------------------"""

def anti_lat(lat):
    antiLat = (lat * -1)   
    return antiLat
    
def anti_long(long):
    if long > 0:
        antiLong = ((180 - (abs(long))) * -1)
    elif long < 0:
        antiLong = (180 - (abs(long)))
    return antiLong




# these were to convert the directions from the manual coords
# this is definately not here just to make me feel better... pointless


# def direction_reverse_lat(lat_direction):
#     if lat_direction == "N":
#         anti_lat_direction = lat_direction.replace("N","S")
#     elif lat_direction == "S":
#         anti_lat_direction = lat_direction.replace("S","N")
#     elif lat_direction == "n":
#         anti_lat_direction = lat_direction.replace("n","S")
#     elif lat_direction == "s":
#         anti_lat_direction = lat_direction.replace("s","N")
#     return anti_lat_direction
    
# def direction_reverse_long(long_direction):
#     if long_direction == "E":
#         anti_long_direction = long_direction.replace("E","W")
#     elif long_direction == "W":
#         anti_long_direction = long_direction.replace("W","E")
#     elif long_direction == "e":
#         anti_long_direction = long_direction.replace("e","W")
#     elif long_direction == "w":
#         anti_long_direction = long_direction.replace("w","E")
#     return anti_long_direction

#------this is so it rounds the displayed coords to 2 decimals
# I didnt know where else to put it

new_lat = round(anti_lat(exact_location.latitude), 2)
new_long = round(anti_long(exact_location.longitude), 2)


"""------------------PLOTTING---------------------------------------- """

# ax = plt.axes(projection=ccrs.EqualEarth())
# ax.coastlines()
# ax.stock_img()


# plt.plot([long, anti_long(long)], [lat, anti_lat(lat)],
#          color='blue', linewidth=0, marker='o',
#          transform=ccrs.Geodetic(),
#          )

# plt.plot([long, anti_long(long)], [lat, anti_lat(lat)],
#           color='red', linestyle='--',
#           transform=ccrs.PlateCarree(),
#           )

# plt.text(long - 3, lat - 12, location,
#           horizontalalignment='right',
#           transform=ccrs.Geodetic())

# plt.text(anti_long(long) + 3, anti_lat(lat) - 12, 'Antipode location',
#           horizontalalignment='left',
#           transform=ccrs.Geodetic())

# plt.show() 



ax = plt.axes(projection=ccrs.EqualEarth())
#ax.coastlines()
ax.stock_img()


plt.plot([exact_location.longitude, anti_long(exact_location.longitude)], [exact_location.latitude, anti_lat(exact_location.latitude)],
         color='blue', linewidth=0, marker='o',
         transform=ccrs.Geodetic(),
         )

plt.plot([exact_location.longitude, anti_long(exact_location.longitude)], [exact_location.latitude, anti_lat(exact_location.latitude)],
          color='red', linestyle='--',
          transform=ccrs.PlateCarree(),
          )

plt.text((exact_location.longitude) - 3, (exact_location.latitude) - 12, ladd1,
          horizontalalignment='right',
          transform=ccrs.Geodetic())

plt.text(anti_long(exact_location.longitude) + 3, anti_lat(exact_location.latitude) - 15, str(new_long) + " " + str(new_lat),
          horizontalalignment='left',
          transform=ccrs.Geodetic())

plt.show() 


"""-----------This was the origanal output, still set for outputting manual coords"""

# print("-------------------------------------")
# print("Original Coordinates (Decimal format)")
# print("Latitude is " + str(lat) + " " + (lat_direction))
# print("Longitude is " + str(long) + " " + (long_direction))
# print("-------------------------------------")
# print("Antipodal Coordinates (Decimal format)")
# print("Anti Latitude is: " + str(anti_lat(lat)) + " " + str(direction_reverse_lat(lat_direction)))
# print("Anti Longitude is: " + str(anti_long(long)) + " " + str(direction_reverse_long(long_direction)))



"""

This is the end of this code
if you got this far in the page to read this
congradulations...


love
Jackson <3

12/22/2020

_____________¶____¶ 
_________¶_¶¶¶¶¶¶¶¶¶¶ 
_____¶¶¶¶¶¶¶_________¶ 
___¶¶¶¶¶_____________¶ 
___¶_________________¶ 
____¶________________¶¶ 
____¶¶________________¶ 
_____¶________________¶¶ 
_____¶¶_______¶¶¶____¶¶¶ 
______¶_____¶¶___¶¶_¶___¶ 
______¶_____¶¶_____¶____¶ 
______¶¶____¶______¶¶¶¶¶¶¶ 
_______¶____¶¶__¶¶¶_____¶¶ 
______¶¶¶¶____¶¶¶¶_____¶¶ 
______¶¶¶_______________¶¶ 
_______¶¶¶______________¶¶ 
________¶_____¶¶¶¶¶¶¶¶¶¶¶ 
_______¶¶_______¶¶¶¶¶ 
______¶¶¶¶¶_____¶ 
___¶¶¶¶__¶¶¶¶¶¶¶¶ 
__¶¶____¶¶_____¶¶ 
_¶¶_____¶¶______¶¶ 
¶¶______¶¶_______¶¶ 
_¶¶¶¶¶___¶¶______¶¶ 
_¶__¶¶¶¶¶¶_______¶¶ 
¶¶____¶___________¶¶ 
¶____¶¶__________¶¶¶ 
¶____¶¶____________¶ 
¶_____¶___________¶¶¶ 
¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶_¶ 
¶______¶_________¶___¶ 
¶¶¶¶__¶__________¶_¶¶¶ 
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
___¶¶¶¶¶¶¶¶¶____¶ 
___¶¶___¶__¶____¶ 
___¶____¶__¶____¶ 
___¶¶___¶__¶____¶¶ 
__¶_______¶¶¶¶¶¶¶¶¶¶ 
_¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶ 
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶

"""