[app]
title = Minecraft Mobile
package.name = minecraftmobile
package.domain = org.kondrashenko
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ВАЖНО: строго английские буквы, добавлен pyjnius
requirements = python3==3.10.12, pygame==2.5.2, pyjnius

android.bootstrap = sdl2
orientation = landscape
fullscreen = 1

android.api = 33
android.build_tools = 34.0.0
android.ndk = 25b
android.ndk_version = 25b
android.ndk_api = 21

android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
