from django.contrib import admin
from .models import Coordinator,Proposal,Event,SubCoordinator,SubEvent,Volunteer,Participant,Payment,Notification,Memories,Audience,Pass
# Register your models here.

class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'semester','erp')
    list_filter = ('branch','semester')
    search_fields = ['branch','semester']

admin.site.register(Coordinator,CoordinatorAdmin)

class ProposalAdmin(admin.ModelAdmin):
    list_display = ('hodApproval', 'adminApproval', 'status')
    list_filter = ('coordinator','status','createdAt')
    search_fields = ['coordinator','status','createdAt']

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)

admin.site.register(Proposal,ProposalAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_filter = ('coordinator','status','createdAt')
    search_fields = ['coordinator','status','createdAt']

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)

admin.site.register(Event,EventAdmin)

class SubCoordinatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'semester','erp')
    list_filter = ('coordinator','event','branch','semester')
    search_fields = ['coordinator','event']

admin.site.register(SubCoordinator,SubCoordinatorAdmin)

class SubEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'createdAt')
    list_filter = ('coordinator','subcoordinator','event')
    search_fields = ['coordinator','subcoordinator','event']

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)

admin.site.register(SubEvent,SubEventAdmin)

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch','semester','erp')
    list_filter = ('event','subevent','branch','semester','createdAt')
    search_fields = ['event','subevent','branch','semester','createdAt']

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)

admin.site.register(Volunteer,VolunteerAdmin)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch','semester','erp')
    list_filter = ('event','subevent','branch','semester','createdAt')
    search_fields = ['event','subevent','branch','semester','createdAt']

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)

admin.site.register(Participant,ParticipantAdmin)

class AudienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch','semester','erp')
    list_filter = ('event','branch','semester','createdAt')
    search_fields = ['event','branch','semester','createdAt']

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)

admin.site.register(Audience,AudienceAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch','semester','erp','recieptNumber')
    list_filter = ('event','branch','semester')
    search_fields = ['event','branch','semester']

admin.site.register(Payment)

class NotificationAdmin(admin.ModelAdmin):

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)

admin.site.register(Notification,NotificationAdmin)

class MemoriesAdmin(admin.ModelAdmin):
    list_display = ('image', 'createdAt')
    list_filter = ('event','subevent')
    search_fields = ['event','subevent']

admin.site.register(Memories,MemoriesAdmin)

class PassAdmin(admin.ModelAdmin):
    list_display = ('name', 'event','date','uuid')
    list_filter = ('name', 'event','date','uuid')
    search_fields = ['name', 'event','date','uuid']

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)

admin.site.register(Pass,PassAdmin)
