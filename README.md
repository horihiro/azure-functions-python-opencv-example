# azure-functions-python-opencv-example
This is **unofficial** sample project of Azure Functions for python with OpenCV

  1. Install and run docker daemon
  1. Clone this repository and open this by VScode with Azure Functions extension.
  1. Edit `HttpTrigger/__init__.py` if you want
  1. Deploy to your Function App (Linux and Consumption plan) using Azure Functions extensions.<br>
     This step includes the process which downloads the libraies to `./lib`

The http trigger function can comvert image, which is specified by `image_url` query parameter, to grayscale image using `cv2.imread`, `cv2.cvtColor` and `cv2.imwrite`

|Input|Output|
| - | -|
|![](https://user-images.githubusercontent.com/4566555/66614178-ed7d1c80-ec02-11e9-8b22-4560309db118.png)|![](https://user-images.githubusercontent.com/4566555/66614160-dccca680-ec02-11e9-8946-4db70d5d861a.png)|
