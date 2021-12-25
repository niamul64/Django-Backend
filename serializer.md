
```
from django.contrib import admin
from django.db.models.base import Model
from . models import Status

class StatusAdmin(admin.ModelAdmin):                 
      list_display=['user','content','image',] # on admin panel which column we want to show
      class Meta:                              # which model are using 
            model =Status


admin.site.register(Status, StatusAdmin)       # registering
```
<img src="srializer before.JPG" alt="alt" width="46%">

<img src="srializer after.JPG" alt="alt" width="46%">