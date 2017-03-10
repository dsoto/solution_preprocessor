'''A simple exporter to strip solution cells from a student assignment document
'''

'''Add
c.Exporter.preprocessors = ['solution_preprocessor.SolutionPreprocessor']
to the `jupyter_nbconvert_config.py` file to use
'''

'''
To pass a flag for whether or not to filter the solution use the
following line with --ClassName.attribute=True
> jupyter nbconvert --to notebook --SolutionPreprocessor.solution=True test.ipynb
'''

from nbconvert.preprocessors import Preprocessor
from traitlets import Bool

class SolutionPreprocessor(Preprocessor):

    solution = Bool(default_value=False, config=True)

    def is_assigned(self, c):
        # cells marked as having slideshow slide metadata are whitelisted
        if hasattr(c.metadata, 'slideshow'):
            if c.metadata.slideshow.slide_type == 'slide':
                return True
            else:
                return False
        else:
            return False

    def preprocess(self, nb, resources):
        if self.solution:
            nb.cells = [c for c in nb.cells if self.is_assigned(c)]
        return nb, resources




