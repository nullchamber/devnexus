from django import template, forms
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.db.models import Count


register = template.Library()


@register.filter
def format_article(text):
    paragraphs = text.split("\n")
    paragraphs = list(filter(lambda p: len(p) > 0, paragraphs))
    paragraphs = [p.replace('\t', '<p>') for p in paragraphs]
    article = "</p>".join(paragraphs)
    return format_html(article)



@register.filter(name="label")
def style_label(element, css_class):
    label = element.label
    id_for_label = element.id_for_label or ""
    return format_html(
        f'<label for="{id_for_label}" class="{css_class}">{label}</label>'
    )


@register.filter(name="field")
def style_field(field, css_class):
    classes = field.field.widget.attrs.get("class", "")
    return field.as_widget(
        attrs={
            'class': f'{classes} {css_class}'
        }
    )


@register.filter(name="textarea")
def is_textarea(field):
    return isinstance(field, forms.Textarea)


@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
    