from django.shortcuts import render

def slot_view(request):
    return render(request, 'slot.html')  

