from django.shortcuts import redirect, render
from .forms import StudentForm

# Create your views here.
def index(request):
    return render(request, "student/index.html")

def student_page(request):

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data.get("first_name")
            student_surname = form.cleaned_data.get("last_name")
            student_number = form.cleaned_data.get("number")

            print(student_name, student_surname, student_number)
            print(form)
            return redirect("index")

        context = {
            "form": form
        }
        return render(request, "student/student_form.html", context)

    form = StudentForm()
    context = {
        "form": form
    }
    return render(request, "student/student_form.html", context)

