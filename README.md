# workout-viewer
This is a python script that will take a direcotry of GPX files and draw a map with all the GPS traces. 

The boundaries of the map are defined by the latitude and longitude of each edge which can be adjusted within the code.
There is also the ability to supply a map to overlay the drawn traces onto. To do this you must change `USE_BACKGROUND_IMAGE` inside the code.

## Future
I plan to clean up the code and make it much easier to change between doing a map overlay and not, maybe even automatically downloading the background map in the process.
The code is quite slow but I'm figuring out the bottleneck and might speed it up a lot. Also I am thinking of writing this in C as a little priject which will obviously speed things up.
