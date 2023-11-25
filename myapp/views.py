from django.shortcuts import render
from .forms import ImageForm
from .models import Images

# Create your views here.

def home(req):
    if req.method == 'POST':
        form=ImageForm(req.POST,req.FILES)
        if form.is_valid():               # means form me sare input box fill hai 
           form.save()

    form=ImageForm()
    # image fetch krege database me se 

    img=Images.objects.all()
    return render(req,"home.html",{'img':img,'form':form})