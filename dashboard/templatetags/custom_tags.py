from django import template

register = template.Library()


def getgeneallele(value, arg):
    return value[arg]

register.filter('getgeneallele', getgeneallele)

def counter_one(value):
    return value

register.filter('counter_one', counter_one)