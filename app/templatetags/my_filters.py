from django import template

register = template.Library()


@register.filter
def val2color(value):
    if value[0] != "Суммарная" and value[0] != "Год":
        try:
            if float(value[1]) < 0:
                return "green"
            elif float(value[1]) < 1:
                return "white"
            elif float(value[1]) < 2:
                return "red"
            elif float(value[1]) < 5:
                return "firebrick"
            elif float(value[1]) >= 5:
                return "darkred"
        except ValueError:
            return "white"
    elif value[0] == "Суммарная":
        return "grey"
    else:
        return "white"


@register.filter
def if_text(value):
    if value[1] == "":
        return "-"
    return value[1]