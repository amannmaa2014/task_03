from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
     "my_list" : [
     	{
	    "restaurant_name" :"Tacco Hot: ",
	    "food_type":"Maxican Food",
	    },
	    {
	    "restaurant_name":"Shawarmer: ",
	    "food_type":"Arabian Food",
	    },
	    {
	    "restaurant_name":"Pastalita: ",
	    "food_type":"Italian Foof",
	    }
    ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { 
    "my_object": {
    "restaurant_name":"Tacco Hot",
    "food_type":"Maxican Food",
    },

    }
    return render(request, 'detail.html', context)
