from django import template

register= template.Library()

# Now filters are written as function
def my_filter(value, filter_parameter):  # this is custom filter. here 'value' accept the value from HTML carly tag {{ }}
    # now Lets say our filter will add a string with received string
    return value +" "+ filter_parameter

# now register the function as filter
register.filter("custom_filter", my_filter) # now if we call "custom_filter" then 'my_filter' function will work