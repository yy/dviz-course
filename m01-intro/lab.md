# Setup instructions

## Local setup

### Anaconda environment

First download Anaconda for your system (Python 3.6) from [here](https://www.anaconda.com/download). The `miniconda` is a minimal version on which you need to install necessary packages. If you don't have much space or prefer to install only necessary packages, `miniconda` will suit you. Anaconda comes with a package manager called `conda`. 

If you haven't, you may want to install the core Python data packages. 

```
conda install numpy scipy pandas scikit-learn matplotlib seaborn jupyter
```

Although it is not strictly necessary, it is a good practice to use virtual environment for each project. By doing so, you can isolate each environment from each other and maintain packages separately. In this case, you would want to have a virtual environment for the course. `conda` has a built-in support for virtual environments. 

```
conda create -n dviz python=3.6 
```

This command creates a virtual environment named `dviz` with Python 3.6 and Anaconda. 

You can activate the environment by running

```
source activate dviz
```

and deactivate by running

```
source deactivate dviz
```

For the full documentation, see https://conda.io/docs/user-guide/tasks/manage-environments.html

### Pipenv

If you are not using Anaconda but using `pip`, a nice option to manage virtual environments is using [`pipenv`](https://pipenv.readthedocs.io/en/latest/). It is similar to conda, but of course can be used without installing Anaconda. 

You can install it by running

```
pip install --user pipenv
```

On a mac, you can also install through [homebrew](https://brew.sh/):

```
brew install pipenv
```

Check out the full documentation about installation: https://pipenv.readthedocs.io/en/latest/install


Once you have installed it, you can download the `pipfile` for the course from [here](https://github.com/yy/dviz-course/blob/master/Pipfile) and put it in your work directory (or you can simply clone the repo and work on it), then run 

```
pipenv install
```

This command performs several actions. First it reads necessary packages from `pipfile`, then it creates a new virtual environment, and then install these packages into the newly created virtual environment. If you want to install a new package, you run 

```
pipenv install package-name
```

If you want to use the virtual environment, run

```
pipenv shell
```

If you want to deactivate the virtual env, you can simply type `exit`. 

## Cloud setup

- Anaconda cloud: https://anaconda.org/
- CoCalc: https://cocalc.com/
- Kaggle Kernels: https://www.kaggle.com/kernels
- Google Colaboratory: https://colab.research.google.com/

## Other visualization tools

- R: https://www.r-project.org
    - [ggplot2](http://ggplot2.org)
    - [Rstudio](https://www.rstudio.com) 
- Processing: https://processing.org
    - http://processingjs.org - Javscript-based processing
    - [p5.js](https://p5js.org/)
- Tableau: http://www.tableau.com
- D3.js: http://d3js.org 
    - http://yyahnwiki.appspot.com/D3.js
    - [NVd3](http://nvd3.org/index.html)
    - [D3plus](http://d3plus.org)

