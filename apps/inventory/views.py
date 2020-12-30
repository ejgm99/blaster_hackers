from django.shortcuts import render

# from django.contrib.staticfiles.templatetags.staticfiles import static #allows use of static files easily, use this to load images

from .models import Item, Type #this lets us access all our items in our databace

# Create your views here.
def index(request):
	types = Type.objects.all().order_by("title")
	context = {'types' : types}
	return render(request, 'inventory/index.html', context)

def type(request, type_id):
	items = Item.objects.filter(typeID = type_id).order_by("title")
	context = {'items' : items, 'type' : Type.objects.all().filter(pk = type_id)[0].title }
	return render(request, 'inventory/type.html', context)


def item(request, item_id):
	try:
		item = Item.objects.get(pk = item_id)
		image_url = get_image_url(item)
		print(image_url)
	except Item.DoesNotExist:
		raise Http404("Item Does Not Exist")
	return render(request, 'inventory/item.html', {'item':item, 'url':image_url})

def get_image_url(item):
	return static('images/inventory/'+str(item.title).replace(" ","")+'.jpg')
