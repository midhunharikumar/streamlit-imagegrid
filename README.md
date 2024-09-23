# streamlit-imagegrid

![PyPI version](https://img.shields.io/pypi/v/streamlit-imagegrid?color=brightgreen)
![License](https://img.shields.io/github/license/midhunharikumar/streamlit-imagegrid)
![GitHub issues](https://img.shields.io/github/issues/midhunharikumar/streamlit-imagegrid)
![GitHub stars](https://img.shields.io/github/stars/midhunharikumar/streamlit-imagegrid)

<img width="1326" alt="image" src="https://github.com/user-attachments/assets/5225f2ed-ba2d-496d-9f7d-8b512bc13072">


**A powerful Streamlit plugin for visualizing images and videos in a responsive grid layout.**

## Features
- **Interleaved image and video support:** Add images and videos to a single grid.
- **Interactive asset selection:** Clickable assets for downstream processing.
- **Metadata and tag support:** Attach metadata to media assets and display tags.
- **Flexible format support:** Most popular media formats are supported.

---

## Installation

Install the plugin using pip:

```bash
pip install streamlit-imagegrid

```
#### Sample Usage
Here’s a quick example of how to use the streamlit-imagegrid plugin in your app:

```python
import streamlit_imagegrid
import streamlit as st

# List of image and video URLs
urls = [
    'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4',
    'https://images.freeimages.com/images/large-previews/56d/peacock-1169961.jpg',
    'https://images.freeimages.com/images/large-previews/bc4/curious-bird-1-1374322.jpg',
    'https://images.freeimages.com/images/large-previews/9f9/selfridges-2-1470748.jpg',
    'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'
] * 2

# Generate the interactive grid with 4 columns
selected = streamlit_imagegrid.streamlit_imagegrid("visualization1", urls, 4, key='foo')

# Display the selected item
st.write(f"Selected item: {selected}")
```

## Metadata Support
You can also pass metadata and tags alongside the media URLs for better organization and display. Here’s how:

```json
{
    "src": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
    "metadata": {},
    "tags": {"type": "video", "duration": "1m45s"}
}
```

The src key is mandatory for identifying the media, while the metadata and tags can be customized and will be displayed alongside the asset in the grid.

#### Example usage with metadata:

```python
urls = [
    {'src': 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4', 'tags': {'type': 'video', 'duration': '1m45s'}},
    'https://images.freeimages.com/images/large-previews/56d/peacock-1169961.jpg',
    'https://images.freeimages.com/images/large-previews/bc4/curious-bird-1-1374322.jpg',
    'https://images.freeimages.com/images/large-previews/9f9/selfridges-2-1470748.jpg',
    'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'
]
```

The grid is interactive: when you click an asset, it will return the URL of the clicked item, making it ideal for selecting images or videos from large sets for further processing.

## Performance Considerations
Please note that the plugin's performance may be impacted when loading many videos. Caching and optimizations are being worked on. Feel free to report any issues you encounter to midhun1234@gmail.com.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to submit issues or pull requests. For bug reports or feature requests, email us at midhun1234@gmail.com.

## License
streamlit-imagegrid is licensed under the MIT License. See the LICENSE file for more details.
