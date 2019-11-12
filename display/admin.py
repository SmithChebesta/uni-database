from django.contrib import admin
from . import models
from django.shortcuts import redirect
# Register your models here.
# admin.site.register(models.Tag)
# admin.site.register(models.Webapp)
# admin.site.register(models.Customer)
# admin.site.register(models.service)
# admin.site.register(models.Gateway)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/')

    def response_change(self, request, obj):
        return redirect('/')

    def response_delete(self, request, obj_display, obj_id):
        return redirect('/')


@admin.register(models.Webapp)
class WebappAdmin(admin.ModelAdmin):
    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/webapp')

    def response_change(self, request, obj):
        return redirect('/webapp')

    def response_delete(self, request, obj_display, obj_id):
        return redirect('/webapp')


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/customer')

    def response_change(self, request, obj):
        return redirect('/customer')

    def response_delete(self, request, obj_display, obj_id):
        return redirect('/customer')


@admin.register(models.service)
class serviceAdmin(admin.ModelAdmin):
    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/service')

    def response_change(self, request, obj):
        return redirect('/service')

    def response_delete(self, request, obj_display, obj_id):
        return redirect('/service')


@admin.register(models.Gateway)
class GatewayAdmin(admin.ModelAdmin):
    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/gateway')

    def response_change(self, request, obj):
        return redirect('/gateway')

    def response_delete(self, request, obj_display, obj_id):
        return redirect('/gateway')
