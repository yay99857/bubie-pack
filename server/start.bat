@echo off
rem Bubie Pack server - NeoForge 21.1.265, Minecraft 1.21.1, Java 21
cd /d "%~dp0"
set NEO=21.1.265
if not exist "libraries\net\neoforged\neoforge\%NEO%\win_args.txt" (
  echo Instalando NeoForge %NEO% / Installing NeoForge %NEO%...
  curl -fL -o neoforge-installer.jar "https://maven.neoforged.net/releases/net/neoforged/neoforge/%NEO%/neoforge-%NEO%-installer.jar"
  java -jar neoforge-installer.jar --installServer
  del /q neoforge-installer.jar neoforge-installer.jar.log run.sh run.bat 2>nul
)
rem Distancias para PC modesto, so na primeira vez (nao mexe num server.properties existente).
if not exist server.properties (
  >server.properties echo view-distance=8
  >>server.properties echo simulation-distance=6
)
java @user_jvm_args.txt @libraries/net/neoforged/neoforge/%NEO%/win_args.txt nogui %*
pause
