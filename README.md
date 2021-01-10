# Path Tracer Documentation
This is the code for the documentation of a Path Tracer I wrote throughout 2020 in the context of my *Travail de Maturité* (see [my repository](https://github.com/JoachimFavre/PathTracer)). The documentation can be found at the following url: https://joachimfavre.github.io/PathTracerDocumentation/.

This documentation was generated using [doxygen](https://www.doxygen.nl/index.html) 1.9.0. The parameters I defined can be found in the following files: DoxyfileHTML, DoxyfileLatex, DoxygenLayout.xml, MainPageHTML.md, MainPageLatex and ExtraStyleSheet.css, footer.html and header.tex.

I also wrote a little python script (not very properly, but it works) that turns doxygen documentation written right before each function into a block of text that can be put at the beginning of the file. See its docstring for further information. This file is named documentationConversion.py.

Note to myself, and to anyone trying to have a GitHub pages from a Doxygen-generated documentation, we have to put a .nojekyll empty file in the source code. I found this solution [here](https://github.blog/2009-12-29-bypassing-jekyll-on-github-pages/).
