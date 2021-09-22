from django.contrib import admin
from .models import sleep, activity, readiness

# registering models in order to make them editable from the django admin page

admin.site.register(sleep)
admin.site.register(activity)
admin.site.register(readiness)