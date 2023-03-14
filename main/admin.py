from django.contrib import admin
from .models import Services, Menu, Category, Special_Dishes, Podeia, Gallery, Reservation


admin.site.register(Reservation)

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    model = Services
    list_display = ['title', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ['title', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']
    list_filter = ['is_visible']

@admin.register(Podeia)
class EventsAdmin(admin.ModelAdmin):
    model = Podeia
    list_display = ['title', 'position', 'is_visible', 'photo', 'month']
    list_editable = ['position', 'is_visible', 'photo']
    list_filter = ['is_visible']

@admin.register(Special_Dishes)
class SpecialDishesAdmin(admin.ModelAdmin):
    model = Special_Dishes
    list_display = ['title', 'position', 'ingredients', 'price', 'photo', 'is_visible', 'discount']
    list_filter = ['is_visible']
    list_editable = ['position', 'is_visible', 'photo', 'price', 'discount']

class MenuAdmin(admin.TabularInline):
    model = Menu
    raw_id_fields = ['category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']
    inlines = [MenuAdmin]

@admin.register(Menu)
class DishAllAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ['title', 'position', 'ingredients', 'price', 'photo', 'is_visible', 'category', 'recommended', 'is_special']
    list_filter = ['category', 'recommended', 'is_visible', 'is_special']
    list_editable = ['position', 'is_visible', 'category', 'photo', 'price']