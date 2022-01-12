


def Techskils (request):
    from .models import Techskils
    return {"Techskils":Techskils.objects.all()}

def FRAMEWORK (request):
    from .models import FRAMEWORK
    return {"FRAMEWORK":FRAMEWORK.objects.all()}
def TOOLS (request):
    from .models import TOOLS
    return {"TOOLS":TOOLS.objects.all()}


