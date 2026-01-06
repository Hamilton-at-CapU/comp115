import nbformat as nbf
from glob import glob


def process_cell(cell):
    # get tags
    tags = cell['metadata'].get('tags', [])

    # add hide-cell tag to solutions
    if cell['cell_type'] == 'code':

        # remove outputs
        cell.outputs = []

        # remove solutions
        source = cell['source']
        if source.startswith('# Solution') or 'solution' in tags:
            cell['source'] = []

        # remove %%expect cell magic
        #if source.startswith('%%expect'):
        #    t = source.split('\n')[1:]
        #    cell['source'] = '\n'.join(t)


def process_notebook(source, target):
    ntbk = nbf.read(source, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        process_cell(cell)

    nbf.write(ntbk, target)


# Collect a list of the notebooks in the solutions folders
# select either lesson or lab
directory = 'labs'
#directory = 'lessons'

sources = glob(f"../solutions/{directory}/*.ipynb")

for source in sorted(sources):
    target = f"../workbooks/{directory}/{source.split('/')[-1]}"
    print(f'processing {source} to {target}')
    process_notebook(source, target)
