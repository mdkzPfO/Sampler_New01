from django.contrib import admin
from .models import SamplingModel,ReportModel,AnimalModel
# Register your models here.
admin.site.register(SamplingModel)
admin.site.register(ReportModel)
admin.site.register(AnimalModel)
