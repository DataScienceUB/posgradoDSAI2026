# Demo: why notebooks are awkward in Git

`analysis_v1.ipynb` and `analysis_v2.ipynb` are the **same analysis**; v2 only changes the title of the first cell
and was **run again**. Compare them in VS Code (select both in the Explorer -> right click -> *Compare Selected*)
and look at how many lines differ because of outputs, `execution_count` and the embedded PNG image.

Then compare again after clearing outputs (*Clear All Outputs* in the notebook toolbar): the real change is one line.
