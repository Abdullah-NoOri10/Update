from django.forms import ModelForm
from .models import Product,Companie


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['marketer', 'distributor','image']

class EditCompanyForm(ModelForm):
    class Meta:
        model = Companie
        exclude = ['user']

class EditProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['distributor']

    def clean_picture(self):
       picture = self.cleaned_data.get("image")
       if not picture:
           raise forms.ValidationError("No image!")
       else:
           w, h = get_image_dimensions(picture)
           if w != 100:
               w = 100
           if h != 200:
               h = 200
       return picture

# class ProductPictureForm(ModelForm):
#     class Meta:
#         model = Product

#     def clean_picture(self):
#        picture = self.cleaned_data.get("picture")
#        if not picture:
#            raise forms.ValidationError("No image!")
#        else:
#            w, h = get_image_dimensions(picture)
#            if w != 100:
#                w = 100
#            if h != 200:
#                h = 200
#        return picture

