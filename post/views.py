from . import forms
from django.views.generic import CreateView


class CreateOrder(CreateView):
    template_name = "product/create_order.html"
    form_class = forms.OrderForm
    success_url = "/"

    def form_valid(self, form):
        return super().form_valid(form=form)