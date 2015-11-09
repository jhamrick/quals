"""
Source: http://mcwitt.github.io/2015/04/29/jekyll_blogging_with_ipython3/
"""

from urllib.parse import quote  # Py 3
import os


def path2url(path):
    """Turn a file path into a URL"""
    parts = path.split(os.path.sep)
    return '{{ site.baseurl }}/notebooks/' + '/'.join(quote(part) for part in parts)

################################################################################

c = get_config()
c.NbConvertApp.export_format = 'markdown'
c.MarkdownExporter.template_file = 'jekyll-post'
c.FilesWriter.build_directory = 'notebooks'
c.MarkdownExporter.filters = {'path2url': path2url}
c.Exporter.preprocessors = ['jekyll_nbconvert.ExtractTitle']
c.NbConvertApp.postprocessor_class = 'jekyll_nbconvert.Rename'
