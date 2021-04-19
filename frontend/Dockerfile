# build stage
FROM node:14.15.1-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN yarn
COPY ./ .
RUN npm run build

# Production stage
FROM nginx:1.16.1-alpine as production-stage
RUN mkdir /app
COPY --from=build-stage /app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD [ "nginx", "-g", "daemon off;"]