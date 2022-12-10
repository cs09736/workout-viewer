import os
from bs4 import BeautifulSoup as bs
from PIL import Image, ImageDraw

UPPER_LATITUDE = -37.7745
LOWER_LATITUDE = -38.0035
UPPER_LONGITUDE = 145.1716
LOWER_LONGITUDE = 144.8863
# 36 km wide
# 23 km tall
# image size = 2300x3600 px



#image = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), color=0)
image = Image.open('/home/sam/Nextcloud/map.png', 'r')
draw = ImageDraw.Draw(image)
IMG_WIDTH = image.size[0]
IMG_HEIGHT = image.size[1]


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


# Test code to print each file name in directory
directory  = "/home/sam/Nextcloud/workout-routes"
for filename in os.listdir(directory):
	img_points = []
	f = '/'.join([directory,filename])

	with open(f, 'r') as f:
		data = f.read()
		bs_data = bs(data, "xml")
		bs_trkpts = bs_data.find_all('trkpt')
	
	for trkpt in bs_trkpts:
		latitude = float(trkpt.get('lat'))
		longitude = float(trkpt.get('lon'))
		points = coordinate_to_pixel(latitude, longitude)
		img_points.append(points)
	

	
	draw.line(img_points, fill=(255,0,0), width=2)



image.save("resultMap.png", "PNG")




print(coordinate_to_pixel(UPPER_LATITUDE, UPPER_LONGITUDE))




print("Hello world!")
print("A second message")
