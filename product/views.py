from django.views.generic import ListView, DetailView
from product.models import Model, RewardsImage, Variety, Specification, Color, Slider


class ProductDetailView(DetailView):
    context_object_name = 'product'
    template_name = 'product/detail.html'

    def get_object(self, queryset=None):
        return Model.objects.prefetch_related('description__features', 'description__video_urls').get(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        rewards_queryset = RewardsImage.objects.select_related('model')
        context['variety_first_element_id'] = Variety.objects.first().id
        context['rewards_standard'] = rewards_queryset.filter(model=self.object, small=False)
        context['rewards_small'] = rewards_queryset.filter(model=self.object, small=True)
        context['main_photo'] = Variety.objects.filter(model=self.object).first()
        context['colored_specs'] = Specification.objects.filter(model=self.object, main=True)
        context['non_colored_specs'] = Specification.objects.filter(model=self.object, main=False)
        context['variety'] = Variety.objects.select_related('color').filter(model=self.object).select_related("model", "color")
        context['sliders'] = Slider.objects.filter(active=True)

        return context


class ProductListView(ListView):

    template_name = 'product/main.html'
    context_object_name = 'varieties'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all()
        return context

    def get_queryset(self):
        ids = [i.get('id') for i in Model.objects.all().values('id')]
        queryset = Variety.objects.all().select_related('model', 'model__description')
        result_queryset = []
        for i in queryset:
            if i.id in ids:
                ids.remove(i.id)
                result_queryset.append(i)

        return result_queryset

