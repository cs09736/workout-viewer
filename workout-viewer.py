import numpy

UPPER_LATITUDE = -37.75
LOWER_LATITUDE = -37.96
UPPER_LONGITUDE = 145.15
LOWER_LONGITUDE = 144.89
# 36 km wide
# 23 km tall
# image size = 2300x3600 px

IMG_WIDTH = 2300
IMG_HEIGHT = 3600

def coordinate_to_pixel(latitude, longitude):
	degrees_wide = UPPER_LONGITUDE - LOWER_LONGITUDE
	degrees_tall = UPPER_LATITUDE - LOWER_LATITUDE

	latitude_offset = latitude - LOWER_LATITUDE
	longitude_offset = longitude - LOWER_LONGITUDE

	x_position = longitude_offset / degrees_wide
	y_position = latitude_offset / degrees_tall
	return (x_position, y_position)

print(coordinate_to_pixel(UPPER_LATITUDE, UPPER_LONGITUDE))




print("Hello world!")
print("A second message")
