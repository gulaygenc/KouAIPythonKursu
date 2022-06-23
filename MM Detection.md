# MM Detection

## Installation

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

2. First create a Conda environment using:
   ```sh 
    pip install -U openmim
    ```
3. Activate the environment using:
    ```sh
    conda activate env_pytorch
    ```
4. Now install PyTorch:
    
    Using pip:
    ```sh
    pip install tourchvision
    ``` 
    
    On GPU:
    ```sh
    conda install pytorch torchvision -c pytorch
    ``` 
5. Install MMCV using MIM:
    ```sh
    pip install -U openmim
    mim install mmcv-full
    ```
6. Install MMDetection:
    ```sh
    git clone https://github.com/open-mmlab/mmdetection.git
    cd mmdetection
    pip install -v -e .
    ```
    
## Run

1. Download config and checkpoint files:
    ```sh
    mim download mmdet --config yolov3_mobilenetv2_320_300e_coco --dest .
    ```
2. Run py file
 
     ```sh
     python demo/image_demo.py demo/demo.jpg yolov3_mobilenetv2_320_300e_coco.py yolov3_mobilenetv2_320_300e_coco_20210719_215349-d18dff72.pth --device cpu --out-file result.jpg
     ```
    You will see the results in file on result.jpg 