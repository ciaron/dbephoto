from django.contrib import admin
from photo.models import Album, Image, Tag

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "images"]

class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]

#class ImageAdmin(admin.ModelAdmin):
#    search_fields = ["title"]
#    list_display = ["__unicode__", "title", "user", "rating", "created"]
#    list_filter = ["tags", "albums"]

class ImageAdmin(admin.ModelAdmin):
    # search_fields = ["title"]
    list_display = ["__unicode__", "title", "user", "rating", "size", "tags_", "albums_",
        "thumbnail_", "created"]
    list_filter = ["tags", "albums", "user"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)

