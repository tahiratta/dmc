from django.shortcuts import render
#from django.template.response import TemplateResponse
from dmc.models import Menu_items 

def index(request):
	
	'''
	index_data1 = get_object_or_404(Menu_items, menu_item_id = "MI1")
	index_context1 = {"index_data1" : index_data1}
	return render(request, "index.html", index_context1)
	'''	
	index_data1 = Menu_items.objects.all()
	index_context1 = {'index_data1' : index_data1}
	return render(request, 'index.html', index_context1)

	# index_data2 = Sub_items.objects.all()
	# index_context2 = {'index_data2' : index_data2}
	# return render(request, 'index.html', index_context2)

	# index_data3 = Sub_of_sub_items.objects.all()
	# index_context3 = {'index_data3' : index_data3}
	# return render(request, 'index.html', index_context3)

	# index_data4 = Slider_items.objects.all()
	# index_context4 = {'index_data4' : index_data4}
	# return render(request, 'index.html', index_context4)

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


	