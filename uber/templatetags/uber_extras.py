from django import template
import datetime

register = template.Library()


@register.filter(name='date_readable')
def date_readable(value):
	"converts unix time to python date time"
	return value.strftime("%Y-%m-%d %H:%M")

@register.filter(name='distance_readable')
def date_readable(value):
	"converts unix time to python date time"
	return round(value, 2)
