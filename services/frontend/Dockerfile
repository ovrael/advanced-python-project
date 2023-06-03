FROM node:lts-alpine

WORKDIR /app

EXPOSE 20222
EXPOSE 30222

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@5.0.8 -g

COPY package.json .
COPY package-lock.json .
RUN npm install