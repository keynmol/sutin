import glob
import os
import shutil

pj = os.path.join

SUTIN_ROOT = os.path.dirname(os.path.dirname(__file__))
TEMPLATES_ROOT = pj(SUTIN_ROOT, "templates")

def list_templates(folder):
    if os.path.exists(folder):
        return {os.path.basename(f): f for f in glob.glob(os.path.join(folder, "*")) if os.path.isdir(f)}

    return {}

def get_templates():
    templates = list_templates(os.path.expanduser(TEMPLATES_ROOT))
    templates.update(list_templates(os.path.expanduser("~/.sutin")))

    return templates

def is_empty(folder):
    return not os.path.exists(folder) or os.listdir(folder) == []

def prepare(folder, template):
    os.makedirs(folder, exist_ok=True)

    files = os.listdir(template)

    for f in files:
        template_file = pj(template, f)
        if os.path.isdir(template_file):
            shutil.copytree(template_file, pj(folder, f))
        else:
            shutil.copy(template_file, pj(folder, f))
