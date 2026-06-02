[app]
title = Minecraft Mobile
package.name = minecraftmobile
package.domain = org.kondrashenko
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Чистый набор требований для стабильного подбора версий
requirements = python3, pygame, pyjnius

android.bootstrap = sdl2
orientation = landscape
fullscreen = 1

# Позволяем Buildozer самому скачать нужный и совместимый NDK r25b
android.api = 33
android.build_tools = 34.0.0
android.ndk_api = 21

android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
