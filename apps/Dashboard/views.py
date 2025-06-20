from django.shortcuts import render

def main(request):
    return render(request, 'modules/dashboard/index.html')
