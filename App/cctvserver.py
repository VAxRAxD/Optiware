from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from .camera import VideoCamera, IPWebCam

def index(request):
	return render(request, 'App/footage.html')

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def warehouse_feed(request):
    url="http://192.168.29.177:8080/shot.jpg"
    return StreamingHttpResponse(gen(IPWebCam(url)),
					content_type='multipart/x-mixed-replace; boundary=frame')
 
def machinery_feed(request):
    url="http://192.168.29.232:8080/shot.jpg"
    return StreamingHttpResponse(gen(IPWebCam(url)),
					content_type='multipart/x-mixed-replace; boundary=frame')