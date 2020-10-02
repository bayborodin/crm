from django.contrib import admin
from django.utils.safestring import mark_safe

from offerings.models import Offering, OfferingGroup, SparePart, SparePartImage


def get_picture_preview(obj):
    if obj.pk:
        src = obj.primary_image.url
        title = obj.name
        return mark_safe(
            f"<a href='{src}' target='_blank'><img src='{src}'\
                alt='{title}' style='max-width: 200px; max-height: 200px;'></a>"
        )
    return '(выберите картинку для просмотра)'


get_picture_preview.short_description = 'Предпросмотр'


def get_picture_thumb(obj):
    if obj.pk and obj.primary_image:
        src = obj.primary_image.url
        title = obj.name
        return mark_safe(
            f"<a href='{src}' target='_blank'><img src='{src}'\
                alt='{title}' style='max_width: 60px; max-height: 60px;'></a>"
        )


get_picture_thumb.short_description = 'Фото'


class SparePartImageInline(admin.StackedInline):
    model = SparePartImage
    extra = 0


class OfferingGroupAdmin(admin.ModelAdmin):
    """Offering group admin."""

    list_display = ['name', 'enabled']


class OfferingAdmin(admin.ModelAdmin):
    """Offering admin."""

    list_display = [
        'code_1c', 'name', 'group', 'bulk_price', 'retail_price', 'enabled',
    ]
    list_filter = ['group', 'enabled']


class SparePartAdmin(admin.ModelAdmin):
    """Spare part admin."""

    fields = [
        'code_1c',
        'name',
        'mark',
        'description',
        'tags',
        'equipment',
        'net_weight',
        'gross_weight',
        'length',
        'width',
        'height',
        'primary_image',
        get_picture_preview,
    ]

    readonly_fields = [get_picture_preview]

    list_display = [
        'code_1c', 'name', 'net_weight', 'gross_weight', get_picture_thumb,
    ]
    list_filter = ['code_1c', 'name']
    inlines = [SparePartImageInline]


admin.site.register(OfferingGroup, OfferingGroupAdmin)
admin.site.register(Offering, OfferingAdmin)
admin.site.register(SparePart, SparePartAdmin)
