[app]
title = Minecraft Mobile
package.name = minecraftmobile
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ИСПРАВЛЕНИЕ: Добавлен обязательный pygame_bootstrap
requirements = python3, pygame, pygame_bootstrap

orientation = landscape
fullscreen = 1

# ОПТИМИЗАЦИЯ: Оставляем только arm64-v8a для GitHub. 
# Сборка под две архитектуры на бесплатных серверах часто падает по памяти!
android.archs = arm64-v8a
android.allow_backup = True

# Дополнительные настройки для стабильности в облаке
android.accept_sdk_license = True
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 1
