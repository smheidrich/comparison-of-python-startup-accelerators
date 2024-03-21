# Comparison of Python startup accelerators

It is sometimes claimed that there are more Python startup acceleration
utilities than cells in the human body.
Here I compare them all.

*Did I miss one or do you have suggestions for other criteria? Feel free to
[open an issue](https://github.com/smheidrich/comparison-of-python-startup-accelerators/issues/new)!*


## Comparison

All of them employ the same basic principle: There is a server process which,
when launched, does your application's expensive startup work (typically
imports, but could be other things) and then runs in the background, waiting
for clients. When a user launches your actual application, they're really
launching a client which connects to this server. The server forks off a copy
of itself which runs the "main" (i.e. non-init) part of your application, which
launches much faster because all the init work is already done. The client's
input and output streams as well as environment and CLI args are
attached/forwarded to the server process so the experience is otherwise the
same as running the application directly.

<table>
  <tr>
    <th>Name / URL</th>
    <th>Client written in</th>
    <th>Server written in</th>
    <th>Implicit server launch</th>
    <th>Association between script and preload state</th>
    <th>Packaging integration / entrypoints</th>
  </tr>
  {%- for project in projects %}
  <tr>
    <td>
      <a href="{{ project.pypi_url }}">
        {{ project.name }}
      </a>
    </td>
    <td>
      {{ project.client_lang }}
    </td>
    <td>
      {{ project.server_lang }}
    </td>
    <td>
      {% if project.implicit_server_launch %}✅{% else %}❌{% endif %}
    </td>
    <td>
      {% if project.association %}✅{% else %}❌{% endif %} {{ project.association_details }}
    </td>
    <td>
      {% if project.packaging_integration %}✅{% else %}❌{% endif %}
    </td>
  </tr>
  {%- endfor %}
</table>

