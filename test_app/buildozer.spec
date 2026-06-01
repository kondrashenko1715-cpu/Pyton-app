[app]
title = Minecraft Mobile
package.name = minecraftmobile
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ВАЖНО: Указали стабильную версию pygame и обязательный pygame_bootstrap
requirements = python3, pygame==2.5.2, pygame_bootstrap

orientation = landscape
fullscreen = 1

# Собираем только под современные 64-битные процессоры телефонов. 
# Это экономит память сервера GitHub и защищает от падений по тайм-ауту.
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
