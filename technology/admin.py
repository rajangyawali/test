from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from .models import AllNews, TechNews, TelcoNews, GadgetNews, GlobalNews, NewsPost, Search

#Customizing Admin Page with ModelAdmin
#first inherit ImportExportModelAdmin and then admin.ModelAdmin
#otherwise there will be error in inheritance
#ImportExportModelAdmin is for showing import and export options in Django Administration
#admin.ModelAdmin is for displaying lists, links and filter options
class AllNewsModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["title", "description", "author", "posted", "scrapped"]
    list_display_links = ["description"]
    list_filter = ["author", "posted","scrapped"]
    search_fields = ["title", "content", "user"]
    class Meta:
        model = AllNews

class TechNewsModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["title", "description", "author", "posted", "scrapped"]
    list_display_links = ["description"]
    list_filter = ["author", "posted","scrapped"]
    search_fields = ["title", "content", "user"]
    class Meta:
        model = TechNews

class TelcoNewsModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["title", "description", "author", "posted", "scrapped"]
    list_display_links = ["description"]
    list_filter = ["author", "posted","scrapped"]
    search_fields = ["title", "content", "user"]
    class Meta:
        model = TelcoNews

class GadgetNewsModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["title", "description", "author", "posted", "scrapped"]
    list_display_links = ["description"]
    list_filter = ["author", "posted","scrapped"]
    search_fields = ["title", "content", "user"]
    class Meta:
        model = GadgetNews

class GlobalNewsModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["title", "description", "author", "posted", "scrapped"]
    list_display_links = ["description"]
    list_filter = ["author", "posted","scrapped"]
    search_fields = ["title", "content", "user"]
    class Meta:
        model = GlobalNews

    
class NewsPostModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["user", "title", "content", "timestamp", "publish_date", "updated"]
    list_display_links = ["content"]
    # list_editable = ["title"]
    list_filter = ["user", "timestamp", "updated"]
    search_fields = ["user", "title", "content"]
    class Meta:
        model = NewsPost

class SearchModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["user", "search", "timestamp"]
    class Meta:
        model = Search

# Register your models here.
admin.site.register(AllNews, AllNewsModelAdmin) #Registering AllNewsModelAdmin Class
admin.site.register(TechNews, TechNewsModelAdmin) #Registering TechNewsModelAdmin Class
admin.site.register(TelcoNews, TelcoNewsModelAdmin) #Registering TelcoNewsModelAdmin Class
admin.site.register(GadgetNews, GadgetNewsModelAdmin) #Registering GadgetNewsModelAdmin Class
admin.site.register(GlobalNews, GlobalNewsModelAdmin) #Registering GlobalNewsModelAdmin Class
admin.site.register(NewsPost, NewsPostModelAdmin) #Registering NewsPostModelAdmin Class
admin.site.register(Search, SearchModelAdmin) #Registering SearchModelAdmin Class