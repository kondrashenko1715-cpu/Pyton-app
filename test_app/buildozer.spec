[app]
title = Minecraft Mobile
package.name = minecraftmobile
# ИСПРАВЛЕНИЕ: изменили тестовый org.test на уникальное имя, чтобы сборщик пропустил проект
package.domain = org.kondrashenko

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3, pygame

orientation = landscape
fullscreen = 1

android.api = 33
android.build_tools = 34.0.0

android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
