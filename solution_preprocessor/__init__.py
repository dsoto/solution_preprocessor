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

'''
This is the metadata format the preprocessor is expecting

"solutions": {
        "visible_in_assignment": true
    }
'''

from nbconvert.preprocessors import Preprocessor
from traitlets import Bool

class SolutionPreprocessor(Preprocessor):

    assignment = Bool(default_value=True, config=True)

    def is_visible_in_assignment(self, c):
        # only cells marked as being visible in assignment are whitelisted
        if hasattr(c.metadata, 'solutions'):
            if c.metadata.solutions.visible_in_assignment == True:
                return True
            else:
                return False
        else:
            return False

    def preprocess(self, nb, resources):
        # if we are creating a solution, we leave cells alone
        # if we are creating an asssignment, only copy whitelisted cells
        if self.assignment == True:
            nb.cells = [c for c in nb.cells if self.is_visible_in_assignment(c)]
        return nb, resources




