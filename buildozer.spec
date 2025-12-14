[app]
title = GameMod
package.name = gamemod
package.domain = org.gamemod
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas
source.exclude_exts = spec,yml
source.exclude_dirs = .git,__pycache__,bin,.buildozer
source.include_patterns = assets/*,icon.png
icon.filename = icon.png
requirements = python3,kivy,plyer,python-dateutil
orientation = portrait
fullscreen = 0
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.sdk = 24
android.ndk = 25b
android.api = 33
android.ndk_api = 21
android.sdk_path = 
android.ndk_path = 
android.tools_path = 
android.build_tools_version = 33.0.2
android.enable_androidx = True
android.gradle_dependencies = 
ios.deployment_target = 
ios.sdk = 
ios.codesign.allowed = False
[buildozer]
log_level = 2
warn_on_root = 1
[android]
arch = armeabi-v7a,arm64-v8a
[ios]
arch = arm64