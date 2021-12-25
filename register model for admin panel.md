# register model
goto admin.py file of the same App where the models are located.
```
# in admin.py file: (# import models: (lets say our app name 'first_app' : with two models: 1.Musician 2. Album))

from .models import Musician, Album
# or we can import like this: from first_app.models import Musician, Album


admin.site.register(Musician)
admin.site.register(Album)
```


# We also can use serialization or serializer in admin panel, to see mor info from admin panel (see: serializer.md)