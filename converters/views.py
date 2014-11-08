from django.shortcuts import render
from django.http import HttpResponse
from  PIL import Image
from converters.forms import UploadForm

def index(request):
	form = UploadForm(request.POST, request.FILES)
	if form.is_valid():
		gray(request.FILES['image'])

	context = {"form": form}
	template = "upload.html"
	return render(request, template, context)

def gray(image):
	img = Image.open(image)
	size = img.size
	new_img = Image.new("L", size)
	for x in range(0, size[0]):
		for y in range(0, size[1]):
			loc = (x, y)
			pixel = img.getpixel(loc)
			val = (pixel[0] + pixel[1] + pixel[2]) / 3
			new_img.putpixel(loc, val)

	new_img.show()