# Image
FROM node:20.19.0-alpine

# Set up work directory
WORKDIR /app

COPY frontend .

ENV HOST 0.0.0.0
EXPOSE 5173
EXPOSE 24678

# Run after container is up
CMD ["yarn", "dev"]