"""Cinder Notes: notebook to structured report export."""

import json
from pathlib import Path


def collect_cells(notebook):
    cells = []
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            cells.append(''.join(cell.get('source', [])))
    return cells


def render(cells, templates):
    sections = templates['sections']
    output = []
    for index, heading in enumerate(sections):
        output.append('## ' + heading)
        if index < len(cells):
            output.append(cells[index])
    return '\n\n'.join(output)


def build(notebook_path, template_path):
    notebook = json.loads(Path(notebook_path).read_text(encoding='utf-8'))
    templates = json.loads(Path(template_path).read_text(encoding='utf-8'))
    return render(collect_cells(notebook), templates)
