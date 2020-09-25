# cubesat_controls_playground
Playground for experimenting with models of cubsat control 

## Setup
1. Create a conda environment based on the `env.yaml` with the comand `conda env create -f env.yml`
2. Activate the conda environment with `conda activate cubesat` and add it to your jupyter lab with `ipython kernel install --user --name=cubesat`
3. Run `jupyter labextension install @jupyter-widgets/jupyterlab-manager && jupyter labextension install jupyter-matplotlib && jupyter nbextension enable --py widgetsnbextension` for interactive plots in jupyter lab
4. With `cubesat` environment active run `jupyter lab` in the terminal
