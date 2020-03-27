FROM node:13.7.0 as builder
MAINTAINER Benning

WORKDIR /frontend
COPY ./package.json .index
RUN npm install
COPY . .
RUN npm install
RUN npm run build

FROM nginx
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /frontend/dist /usr/share/nginx/html