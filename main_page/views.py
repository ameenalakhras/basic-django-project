from django.shortcuts import render


def main_page(request):
    """
    the main page of the website
    """

    return render(request, template_name="main_page.html" ,context=None )

def temp_page(request):
    """
    the main page of the website
    """

    return render(request, template_name="temp_page.html" ,context=None )
