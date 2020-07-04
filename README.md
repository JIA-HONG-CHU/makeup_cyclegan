# CycleGAN in PyTorch
I use the cyclegan code provided by https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix .It allows users who have never applied makeup before to easily try other people's makeup without spending time learning makeup techniques and money on cosmetics, and then make a reference for their own makeup style.

BTW:I use the Bilinear_interportation+Reflection2d+Conv2d instead of Con2dTranspose in the generator to prevent the checkerboard problem.

## Prerequisites
- Linux or macOS
- Python 3
- CPU or NVIDIA GPU + CUDA CuDNN

## Getting Started
### Installation

```bash
pip install -r requirements.txt
```

### CycleGAN train/test

- To view training results and loss plots, run `python -m visdom.server` and click the URL http://localhost:8097.

- Train a model:

```bash
python train.py --dataroot ./Train_Test_datasets/makeup --name makeup_cyclegan --model cycle_gan
```
To see more intermediate results, check out `./checkpoints/makeup_cyclegan/web/index.html`.

- Test the model:

```bash
python test.py --dataroot ./Train_Test_datasets/makeup --name makeup_cyclegan --model cycle_gan
```
- The test results will be saved to a html file here: `./results/makeup_cyclegan/latest_test/index.html`.

