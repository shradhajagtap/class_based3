from django.shortcuts import render, redirect
from django.views import View

from .forms import StudentForm
from .models import Student


class ElectricView(View):
    template_name = "curd_app/info.html"
    form = StudentForm

    def get(self, request):
        form = self.form()
        context = {"form": form}
        return render(request,self.template_name, context)

    def post(self,  request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        return render(request, self.template_name, {"form": form})


class ShowView(View):
    template_name = "curd_app/show.html"
    form = StudentForm

    def get(self, request):
        form = self.form()
        obj = Student.objects.all()
        context = {"obj": obj, "form": form}

        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_url')
        return render(request, self.template_name, {"form": form})


class UpdateView(View):
    template_name = "curd_app/info.html"
    form = StudentForm

    def get(self, request, pk):
        objs = Student.objects.get(id=pk)
        form = self.form(instance=objs)
        context = {"objs": objs, "form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        objs = Student.objects.get(id=pk)
        form = self.form(request.POST, instance=objs)
        if form.is_valid():
            form.save()
            return redirect('show_url')
        return render(request, self.template_name, {"form": form})


class DeleteView(View):
    template_name = "curd_app/confirm.html"
    form = StudentForm

    def get(self, request, pk):
        objs = Student.objects.get(id=pk)
        form = self.form(instance=objs)
        context = {"objs": objs, "form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        obj = Student.objects.get(id=pk)
        obj.delete()
        return redirect("show_url")
