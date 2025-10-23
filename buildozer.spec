[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = com.varunesh
source.dir = .
version = 0.1
requirements = python3,kivy,sqlite3
orientation = portrait
fullscreen = 0

# Android settings
android.api = 31
android.ndk = 25b
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True
android.debug = True

# Optional (logs थोड़े क्लीन रहें)
android.allow_backup = True
android.log_level = 2
android.release_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 0
