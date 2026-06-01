[app]
title = Minecraft Mobile
package.name = minecraftmobile
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ВАЖНО: Только python3 и чистый pygame. Современный Buildozer сам выберет нужный bootstrap
requirements = python3, pygame

orientation = landscape
fullscreen = 1

# Собираем под arm64-v8a — это стандарт для 99% современных телефонов
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
