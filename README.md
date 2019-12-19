# pyappiumtest
Python Appium sample script

```batch
conda create --prefix c:\y\envs\appiumenv conda pip
conda activate c:\y\envs\appiumenv
pip install Appium-Python-Client
```
Install Appium (this application will be webdriver proxy to Chrome driver on Android)
```batch
npm install -g appium
```
Note that I am assuming that Node.js is installe on the machine

To run the test do:
```batch
appium --allow-insecure chromedriver_autodownload
```
The above command runs appium proxy. Now run the actual test, like:
```batch
python testandroidchrome.py
```