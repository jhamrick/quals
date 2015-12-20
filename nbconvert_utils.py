import os
import re
import datetime
from nbconvert.preprocessors import Preprocessor
from nbconvert.postprocessors import PostProcessorBase


class ExtractTitle(Preprocessor):

    def preprocess(self, nb, resources):
        first = nb.cells[0]
        if first.cell_type == 'markdown':
            lines = first.source.split('\n')
            m = re.match(r'^#(?P<title>[^#]+)', lines[0])
            if m:
                resources['metadata']['title'] = m.groupdict()['title'].strip()
                self.log.info("Title is '{}'".format(resources['metadata']['title']))
                if len(lines) == 1:
                    nb.cells = nb.cells[1:]
                else:
                    first.source = '\n'.join(lines[1:])

        now = datetime.datetime.now()
        resources['metadata']['date'] = now.strftime("%Y-%m-%d %H:%M:%S")

        return super(ExtractTitle, self).preprocess(nb, resources)

    def preprocess_cell(self, cell, resources, cell_index):
        return cell, resources


class Rename(PostProcessorBase):

    def postprocess(self, path):
        now = datetime.datetime.now()
        dirname, filename = os.path.split(path)
        new_name = "{year}-{month:02d}-{day:02d}-{name}-ipynb.md".format(
            year=now.year,
            month=now.month,
            day=now.day,
            name=os.path.splitext(filename)[0])
        new_path = os.path.join('_posts', new_name)
        self.log.info("Renaming '{}' --> '{}'".format(path, new_path))
        os.rename(path, new_path)
