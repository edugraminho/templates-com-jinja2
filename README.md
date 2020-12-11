{% macro post_macro(author) -%}

<!-- 
{% macro post_macro(author, date_post, email, title, text) -%}

Deve conter uma macro que reproduza um card de uma postagem
Deve-se utilizar o filtro upper para tornar o título todo em caixa alta -->
<h1> {{ author }}</h1>
<!-- <ul>
  <div class="card" style="width: 18rem">
    <div class="card-body">
      <h5 class="card-title">{{ title | upper }}</h5>
      <h6 class="card-subtitle mb-2 text-muted">{{ text }}</h6>
      <p class="card-text">{{ author }} - {{ email }}</p>
    </div>
  </div>
</ul> -->

{%- endmacro %}
