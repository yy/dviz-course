# Overview of Python visualization tools

These two talks provide pretty good overview of the Python visualization landscape. 

- Jake VanderPlas at PyCon 2017: [The Python Visualization Landscape](https://www.youtube.com/watch?v=FytuB8nFHPQ). 
- James Bednar at AnacondaCon 2018: [PyViz: Dashboards for Visualizing 1 Billion Datapoints in 30 Lines of Python](https://www.youtube.com/watch?v=k27MJJLJNT4). 

# Python environment setup instruction

## Local setup

### Anaconda environment

First download Anaconda for your system (Python 3) from [here](https://www.anaconda.com/download). The `miniconda` is a minimal version on which you need to install necessary packages. If you don't have much space or prefer to install only necessary packages, `miniconda` will suit you. Anaconda comes with a package manager called `conda`. 

If you haven't, you may want to install the core Python data packages. 

```
conda install numpy scipy pandas scikit-learn matplotlib seaborn jupyter
```

Although it is not strictly required, it is a really good practice to use virtual environment for each project. Try to use it for every project! 

By using virtual environments, you can isolate each environment from the others and maintain separate sets (versions) of packages. `conda` has a built-in support for virtual environments. 

```
conda create -n dviz python=3.7
```

This command creates a virtual environment named `dviz` with Python 3.6 and Anaconda. 

You can activate the environment (whenever you begins to work on this course) by running

```
conda activate dviz
```

and deactivate (when you're done) by running

```
conda deactivate 
```

For the full documentation, see https://conda.io/docs/user-guide/tasks/manage-environments.html

### Pipenv

If you are not using Anaconda but using `pip`, a nice option to manage virtual environments is using [`pipenv`](https://pipenv.readthedocs.io/en/latest/). It is similar to conda, but of course can be used without installing Anaconda. 

You can install it by running

```
pip install --user pipenv
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

#### Using pipenv with system Jupyter

To use pipenv-installed packages in your system Jupyter notebook or lab, you need to install `ipykernel` package first. 

```
pipenv install ipykernel
```

Then you can install a custom Python kernel (for your virtual env) for Jupyter by running the following (replace `dviz` with any name you want). 

```
pipenv shell
python -m ipykernel install --user --name=dviz
```

After doing this, you will be able to choose the kernel you created from Jupyter environment. When you click "New", it allows you to choose a kernel from a list. You'll see your kernel (e.g. "dviz...") in this list. 


## Cloud setup

These are good cloud Jupyter notebook options. They are not necessarily supporting every package that we use but they may be an excellent option especially if you have a hard time installing packages. They also allow you to work on your code anywhere with internet access. The best option is Google colaboratory. It allows installation of many packages. It even lets you use GPUs! (although we don't really need to use any). 

### Google colaboratory

[Google Colaboratory](https://colab.research.google.com/) is Google's collaborative Jupyter notebook service. You can install packages by running 

```
!pip install packagename
``` 
I could install every package that we are using on colaboratory. 

### Azure notebooks

Microsoft also has a cloud notebook service called [Azure notebooks](https://notebooks.azure.com/). This service also allows installing new packages through `!pip install ...`. 

### CoCalc

CoCalc (https://cocalc.com/) is a service by [SageMath](http://www.sagemath.org/). You can use it freely but the free version is slow and can be turned off without warning. Most of the packages that we use are pre-installed. We may be able to provide a subscription through the school. 

### Kaggle Kernels

The famous machine learning / data science competition service Kaggle offers cloud-based notebooks called [Kaggle kernels](https://www.kaggle.com/kernels). Because you can directly use all the Kaggle datasets, it is an excellent option to do your project if you use one of the Kaggle datasets. It allows uploading your own dataset and install some packages, but not all packages are supported. 

## Jupyter

Once you have setup your local environment, you can run 

```
jupyter notebook
```

or [Install Jupyter lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) and run:

```
jupyter lab
```

Jupyter lab is the "next generation" interface for the Jupyter project and it has more powerful features. Some packages that we use work more nicely with Jupyter lab too (although for some lab assignments you may need to use jupyter notebook instead of the lab). 


# Lab assignment

1. Set up your local Python environment following the instructions. You should be using a virtual environment on your local machine. 
1. Install Jupyter notebook and Jupyter lab. 
1. Launch jupyter notebook (lab) 
1. Create a new notebook and play with it. Print "Hello world!". 

If you want to use a cloud environment, 

1. Try out the cloud environments listed above. (Google colaboratory is recommended)
1. Try installing the following packages. 

Finally, these are the packages that we plan to use. So check out their homepages and figure out what they are about. 

- Jupyter Notebook and Lab: https://jupyter.org/
- numpy: http://www.numpy.org/
- scipy: http://www.scipy.org/
- matplotlib: http://matplotlib.org/
- seaborn: http://seaborn.pydata.org/
- pandas: http://pandas.pydata.org/
- scikit-learn: http://scikit-learn.org/stable/
- altair: https://github.com/altair-viz/altair
- vega_datasets: https://github.com/altair-viz/vega_datasets
- bokeh: http://bokeh.pydata.org/en/latest/
- datashader: http://datashader.org/
- holoviews: http://holoviews.org/
- wordcloud: https://github.com/amueller/word_cloud
- spacy: https://spacy.io/

Install them using your package manager (conda or pip).

Once you have installed the Jupyter locally or succeeded with a cloud environment, create a notebook and print "Hello world!" using the `print` command. Try to install some of the packages that you installed. I'd strongly recommend you to make sure that you can install and import these packages. 

Save (download) the notebook and submit it on the canvas. 
