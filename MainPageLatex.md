# Main Page
### Introduction
This is a C++ renderer using the Path Tracing algorithm I made throughout 2020 in the context of my *Travail de Maturité*. You can find at the following URL:

[https://github.com/JoachimFavre/PathTracer](https://github.com/JoachimFavre/PathTracer)


If you want to have the code behind this documentation, you can find it at the following URL:

[https://github.com/JoachimFavre/PathTracerDocumentation](https://github.com/JoachimFavre/PathTracerDocumentation)

Finally, you can find a web documentation at the following URL:

[https://joachimfavre.github.io/PathTracerDocumentation/](https://joachimfavre.github.io/PathTracerDocumentation/)


### Dependencies
- FBX SDK version 2020.1 by Autodesk
  - Download (use Runtime Library Option "MT"):

  [https://www.autodesk.com/developer-network/platform-technologies/fbx-sdk-2020-1](https://www.autodesk.com/developer-network/platform-technologies/fbx-sdk-2020-1)

  - Documentation:

  [https://help.autodesk.com/view/FBX/2020/ENU/](https://help.autodesk.com/view/FBX/2020/ENU/)


- JSON for Modern C++ version 3.9.1 by nlohmann
  - GitHub (I used examples from README.md):

  [https://github.com/nlohmann/json](https://github.com/nlohmann/json)

  - Download (using include.zip/single_include):

  [https://github.com/nlohmann/json/releases/tag/v3.9.1](https://github.com/nlohmann/json/releases/tag/v3.9.1)

  - Documentation:

  [https://nlohmann.github.io/json/](https://nlohmann.github.io/json/)


- The CImg Library version 2.9.2 by David Tschumperlé
  - Website:

  [http://cimg.eu/](http://cimg.eu/)

  - Download (put CImg.h in [your project directory]/CImg):

  [http://cimg.eu/download.html](http://cimg.eu/download.html)

  - List of supported picture format:

  [http://cimg.eu/reference/group__cimg__files__io.html](http://cimg.eu/reference/group__cimg__files__io.html)



### Visual Studio 2017 parametring
- Make sure to follow the FBX SDK configuration tutorial (using Runtime Library Option "MT"):

  [https://help.autodesk.com/view/FBX/2020/ENU/?guid=FBX_Developer_Help_getting_started_installing_and_configuring_configuring_the_fbx_sdk_for_wind_html](https://help.autodesk.com/view/FBX/2020/ENU/?guid=FBX_Developer_Help_getting_started_installing_and_configuring_configuring_the_fbx_sdk_for_wind_html)
- Assert that "Project Properties > C/C++ > Language > Open MP Support" is yes (else multithreading will not work).
- NB: I could not use a Visual Studio 2019 because the FBX SDK library is not available (or, at least, was not on the 10th January 2021) for this version.  


### Fbx file export from Blender
To export a FBX file from Blender ([https://www.blender.org/](https://www.blender.org/)), make sure to configure:
- Scale: 0.01
- Forward: -Z Forward
- Up: Y up
