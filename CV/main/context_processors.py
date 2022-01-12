def Techskils (request):
    from .models import Techskils
    return {"Techskils":Techskils.objects.all()}