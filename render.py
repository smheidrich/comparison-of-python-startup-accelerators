#!/usr/bin/env python3
# $ pip list | grep -iE '(jinja|pyyaml)'
# Jinja2                            3.0.1
# PyYAML                            5.3.1
from jinja2 import Template
from pathlib import Path
import yaml

t = Template(Path("README.template.md").read_text())
with Path("data.yml").open() as f:
  d = yaml.load(f, Loader=yaml.SafeLoader)
s = t.render(d)
Path("README.md").write_text(s)
