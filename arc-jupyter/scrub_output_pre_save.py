
def scrub_output_pre_save(model, **kwargs):
    """scrub output before saving notebooks"""
    # only run on notebooks
    if model['type'] != 'notebook':
        return

    # only run on nbformat v4
    if model['content']['nbformat'] != 4:
        return

    # only run for arc kernel
    if model['content']['metadata']['kernelspec']['name'] != 'arc':
        return

    for cell in model['content']['cells']:
        if cell['cell_type'] != 'code':
            continue
        cell['outputs'] = []
        cell['execution_count'] = None
        cell['metadata'] = {}


c.FileContentsManager.pre_save_hook = scrub_output_pre_save
