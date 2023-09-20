import os
import re

import unicodedata
import yaml
from jinja2 import Template

template = """# {{name}}

{{description}}

**Open Source:** {{open_source}}

**Category:** {{category}}

{% if core_features %}
**Core Features:**
{%- for feature in core_features %}
- {{feature}}
{%- endfor %}
{%- endif %}

**Links:** 
{%- if resources %}
{%- for resource in resources %}
- {{resource}}
{%- endfor %}
{%- endif %}
{%- if git_url %}
- [{{git_url}}]({{git_url}})
{%- endif %}
"""

index_template = """# Tools

| Name | Category | Description | License|
| ---- | -------- | ----------- | -------|
{%- for tool in tools %}
| [{{ tool.name }}](./{{ tool.slug }}) | {{ tool.category }} | {{ tool.description  }} | {{ tool.open_source }} | 
{%- endfor %}

"""
with open("tools.yaml") as f:
    doc = yaml.load(f, Loader=yaml.FullLoader)
    for idx, tool in enumerate(doc["tools"]):
        slug = tool["name"]
        slug = unicodedata.normalize("NFKD", slug)
        slug = slug.encode("ascii", "ignore").decode("ascii")
        slug = slug.lower()
        slug = re.sub(r"[^0-9a-z]+", "-", slug)
        slug = slug.strip("-")
        doc["tools"][idx]["slug"] = slug

        open_source = tool["open_source"]
        if type(tool["open_source"]) == bool:
            open_source = "Yes" if open_source else "No"

        os.makedirs(slug, exist_ok=True)
        with open(f"./{slug}/index.md", "w") as f:
            f.write(
                Template(template).render(
                    name=tool["name"],
                    description=tool["description"],
                    open_source=open_source,
                    category=tool["category"],
                    core_features=tool.get("core_features", None),
                    resources=tool.get("resources", None),
                    git_url=tool.get("git_url", None),
                )
            )

        desc = tool["description"] or ""
        doc["tools"][idx]["description"] = desc.replace("\n", " ")

    with open(f"./index.md", "w") as f:
        f.write(
            Template(index_template).render(
                tools=sorted(doc["tools"], key=lambda d: d.get("name").lower()),
            )
        )
