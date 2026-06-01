[app]
title = Minecraft Mobile
package.name = minecraftmobile
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ТО САМОЕ ИСПРАВЛЕНИЕ: сохраняем готовый файл в корень проекта, чтобы GitHub его не потерял
bin_dir = .

requirements = python3, pygame

orientation = landscape
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
