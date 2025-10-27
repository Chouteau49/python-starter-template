# {version} ({project_date})

{% for section in sections %}
{% set section_header = sections[section]['name'] %}
{% if sections[section]['fragments'] %}

### {{ section_header }}

{% for fragment in sections[section]['fragments'] %}
- {{ fragment }}
{% endfor %}

{% endif %}
{% endfor %}
