from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Advert

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

    # queryset = Advert.objects.all()
    # advert = get_object_or_404(queryset, ad_id)

    # return render(
    #     request,
    #     "ads/ad_detail.html",
    #     {"advert": advert},
    # )

    try:
        advert = Advert.objects.get(pk=ad_id)
    except Advert.DoesNotExist:
        raise Http404("Advert does not exist")
    return render(request, "ads/ad_detail.html", {"advert": advert})

