import os
import numpy as np
from bs4 import BeautifulSoup
import cv2
import progressbar

UPPER_LATITUDE = -37.7745
LOWER_LATITUDE = -38.0035
UPPER_LONGITUDE = 145.1716
LOWER_LONGITUDE = 144.8863
USE_BACKGROUND_IMAGE = False
RED = (0,0,255)
WHITE = (255,255,255)
LINE_THICKNESS = 2
IMAGE_WIDTH = 4096
IMAGE_HEIGHT = 4096
MAP_FILE = '/Users/samcantwell/Nextcloud/map.png'
ROUTE_DIRECTORY = "/Users/samcantwell/Nextcloud/workout-routes"
WRITE_VIDEO = False
FPS = 24.0
VIDEO_WRITE_FREQUENCY = 1000

write_video = WRITE_VIDEO
route_directory  = ROUTE_DIRECTORY


def sort_function(filename):
	return filename.split("_")[1]


def coordinate_to_pixel(latitude, longitude):
	degrees_wide = UPPER_LONGITUDE - LOWER_LONGITUDE
	degrees_tall = UPPER_LATITUDE - LOWER_LATITUDE

	latitude_offset = latitude - LOWER_LATITUDE
	longitude_offset = longitude - LOWER_LONGITUDE

	x_offset = img_width * longitude_offset / degrees_wide
	y_offset = img_height * latitude_offset / degrees_tall

	x_position = x_offset
	y_position = img_height - y_offset
	return (int(x_position), int(y_position))


if USE_BACKGROUND_IMAGE:
	image = cv2.imread(MAP_FILE)
	img_width = image.shape[1]
	img_height = image.shape[0]
	colour = RED
	downsize = False
else:
	image = np.zeros((IMAGE_WIDTH, IMAGE_HEIGHT, 3), dtype=np.uint8)
	img_width = IMAGE_WIDTH
	img_height = IMAGE_HEIGHT
	colour = WHITE
	downsize = True


if write_video:
	print("Generating video writer")
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	video_writer = cv2.VideoWriter("output.avi", fourcc, FPS, (img_width, img_height))


print("Reading files")
file_counter = 0
counter = 0
file_list = sorted(list(os.listdir(route_directory)), key=sort_function)
widgets = [' [',progressbar.Timer(format= 'elapsed time: %(elapsed)s'),'] ',progressbar.Bar('*'),' (',progressbar.ETA(), ') ',]
bar = progressbar.ProgressBar(max_value=len(file_list), widgets=widgets).start()
for filename in file_list:
	file_counter += 1
	bar.update(file_counter)
#	counter = 0
	img_points = []
	f = '/'.join([route_directory,filename])

	with open(f, 'r') as f:
		data = f.read()
		BeautifulSoup_data = BeautifulSoup(data, "xml",)
		BeautifulSoup_trkpts = BeautifulSoup_data.find_all('trkpt')
	
	for trkpt in BeautifulSoup_trkpts:
		latitude = float(trkpt.get('lat'))
		longitude = float(trkpt.get('lon'))
		points = coordinate_to_pixel(latitude, longitude)
		img_points.append(points)
	
	length = len(img_points)
	for index in range(length-1):
		cv2.line(image, img_points[index], img_points[index+1], colour, LINE_THICKNESS)
		if write_video:
			counter += 1
			if counter%VIDEO_WRITE_FREQUENCY == 0:
				video_writer.write(image)

#	if write_video:
#		video_writer.write(image)
if write_video:
	video_writer.write(image)
##

print("\nWriting final image")
if downsize:
	image = cv2.resize(image, (img_width//2, img_height//2), interpolation=cv2.INTER_LINEAR)

cv2.imwrite("resultMap.png", image)

if write_video:
	print("Releasing video file")
	video_writer.release()

print("All done")
