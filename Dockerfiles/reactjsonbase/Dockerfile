ARG BASE_IMAGE=node:17.2.0-bullseye
ARG RUN_IMAGE=nginx:1.21.4

FROM $BASE_IMAGE as build
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY react-time-ui/package.json ./
COPY react-time-ui/package-lock.json ./
RUN npm ci --silent
RUN npm install react-scripts@3.4.1 -g --silent
COPY react-time-ui ./
RUN npm run build

# production environment
FROM $RUN_IMAGE
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]