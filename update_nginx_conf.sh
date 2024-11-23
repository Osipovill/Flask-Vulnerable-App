#!/bin/bash

# Определяем внешний IP, связанный с интерфейсом, имеющим маршрут по умолчанию
EXTERNAL_IP=$(ip route get 1.1.1.1 | awk '{print $7}' | head -n 1)

# Проверяем, удалось ли получить IP
if [ -z "$EXTERNAL_IP" ]; then
    echo "Не удалось определить внешний IP. Проверьте сетевые настройки."
    exit 1
fi

# Обновляем конфигурацию nginx.conf
sed "s/{{EXTERNAL_IP}}/$EXTERNAL_IP/g" /etc/nginx/nginx.conf.template > /etc/nginx/conf.d/default.conf

echo "Nginx конфигурация обновлена с внешним IP: $EXTERNAL_IP"
