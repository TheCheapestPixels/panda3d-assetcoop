Game assets for use with panda3d, made by Entikan.

BAMs are to be converted with panda3d-boterham.

Basic usage example:
```python
import assetcoop
from direct.showbase.ShowBase import ShowBase


base = ShowBase()
lona = loader.load_model('models/scenes/lona.bam')
lona.ls()
```

To build all assets.
```
$ pip install panda3d-boterham
$ boterham assetcoop/blender assetcoop/bam
```

License is the Panda3D License.
More general-use assets are very welcome. 