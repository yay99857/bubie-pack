#!/usr/bin/env bash
# Bubie Pack server — NeoForge 21.1.265, Minecraft 1.21.1, Java 21
set -e
cd "$(dirname "$0")"
NEO=21.1.265
if [ ! -f "libraries/net/neoforged/neoforge/$NEO/unix_args.txt" ]; then
  echo "Instalando NeoForge $NEO / Installing NeoForge $NEO..."
  curl -fL -o neoforge-installer.jar "https://maven.neoforged.net/releases/net/neoforged/neoforge/$NEO/neoforge-$NEO-installer.jar"
  java -jar neoforge-installer.jar --installServer
  rm -f neoforge-installer.jar neoforge-installer.jar.log run.sh run.bat
fi
exec java @user_jvm_args.txt @libraries/net/neoforged/neoforge/$NEO/unix_args.txt nogui "$@"
