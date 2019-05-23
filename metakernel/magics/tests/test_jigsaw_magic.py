
from metakernel.tests.utils import (get_kernel, get_log_text,
                                    clear_log_text, EvalKernel, has_network)
import os
import pytest


@pytest.mark.skipif(not has_network())
def test_jigsaw_magic():
    kernel = get_kernel(EvalKernel)
    kernel.do_execute("%jigsaw Processing --workspace workspace1")
    text = get_log_text(kernel)
    assert os.path.isfile("workspace1.html"), "File does not exist: workspace1.html"

def teardown():
    for fname in ['workspace1.html']:
        try:
            os.remove(fname)
        except:
            pass
