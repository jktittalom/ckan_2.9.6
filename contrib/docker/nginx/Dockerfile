FROM nginx:stable-alpine

ENV NGINX_DIR=/etc/nginx

COPY setup/nginx.conf ${NGINX_DIR}/nginx.conf
COPY setup/index.html /usr/share/nginx/html/index.html
COPY setup/default.conf ${NGINX_DIR}/conf.d/
COPY setup/node.conf ${NGINX_DIR}/conf.d/
COPY setup/ckan.conf ${NGINX_DIR}/conf.d/

RUN mkdir -p ${NGINX_DIR}/certs
COPY setup/ckan-local.* ${NGINX_DIR}/certs/
COPY setup/node-local.* ${NGINX_DIR}/certs/

EXPOSE 81