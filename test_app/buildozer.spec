[app]
title = Minecraft Mobile
package.name = minecraftmobile
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ВАЖНО: используем чистый pygame и бэкенд sdl2
requirements = python3, pygame
android.bootstrap = sdl2

orientation = landscape
fullscreen = 1

# ФИКСИРУЕМ ВЕРСИИ ДЛЯ СТАБИЛЬНОСТИ
android.api = 33
android.ndk = 25b
android.ndk_api = 21

# Собираем под arm64-v8a
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
