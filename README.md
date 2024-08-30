# streamlit-imagegrid
Streamlit plugin for visualizing images in a pretty grid.


Streamlit native image display does not provide a good UI experiences and misses some crucial features when creating grid of images.

The `streamlit-imagegrid` plugin for provides a way to generate a reactive grid of images or videos.


In the latest update we provide support for interleaved image and video as well as support for metadata visualization.

Sample usage

```python
import streamlit_imagegrid
import streamlit as st

urls = ['http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4',
        'https://images.freeimages.com/images/large-previews/56d/peacock-1169961.jpg',
        'https://images.freeimages.com/images/large-previews/bc4/curious-bird-1-1374322.jpg',
        'https://images.freeimages.com/images/large-previews/9f9/selfridges-2-1470748.jpg',
        'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'] * 2

selected = streamlit_imagegrid.streamlit_imagegrid("visualization1",urls,4,key='foo')

st.write(selected)

```
Note that `urls` can accept interleaved images and video files. Most popular formats are supported and plugin identifies the type by the extensions. Caching and performance optimizations are still TBD and loading many videos might produce lag. Please report any issues you see to midhun1234@gmail.com .

Plugin accepts metadata as long as it respects the following format.

```json
{
    "src":"http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
    "metadata":{}
    "tags":{}
}

The `src` key is required to identify the asset url. Other fields will be joined together to form the tag feild and displayed under the asset after its rendered. The plugin can also take as part of urls mixed dict and strings. e.g

```python

urls = [{'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4','tag':'a video'},
        'https://images.freeimages.com/images/large-previews/56d/peacock-1169961.jpg',
        'https://images.freeimages.com/images/large-previews/bc4/curious-bird-1-1374322.jpg',
        'https://images.freeimages.com/images/large-previews/9f9/selfridges-2-1470748.jpg',
        'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4']

```
The grid is interactive. When an asset is clicked in the grid view, the plugin returns the value from url that was passed to the plugin. This is helpfull for selection of assets from a large set of results to perform downstream processing.