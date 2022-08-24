from django.views.generic import ListView, DetailView
from product.models import Model, RewardsImage, Variety, Specification, Color, Slider


class ProductDetailView(DetailView):
    context_object_name = 'product'
    template_name = 'product/detail.html'

    def get_object(self, queryset=None):
        return Model.objects.get(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['rewards_standard'] = RewardsImage.objects.filter(model=self.object, small=False)
        context['rewards_small'] = RewardsImage.objects.filter(model=self.object, small=True)
        context['main_photo'] = Variety.objects.filter(model=self.object).first()
        context['colored_specs'] = Specification.objects.filter(model=self.object, main=True)
        context['non_colored_specs'] = Specification.objects.filter(model=self.object, main=False)
        context['variety'] = Variety.objects.select_related("model", "color")
        return context


class ProductListView(ListView):

    template_name = 'product/main.html'
    context_object_name = 'varieties'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all()
        return context

    def get_queryset(self):
        # TODO додумать queryset

        models = Model.objects.distinct()

