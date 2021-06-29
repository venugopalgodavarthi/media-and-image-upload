from django.shortcuts import render
from user.models import imgupld 
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

# Create your views here.
def Imgupld(request):
    if request.method == "POST":
        print("haii")
        upload_img = request.FILES.get("img")
        fs= FileSystemStorage()
        file=fs.save(upload_img.name,upload_img)
        print(file)
        var=imgupld.objects.create(img=file)
        var.save()
        img_url=fs.url(file)
        return HttpResponseRedirect(img_url)
    return render(request,"imgupload.html")