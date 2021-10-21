from jinja2 import (
    Environment,
    PackageLoader, select_autoescape,
    Template
)


template = Template(
    'for i in range({{ number }}): print("{{ the }}")'
)
with open('example.py', 'w') as file:
    file.write(template.render(the="variables", number=5))
