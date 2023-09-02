from django.contrib import admin
from courses.models import Course,Tag,Prerequisite,Learning,Video

class TagAdmin(admin.TabularInline):
    model=Tag

class PrerequisiteAdmin(admin.TabularInline):
    model=Prerequisite

class LearningAdmin(admin.TabularInline):
    model=Learning

class VideoAdmin(admin.TabularInline):
    model=Video







class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin , LearningAdmin , PrerequisiteAdmin,VideoAdmin ]
    list_display = ["name"]
    list_filter = ("discount" , 'active')

class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course,CourseAdmin)
admin.site.register(Video,VideoAdmin)


# Register your models here.
