from django.contrib import admin
from . models import Category,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','description']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','availability']
    list_editable = ['price','stock','availability']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 16
admin.site.register(Product,ProductAdmin)
