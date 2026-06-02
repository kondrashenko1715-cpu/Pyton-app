[app]
title = Minecraft Mobile
package.name = minecraftmobile
package.domain = org.kondrashenko
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Фикс: убираем жесткие версии библиотек, которые могли вызвать конфликт рецептов
requirements = python3, pygame, pyjnius

android.bootstrap = sdl2
orientation = landscape
fullscreen = 1

# Фикс: меняем версию NDK на полностью стабильную r25b (без дублирования строк)
android.api = 33
android.build_tools = 34.0.0
android.ndk_path = 
android.ndk = 25b
android.ndk_api = 21

android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
