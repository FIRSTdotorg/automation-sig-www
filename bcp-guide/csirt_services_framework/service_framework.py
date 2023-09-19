import requests
import yaml
from bs4 import BeautifulSoup, PageElement
from markdownify import MarkdownConverter


class ServiceArea:
    def __init__(self, id: str, name: str, description: str, services: list):
        self.id = id
        self.name = name
        self.description = description
        self.services = services

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "services": [service.toDict() for service in self.services]
        }


class Service:
    def __init__(self, id: str, name: str, purpose: str, description: str, outcome: str, functions: list):
        self.id = id
        self.name = name
        self.purpose = purpose
        self.description = description
        self.outcome = outcome
        self.functions = functions

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "purpose": self.purpose,
            "description": self.description,
            "outcome": self.outcome,
            "functions": [function.toDict() for function in self.functions]
        }


class Function:
    def __init__(self, id: str, name: str, purpose: str, description: str, outcome: list):
        self.id = id
        self.name = name
        self.purpose = purpose
        self.description = description
        self.outcome = outcome

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "purpose": self.purpose,
            "description": self.description,
            "outcome": self.outcome
        }


def md(soup, **options):
    try:
        return MarkdownConverter(**options).convert_soup(soup)
    except Exception as e:
        return ""


def clean_name(text: str, prefix: str) -> (str, str):
    id = text.split(prefix)[0].strip()
    name = text.split(prefix)[1].strip(":").strip()
    return id, name


def find_paragraph(soup: PageElement, stop: str, term: str) -> str:
    text = ""
    for e in all_siblings_until(soup, stop):
        if term in e.text:
            text += md(e).replace(term, "").strip("*: ")

    return text


def find_functions(h3: BeautifulSoup) -> [Function]:
    functions = []
    for elem in siblings_until(h3, "h4", "h3"):
        if elem.name == "h4":
            id, name = clean_name(elem.text, "Function")
            purpose = find_paragraph(elem, "h4", "Purpose")
            description = find_paragraph(elem, "h4", "Description")
            outcome = find_paragraph(elem, "h4", "Outcome")

            functions.append(Function(id, name, purpose, description, outcome))

    return functions


def find_services(h2: BeautifulSoup) -> [Service]:
    services = []
    for elem in siblings_until(h2, "h3", "h2"):
        if elem.name == "h3":
            id, name = clean_name(elem.text, "Service")
            purpose = find_paragraph(elem, "h3", "Purpose")
            description = find_paragraph(elem, "h3", "Description")
            outcome = find_paragraph(elem, "h3", "Outcome")
            functions = find_functions(elem)

            services.append(Service(id, name, purpose, description, outcome, functions))

    return services


def find_service_areas(resp: requests.Response) -> [ServiceArea]:
    service_areas = []
    soup = BeautifulSoup(resp.text, "html.parser")
    h2s = soup.find_all("h2")
    for h2 in h2s:
        if "Service Area" in h2.text:
            id, name = clean_name(h2.text, "Service Area")
            description = "\n".join([md(elem) for elem in all_siblings_until(h2, "h3")]).strip()
            services = find_services(h2)

            service_areas.append(ServiceArea(id, name, description, services))

    return service_areas


def main():
    resp = requests.get(
        "https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1#7-Service-Area-Vulnerability-Management")

    service_areas = find_service_areas(resp)

    with open("csirt_services_framework.yaml", "w") as f:
        yaml.dump([a.toDict() for a in service_areas], f, indent=2, sort_keys=False)


def all_siblings_until(soup: PageElement, stop: str):
    for sibling in soup.next_siblings:
        if sibling.name == stop:
            break
        yield sibling


def siblings_until(soup: PageElement, sibling_name: str, stop: str):
    for sibling in soup.next_siblings:
        if sibling.name == stop:
            break
        if sibling.name == sibling_name:
            yield sibling


if __name__ == "__main__":
    main()
