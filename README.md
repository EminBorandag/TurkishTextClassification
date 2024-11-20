<h1 align="center">Hi 👋, I'm LSRM : A new method for Turkish Text Classification</h1>

<h3 align="justify">This repository contains code for the project LSRM. The project focuses on utilizing BERT, RoBERTa, and BERTurk models for text classification tasks, as well as exploring different embedding techniques such as Word2Vec, Doc2Vec, FastText, and Glove.

Repository Structure

Berts (This folder contains all the results related to the BERT, RoBERTa, and BERTurk models.
Embedding (This folder contains the results obtained using Word2Vec, Doc2Vec, FastText, and Glove embedding techniques.
Db (In this folder, you can find the datasets generated using the LSRM approach, as well as the original datasets used in the project.)
Code (The code for the developed method (LSRM) can be found in the repository as well.)</h3>


<h3 align="justify">The present research focused on various machine learning (ML), deep learning (DL), word embedding (WEm), and transfer learning (TL) algorithms for classifying Turkish texts. The study utilized algorithms such as NB, SMO, KNN, J48, RF for ML; CNN, LSTM, GRU for DL; Doc2Vec, Word2Vec, Glove, FastText for WEm; and Bert, RoBERTa, BerTURK for TL. Three different data sets were used to evaluate the text classification performance in the Turkish language. A new method called LSRM was also introduced to enhance text classification for languages like Turkish with agglutinative features. The study made several contributions to the literature, including running various algorithms individually on Turkish text data sets, comparing classification success rates, investigating the impact of WEm algorithms combined with DL algorithms, and introducing a new data set that reflects changes in Turkish word usage over time with timestamp-enabled data.</h3>

Approach and pipeline:
Refer to the report (The link to the publication. (it will be added if it is accepted for publication) for the approach and implementation.)

<h3 align="justify">Results:</h3>

<h3 align="justify"> The research examined how the Turkish language has evolved over time by analyzing a new dataset called TbTT, which includes news articles from newspapers. The findings of the study showed that the model created was successful in accurately determining the time period of news articles in the dataset by analyzing the words used, achieving a high accuracy rate of almost 97%. </h3>

<h3 align="justify">System Requirements and Lab Environment</h3>
<h3 align="justify">This research project developed a software system using the Python programming language v3.8.5, incorporating the Natural Language Toolkit (NLTK) v3.5 for natural language processing. The study utilized Numpy v1.19.2 for multidimensional array and matrix processing in Python. Matplotlib and Seaborn v0.11.0 were chosen for graphical plotting, while Gensim v4.0.1 was used for vectoring structures and Pandas v1.1.3 for data processing. The experiments were conducted on a computer with 16 GB of RAM, an Intel i7 7700hq 64-bit processor, and an Nvidia GTX 1050 graphics card, running on Linux Ubuntu OS.</h3>

<h3 align="justify">Pip list<br></h3>
<p>Package &Version</p>
<h5>
absl-py               0.1.13
appdirs               1.4.3
astor                 0.6.2
attrs                 19.3.0
audioread             2.1.6
backcall              0.2.0
bleach                1.5.0
Brotli                1.0.2
certifi               2018.4.16
cffi                  1.11.5
chardet               3.0.4
cloudpickle           0.5.2
colorama              0.3.9
cycler                0.10.0
dask                  0.17.2
decorator             4.2.1
defusedxml            0.6.0
docopt                0.6.2
entrypoints           0.3
future                0.16.0
gast                  0.2.0
graphviz              0.8.4
grpcio                1.11.0
h5py                  2.8.0
html5lib              0.9999999
idna                  2.7
imageio               2.8.0
importlib-metadata    1.6.1
imutils               0.5.3
intel-openmp          2018.0.3
ipykernel             5.3.0
ipython               7.15.0
ipython-genutils      0.2.0
jams                  0.3.2
jedi                  0.12.1
Jinja2                2.11.2
joblib                0.12.0
json5                 0.9.5
jsonpickle            0.9.6
jsonschema            3.2.0
jupyter-client        6.1.3
jupyter-core          4.6.3
jupyterlab            2.1.4
jupyterlab-server     1.1.5
Keras                 2.2.2
Keras-Applications    1.0.4
Keras-Preprocessing   1.0.2
keras-unet            0.0.7
kiwisolver            1.0.1
Lasagne               0.1
librosa               0.6.2
llvmlite              0.24.0
locket                0.2.0
Markdown              2.6.11
MarkupSafe            1.1.1
matplotlib            2.2.2
mir-eval              0.4
mistune               0.8.4
mkl                   2018.0.3
more-itertools        4.1.0
muda                  0.2.0
nbconvert             5.6.1
nbformat              5.0.7
networkx              2.1
nose                  1.3.7
notebook              6.0.3
numba                 0.39.0
numexpr               2.7.1
numpy                 1.16.1
opencv-contrib-python 3.4.4.19
opencv-python         3.4.4.19
panda                 0.3.1
pandas                0.23.3
pandocfilters         1.4.2
parso                 0.3.1
partd                 0.3.8
pickleshare           0.7.5
Pillow                5.1.0
pip                   18.0
progressbar           2.5
prometheus-client     0.8.0
prompt-toolkit        3.0.5
protobuf              3.5.2.post1
ptpython              0.41
PyAudio               0.2.11
pycparser             2.18
pydot                 1.2.4
Pygments              2.2.0
pyodbc                4.0.22
pyparsing             2.2.0
pyrsistent            0.16.0
pyrubberband          0.3.0
PySoundFile           0.9.0.post1
python-dateutil       2.7.2
python-git            2018.2.1
python-snappy         0.5.2
pythonnet             2.4.0.dev0
pytools               2018.3
pytz                  2018.4
PyWavelets            0.5.2
pywin32               228
pywinpty              0.5.7
PyYAML                3.12
pyzmq                 19.0.1
requests              2.19.1
resampy               0.2.1
scikit-image          0.16.2
scikit-learn          0.19.2
scikit-neuralnetwork  0.7
scipy                 1.2.1
seaborn               0.9.0
Send2Trash            1.5.0
setuptools            39.0.1
sharedmem             0.3.5
six                   1.11.0
sortedcontainers      2.0.4
sqlite-bro            0.8.11
tables                3.6.1
tensorboard           1.9.0
tensorflow            1.9.0
termcolor             1.1.0
terminado             0.8.3
testpath              0.4.4
Theano                1.0.2
toolz                 0.9.0
tornado               6.0.4
tqdm                  4.28.1
traitlets             4.3.3
urllib3               1.23
wcwidth               0.1.7
Werkzeug              0.14.1
wheel                 0.31.0
winpython             1.10.20180404
zipp                  3.1.0
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
</h5>

Go to DataSets  directory: cd db/
Go to Code (for example Doc2Vec) directory: cd embedding/fix/doc2vec/
To start the training run:
$ python doc2vec_ttc.ipynb

<p align="left"> <img src="https://komarev.com/ghpvc/?username=eminborandag&label=Profile%20views&color=0e75b6&style=flat" alt="eminborandag" /> </p>

- 📫 How to reach me **emin.borandag@cbu.edu.tr**

<h3 align="left">Connect with me:</h3>
<p align="left">
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://d3js.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/d3js/d3js-original.svg" alt="d3js" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a> <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a> <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40"/> </a> </p>




