"""Interactive Labeler

This module includes an InteractiveLabeler.
"""
from six.moves import input

from libact.base.interfaces import Labeler
from libact.utils import inherit_docstring_from


class InteractiveLabeler(Labeler):

    """Interactive Labeler

    InteractiveLabeler is a Labeler object that shows the feature text through
    in the command line. For images objects, please refer to the original code,
    not this forked repository.

    Parameters
    ----------
    label_name: list
        Let the label space be from 0 to len(label_name)-1, this list
        corresponds to each label's name.

    """

    def __init__(self, **kwargs):
        self.label_name = kwargs.pop('label_name', None)

    @inherit_docstring_from(Labeler)
    def label(self, text):
        if self.label_name is not None:
            print(f"Current labels: {str(self.label_name)}")

        banner = f"Enter the associated label with the text: '{text}' "

        label = input(banner)

        if self.label_name is None:
            self.label_name = [label]
            return 0
        else:
            if label in self.label_name:
                return self.label_name.index(label)
            else:
                self.label_name.append(label)
                return len(self.label_name) - 1
