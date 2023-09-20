#!/bin/bash

# Обновить список пакетов (если требуется)
sudo apt-get update

#Установить pip
python3 -m ensurepip --default-pip

# Установить Python-зависимости с помощью pip
pip install requests bs4

# Вывести сообщение об успешной установке
echo "Установка зависимостей завершена."