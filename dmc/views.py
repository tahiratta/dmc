from django.shortcuts import render
#from django.db.models import Count
#from django.template.response import TemplateResponse
from dmc.models import Menu_items

from dmc.models import Sub_items

def index(request):

	index_data1 = Menu_items.objects.all()

	index_context1 = {'index_data1' : index_data1}
	return render(request, 'index.html', index_context1)

	'''
	index_data1 = get_object_or_404(Menu_items, menu_item_id = "MI1")
	index_context1 = {"index_data1" : index_data1}
	return render(request, "index.html", index_context1)
	'''
	#index_data1 = Menu_items.objects.all().prefetch_related('menus').annotate(sub_items = Count('menus'))
	#index_data1 = Menu_items.objects.select_related('sub_items').all()

 # all_models_dict = {
 #        "template_name": "index.html",
 #        "queryset": Menu_items.objects.all(),
 #        "extra_context" : {"sub_items_list" : Sub_items.objects.all(),
 #                           #and so on for all the desired models...
 #                           }
 #    }	

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
	index_data1 = Menu_items.objects.all()
	index_context1 = {'index_data1' : index_data1}
	return render(request, 'index.html', index_context1)

def home(request):
	index_data1 = Menu_items.objects.all()
	index_context1 = {'index_data1' : index_data1}
	return render(request, 'index.html', index_context1)			

def blog(request):
	index_data1 = Menu_items.objects.all()
	index_context1 = {'index_data1' : index_data1}
	return render(request, 'blog.html', index_context1)				

def blogSingle(request):
	index_data1 = Menu_items.objects.all()
	index_context1 = {'index_data1' : index_data1}
	return render(request, 'blog-single.html', index_context1)

def serviceList(request):
	index_data1 = Menu_items.objects.all()
	index_context1 = {'index_data1' : index_data1}
	return render(request, 'service-list.html', index_context1)

def serviceDetail(request):
	index_data1 = Menu_items.objects.all()
	index_context1 = {'index_data1' : index_data1}
	return render(request, 'service-detail.html', index_context1)

def contact(request):
	index_data1 = Menu_items.objects.all()
	index_context1 = {'index_data1' : index_data1}
	return render(request, 'contact-us.html', index_context1)

def styleGuide(request):
	index_data1 = Menu_items.objects.all()
	index_context1 = {'index_data1' : index_data1}
	return render(request, 'typography.html', index_context1)				
def pmexform(request):
	index_data1 = Menu_items.objects.all()
	index_context1 = {'index_data1' : index_data1}
	return render(request, 'pmexform.html', index_context1)				
def certificate(request):
	index_data1 = Menu_items.objects.all()
	index_context1 = {'index_data1' : index_data1}
	return render(request, 'certificate.html', index_context1)	
def prod(request):
	index_data1 = Menu_items.objects.all()
	index_context1 = {'index_data1' : index_data1}
	return render(request, 'product.html', index_context1)	
	