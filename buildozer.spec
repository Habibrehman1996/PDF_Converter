[app]
title = Image to PDF Converter
package.name = imagetopdf
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.0.0,kivymd==0.104.1,pillow==8.4.0,img2pdf==0.4.4,plyer==1.4.3
android.api = 30
android.minapi = 21
android.ndk_version = 21b
# Simplified SDK packages
android.sdkmanager_additional_packages = build-tools;30.0.3,platforms;android-30,ndk;21b
android.gradle_packages = com.android.tools.build:gradle:4.1.0
android.timeout_build = 10000
android.arch = armeabi-v7a,arm64-v8a,x86,x86_64
android.num_cores = 4

[android]
permissions = INTERNET
