# Installing Python for data analysis and visualization

## Anaconda

[Continuum Analytics][continuum], a data analysis company, provides a nice Python distribution for data analysis and visualization. It is called [Anaconda][conda] and you can freely download and use. It is usually the easiest solution to install and maintain necessary Python packages for data analysis, regardless of your platform. Here is the download link:

- [Download Anaconda (Python3.5)](http://continuum.io/downloads)

After installing it, you can keep it updated by executing `conda`. 

    conda update conda
    conda update anaconda

With `conda`, you can also install many Python packages. For instance:

    conda install pandas

## Without Anaconda

If you use Mac or Linux and does not want to use Anaconda, you can install packages by using Python's `pip` program.  Install Python using either [homebrew][brew] or the [official Python download][python-download]. Use `pip` (or `pip3`) to install necessary packages. You can run

     pip3 install numpy scipy ipython pandas matplotlib seaborn bokeh scikit-learn

to install most packages that you can use for data analysis and visualization.

## Jupyter notebook

Once you have `Jupyter notebook` (`Anaconda` creates a shortcut), you can simply run 

    jupyter notebook 

in the shell or use the launcher to launch ipython notebook. A browser window will appear and show the `Jupyter notebook` interface. From here, you can create your notebooks and load other notebooks.  

## Wakari.io

Another very convenient way to use the Python stack is using a web-based Python data analysis platform, such as [Wakari.io][wakari]. This is a service provided by [Continuum Analytics][continuum]. You can set up your environment by installing necessary packages and uploading your datasets. Then you can use IPython notebook (Jupyter) online. 


[conda]: http://continuum.io/downloads
[python-download]: https://www.python.org/downloads/
[brew]: http://brew.sh/
[continuum]: http://continuum.io/about-continuum
[wakari]: https://wakari.io
