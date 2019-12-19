# pyappiumtest

## Python Appium sample script on Android device

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
## Sample script on Windows PC
Download and install Windows App Driver (https://github.com/Microsoft/WinAppDriver)

Now run appium, like
```batch
appium
```
Note that Appium should have Windows Application Driver as part of the installation. Otherwise install manually.

Now run the actual script, like:
```batch
python testcalc.py
```

References:  
[Automatic Discovery of Chrome Driver](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/web/chromedriver.md#automatic-discovery-of-compatible-chromedriver)  
[Mostly copied from Appium sampmles](https://github.com/microsoft/WinAppDriver/tree/master/Samples/Python)
