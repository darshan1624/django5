from django.shortcuts import render
from uc.models import UnderConstructModel

def myCustomMidddleware(get_reponse):
    def my_func(request):
        print('Before View')
        construct = UnderConstructModel.objects.first()
        u_key = 'a1234'
        if (request.GET.get('u') == u_key) or (not construct.is_under_construct):
            print('One')
            request.session['give_access'] = True
            return get_reponse(request)
        
        elif request.session.get('give_access'):
            print('Two')
            return get_reponse(request)
        else:
            reponse = render(request, 'uc/under_construct.html')
            return reponse
    return my_func