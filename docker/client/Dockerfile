# docker/client/Dockerfile (dev)
FROM node:20-alpine

WORKDIR /app

# Копируем package*.json для кэширования слоёв
COPY client/package*.json ./ 

# Устанавливаем зависимости
RUN yarn install --frozen-lockfile --network-timeout 100000

# Копируем (в dev мы всё равно монтируем ./client)
COPY client/ /app/

EXPOSE 5173

CMD ["yarn", "dev", "--host", "0.0.0.0"]
