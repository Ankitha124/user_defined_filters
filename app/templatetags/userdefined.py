from django import template
register=template.Library()

@register.filter()
def swap(data):
    return data.swapcase()


@register.filter()
def remove(data,arg):
    return data.replace(arg,'')

@register.filter()
def spremove(data,sub):
    c=0
    for i in range(len(data)):
        if data[i:i+len(sub):]==sub:
            c+=1
    return c

import re
@register.filter()
def count(data,sub):
    return len(re.findall(sub,data))






    
    
    


