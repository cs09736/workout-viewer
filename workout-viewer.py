from bs4 import BeautifulSoup as bs
from PIL import Image, ImageDraw

UPPER_LATITUDE = -37.75
LOWER_LATITUDE = -37.96
UPPER_LONGITUDE = 145.15
LOWER_LONGITUDE = 144.89
# 36 km wide
# 23 km tall
# image size = 2300x3600 px

IMG_WIDTH = 2300
IMG_HEIGHT = 3600

img_points = []

def coordinate_to_pixel(latitude, longitude):
	degrees_wide = UPPER_LONGITUDE - LOWER_LONGITUDE
	degrees_tall = UPPER_LATITUDE - LOWER_LATITUDE

	latitude_offset = latitude - LOWER_LATITUDE
	longitude_offset = longitude - LOWER_LONGITUDE

	x_offset = IMG_WIDTH * longitude_offset / degrees_wide
	y_offset = IMG_HEIGHT * latitude_offset / degrees_tall

	x_position = x_offset
	y_position = IMG_HEIGHT - y_offset
	return (x_position, y_position)

with open('example_data.gpx', 'r') as f:
	data = f.read()

bs_data = bs(data, "xml")
bs_trkpts = bs_data.find_all('trkpt')

for trkpt in bs_trkpts:
	latitude = float(trkpt.get('lat'))
	longitude = float(trkpt.get('lon'))
	points = coordinate_to_pixel(latitude, longitude)
	img_points.append(points)

image = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), color=0)
draw = ImageDraw.Draw(image)

draw.line(img_points, fill=(255,255,255), width=2)



image.save("test.png", "PNG")




print(coordinate_to_pixel(UPPER_LATITUDE, UPPER_LONGITUDE))




print("Hello world!")
print("A second message")
