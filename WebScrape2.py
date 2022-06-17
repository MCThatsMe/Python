#! /usr/bin/python
import os
import psutil as psutil
from selenium import webdriver

#Close Chrome
os.system("TASKKILL /F /IM chrome.exe")
print("Closed Chrome!")

#Open chrome
os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
print("Done")

