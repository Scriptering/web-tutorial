from django.shortcuts import render
import datetime

# Create your views here.
def newyear(request):
    today = datetime.date(datetime.date.today)
    is_new_year = (
        today.month == 1 & today.day == 1
    )

    background_colour = "white" if is_new_year else "black"
    text = "yes" if is_new_year else "no"

    render(request, "/newyear/newyear.html", {
        "is_new_year": is_new_year
    })
    