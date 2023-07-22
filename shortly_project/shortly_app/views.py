from django.shortcuts import render, redirect
from .models import ShortURL
from .forms import ShortURLForm


def create_short_url(request):
    if request.method == 'POST':

        form = ShortURLForm(request.POST)
        urls_list = ShortURL.objects.all()

        if form.is_valid():
            short_url_obj = form.save()
            original_url = form.cleaned_data.get('original_url')
            # print(original_url)
            short_url = short_url_obj.short_url
            return render(request=request,template_name= 'shortend_url.html',context= {'urls_list':urls_list, 'short_url': short_url, "original_url":original_url})

    else:
        form = ShortURLForm()

    return render(request=request,template_name= 'create_short_url_form.html',context= {'form': form})

def redirect_to_original_url(request, short_url):
    short_url_obj = ShortURL.objects.get(short_url=short_url)

    return redirect(short_url_obj.original_url)

def get_shortened_urls_list(request):
    urls_list = ShortURL.objects.all()

    return render(request=request,template_name= 'shortend_url_list.html',context= {'urls_list':urls_list,})

