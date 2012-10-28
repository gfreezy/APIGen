
django_syntax = '''{{ variable_name }}
Example:
   <p> Thanks for placing an order from {{ company }}. </p>


{% if .. %}
   ...
{% else %}
   ...
{% endif %}
Example:
{% if flag %}
    <p>Your warranty information will be included in the packaging.</p>
{% else %}
    <p>You didn't order a warranty, so you're on your own when
    the products inevitably stop working.</p>
{% endif %}


{% for .. %}
   ...
{% endfor %}
Example:
<ul>
{% for item in item_list %}
    <li>{{ item }}</li>
{% endfor %}
</ul>'''

mako_syntax = '''${ variable_name }
Example:
   <p> Thanks for placing an order from ${ company }}. </p>


% if .. :
   ...
% else  :
   ...
% endif
Example:
% if flag :
    <p>Your warranty information will be included in the packaging.</p>
% else :
    <p>You didn't order a warranty, so you're on your own when
    the products inevitably stop working.</p>
% endif


% for .. :
   ...
% endfor
Example:
<ul>
% for item in item_list :
    <li>{{ item }}</li>
% endfor
</ul>

More detailed syntax, usage, please see http://www.makotemplates.org/
'''

jinja_syntax = '''{{ variable_name }}
Example:
   <p> Thanks for placing an order from {{ company }}. </p>


{% if .. %}
   ...
{% else %}
   ...
{% endif %}
Example:
{% if flag %}
    <p>Your warranty information will be included in the packaging.</p>
{% else %}
    <p>You didn't order a warranty, so you're on your own when
    the products inevitably stop working.</p>
{% endif %}


{% for .. %}
   ...
{% endfor %}
Example:
<ul>
{% for item in item_list %}
    <li>{{ item }}</li>
{% endfor %}
</ul>

More detailed syntax, usage, please see http://jinja.pocoo.org/docs/templates/
'''
