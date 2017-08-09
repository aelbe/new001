from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'alb_page/post_list.html', {})
