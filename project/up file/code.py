import cv2
import json
import requests
# Create an object to read
# from camera
def push():
	headers = {"Authorization": "Bearer ya29.a0AfH6SMAZVBVNz5Tp4OHWXj8uqKzk3DXOv5xFS8cX5ibHiD7hV5vHD9gDqUaZAMFuDm3_FJSRE_sdaiUysuAAk8dFNNWeqQUvJZ4WiF47FgDsP2d21GtfztvUla-TBna-iMWz4meR8dWtmaR7kxm9Ev2nmU-ulJoi0GU"}
	para = {
    	"name": "ssss.mp4",
	"parents": ["1DG-9IvyTtrlvB36JsQqNK-PryZv8jkoD"]
	}
	files = {
    	'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    	'file': open("./filename.mp4", "rb")
	}
	r = requests.post(
    	"https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    	headers=headers,
   	files=files
	)
	print(r.text)

def gstreamer_pipeline (capture_width=1280, capture_height=720	, display_width=1280, display_height=720, framerate=30, flip_method=0) :   
    return ('nvarguscamerasrc ! ' 
    'video/x-raw(memory:NVMM), '
    'width=(int)%d, height=(int)%d, '
    'format=(string)NV12, framerate=(fraction)%d/1 ! '
    'nvvidconv flip-method=%d ! '
    'video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! '
    'videoconvert ! '
    'video/x-raw, format=(string)BGR ! appsink'  % (capture_width,capture_height,framerate,flip_method,display_width,display_height))

def Save():

	video = cv2.VideoCapture(1)
	cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
	# We need to check if camera
	# is opened previously or not
	if (video.isOpened() == False):
	    print("Error reading video file")
	# We need to set resolutions.
	# so, convert them from float to integer.
	frame_width = int(video.get(3))
	frame_height = int(video.get(4))
	size = (frame_width, frame_height)
	# Below VideoWriter object will create
	# a frame of above defined The output
	# is stored in 'filename.avi' file.
	result = cv2.VideoWriter('filename.mp4',cv2.VideoWriter_fourcc(*'XVID'),15, size)
    result1 = cv2.VideoWriter('filename1.mp4',cv2.VideoWriter_fourcc(*'XVID'),15,size)
	while (True):
	    ret, frame = video.read()
	    ret_val, frame1 = cap.read()

	    if ret == True:
	       cv2.imshow('CSI Camera',frame1)
	       cv2.imshow('usb camera',frame)
           out.write(frame)
           out.write(frame1)
	       if cv2.waitKey(1) & 0xFF == ord('s'):
	          break
	    # Break the loop
	    else:
	        break
	# When everything done, release
	# the video capture and video
	# write objects
	video.release()
	cap.release()
	result.release()
    result1.release()
	# Closes all the frames
	cv2.destroyAllWindows()
	print("The video was successfully saved")

if _name_ == "_main_":
	Save()
	push()