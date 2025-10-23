1 [app]
2 title = MyKivyApp
3 package.name = mykivyapp
4 package.domain = com.varunesh
5 source.dir = .
6 version = 0.1
7 requirements = python3,kivy,sqlite3
8 orientation = portrait
9 fullscreen = 0
10 # Android settings (ये भी इसी [app] में रखें)
11 android.api = 31
12 android.ndk = 25b
13 android.minapi = 21
14 android.archs = arm64-v8a,armeabi-v7a
15
16 [buildozer]
17 log_level = 2
18 warn_on_root = 1
