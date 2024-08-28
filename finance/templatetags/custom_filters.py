from django import template

register = template.Library()

@register.filter(name='format_currency')
def format_currency(value):
    try:
        # Tente converter o valor para float
        numeric_value = float(value)

        # Formate o valor como uma string com duas casas decimais e ponto com separador de milhar
        formatted_value = '{:,.2f}'.format(numeric_value)

        # Adicione o simbolo da moeda brasileira R$
        formatted_value = 'R$ ' + formatted_value.replace(',', 'v').replace('.', ',').replace('v', '.')

        return formatted_value
    except (ValueError, TypeError):
        # Trate o caso em que a conversão para float falha
        return value