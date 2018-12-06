This is a research project where I'm studying the injectiveness of random functions. Random as in f: D -> C where
f(x) = rand(x). Right now I'm essentially looking at two things -- how does the probability that a random function
is injective change as the domain and codomain both get arbitrarily large while maintaining a fixed ratio
r = size(codomain)/size(domain), and how does the probability change as the codomain gets large but the domain
remains fixed in size. 

The algortithm for determining if a function is injective resides in checkInjective.cpp. build.sh (tested on MacOS
and Fedora Workstation 29) will build a shared library under pwd/lib/$OSTYPE/. pyInjective.py is an API
to that shared object. analysisLib.py contains functions for actually anaylyzing things and making predictions.
analysis_driver.py is where tests are actually run. Eventually, data from the project will reside in a folder
called results/.

To run the project in whatever it's current config is, just clone the repo, run build.sh, install matplotlib,
and then run the driver.

Requirements:
python 3.6 (minimum version tested)
matplotlib
g++11 or higher

