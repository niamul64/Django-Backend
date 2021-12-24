## 1. find the avarage value from a column
## 2. find the avarage value from a column based on a condition

## At views.py: 
```
import: from django.db.models import Avg
```
### 1. avg = Model.objects.all().Aggregate(Avg('columnName'))
### 2. avg = Model.objects.all().filter(condition).aggregate(Avg('columnName'))
```
# Example: suppose, our model name is: Album, have a column named 'rating', if the albums artist id matches the find rating avarage
AVG= Album.objects.filter(id=artist_id).aggregate(Avg('rating'))

```