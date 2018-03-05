from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def logo(request):
	return render(request, 'index.html')

def home(request):
	return render(request, 'index.html')			

def blog(request):
	return render(request, 'blog.html')				

def blogSingle(request):
	return render(request, 'blog-single.html')

def serviceList(request):
	return render(request, 'service-list.html')

def serviceDetail(request):
	return render(request, 'service-detail.html')

def contact(request):
	return render(request, 'contact-us.html')

def styleGuide(request):
	return render(request, 'typography.html')				