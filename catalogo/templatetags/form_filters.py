from django import template

register = template.Library()

@register.filter
def add_class(field, css):
    return field.as_widget(attrs={"class": css})

@register.filter
def widget_name(field):
    """Devuelve el nombre de la clase del widget, permitido en Django templates."""
    return field.field.widget.__class__.__name__

@register.filter
def widget_name(field):
    return field.field.widget.__class__.__name__
