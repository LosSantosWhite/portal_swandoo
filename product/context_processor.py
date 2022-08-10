from product.models import Model

def footer(request):
    return {'models_footer': Model.objects.all()}
