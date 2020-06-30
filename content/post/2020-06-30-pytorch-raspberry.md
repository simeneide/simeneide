+++
date = 2020-06-30
title = "Installing Pytorch on a raspberry pi 4"
active = true
tags = ["foo"]
+++

Earlier this year I had to install pytorch on a raspiberry pi for my robotic lawn mower project (more on that later). However, the process was _very_ painful, so Ill throw my notes here in case anyone else tries to do the same. Its not supposed to be bullet-proof, but may help with some pointers. Updates to this proceudre may be found [here](https://github.com/simeneide/gardengoat#torch-and-torchvision).

Installed from wheel on these:
https://github.com/nmilosev/pytorch-arm-builds

But for rpi4 there was some errors, so I installed a wheel after reading this comment:
https://github.com/nmilosev/pytorch-arm-builds/issues/4#issuecomment-527433112

Install from his wheel a bit longer down the thread, and rename those _C.**.so and _d.**.so files to _C.so and _d.so.

Torchvision works, but Pillow 7.0.0 was too new, so downgraded to 6.1 after some random comments I found.


## Step-by-step:

### PIP install pytorch from wheel
Download wheel from here `https://github.com/nmilosev/pytorch-arm-builds` and run `sudo pip3 install torch-1.1.0-cp37-cp37m-linux_armv7l.whl`

### Rename some files
Then if you try to run `sudo python3 -c "import torch"` you get:

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/usr/local/lib/python3.7/dist-packages/torch/__init__.py", line 79, in <module>
    from torch._C import *
ModuleNotFoundError: No module named 'torch._C'
```
Can be fixed by the following:
```
cd /usr/local/lib/python3.7/dist-packages/torch
sudo mv _C.cpython-37m-arm-linux-gnueabi.so _C.so
sudo mv _dl.cpython-37m-arm-linux-gnueabi.so _dl.so
```