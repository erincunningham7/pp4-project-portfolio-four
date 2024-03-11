from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .models import Advert
from .forms import AdvertForm

class AdList(generic.ListView):
    queryset = Advert.objects.all()
    template_name = "ads/index.html"
    paginate_by = 6

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

    return render(
        request,
        "ads/create_ad.html",
        {
            "advert_form": advert_form,
        },
    )

def edit_ad(request, ad_id):
    """
    view to edit an ad
    """
    if request.method == "POST":

        queryset = Advert.objects.get(pk=ad_id)
        advert = get_object_or_404(queryset, ad_id=ad_id)
        advert_form = AdvertForm(data=request.POST, instance=advert)

        if advert_form.is_valid() and advert.user == request.user:
            ad = advert_form.save(commit=False)
            ad.advert = advert
            ad.save()
            messages.add_message(request, messages.SUCCESS, 'Advert updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating advert!')

    return HttpResponseRedirect(reverse('sd_detail', args=[ad_id]))

