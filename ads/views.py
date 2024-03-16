from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .models import Advert
from .forms import AdvertForm

def about_view(request):
    """
    A view to render the about page
    """
    return render(request, 'ads/about.html')

class AdList(generic.ListView):
    queryset = Advert.objects.all()
    template_name = "ads/index.html"
    paginate_by = 6

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if not self.request.user.is_authenticated:
    #         return redirect('about')

    #     return context

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('about')
        return super().get(request, *args, **kwargs)


def ad_detail(request, ad_id):
    """
    Display an individual :model:`ads.Advert`.

    **Context**

    ``advert``
        An instance of :model:`ads.Advert`.

    **Template:**

    :template:`ads/ad_detail.html`
    """

    try:
        advert = Advert.objects.get(pk=ad_id)
    except Advert.DoesNotExist:
        raise Http404("Advert does not exist")
    return render(request, "ads/ad_detail.html", {
        "advert": advert,
        })

def create_ad(request):
    """
    view to create an ad
    """
    advert = Advert
    advert_form = AdvertForm()

    if request.method == "POST":
        advert_form = AdvertForm(data=request.POST)
    if advert_form.is_valid():
        ad = advert_form.save(commit=False)
        ad.user = request.user
        ad.advert = advert
        ad.save()
        messages.add_message(
        request, messages.SUCCESS,
        'Your advert is now live!'
        )
        return HttpResponseRedirect("/")

    return render(
        request,
        "ads/create_ad.html",
        {
            "advert_form": advert_form,
        },
    )


def edit_ad(request, ad_id):
    """
    View to edit an ad
    """
    context = {}
    obj = get_object_or_404(Advert, id=ad_id)
    form = AdvertForm(request.POST or None, instance = obj)

    if not obj.user == request.user:
        messages.error(
            request,
            'Error, you are unauthorized to edit this ad'
        )
        return redirect(reverse('home'))
    form =  AdvertForm(request.POST or None, instance = obj)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Advert updated')
            return HttpResponseRedirect(reverse('ad_detail', args=[ad_id]))
        else:
            messages.add_message(request, messages.ERROR, 'Error updating advert')

    context["form"] = form

    return render(request, "ads/edit_ad.html", context)

def delete_ad(request, ad_id):
    """
    View to delete and ad
    """
    context ={}
    obj = get_object_or_404(Advert, id = ad_id)
 
    if not obj.user == request.user:
        messages.error(
            request,
            'Error, you are unauthorized to delete this ad'
        )
        return redirect(reverse('home'))
 
    if request.method =="POST":
        obj.delete()
        messages.add_message(request, messages.SUCCESS, 'Advert deleted')
        return HttpResponseRedirect("/")
    else:
        messages.add_message(request, messages.ERROR, 'Error deleting advert')
 
    return render(request, "ads/delete_ad.html", context)

