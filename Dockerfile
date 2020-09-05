FROM python:3.8-alpine
LABEL Auther=rccqa@rccchina.com

WORKDIR /rcc
VOLUME /rcc/rcc_app_api
COPY requirements.txt /rcc/requirements.txt
COPY entry-point.sh /usr/bin/entrypoint

RUN set -e \
    && sed -i "s#http://dl-cdn.alpinelinux.org#https://mirrors.aliyun.com#g" /etc/apk/repositories \
    && apk update \
    && apk add --no-cache build-base gcc musl-dev libffi-dev openssl-dev jpeg-dev libxml2-dev libxslt-dev postgresql-dev python3-dev \
    && pip install --no-cache -U -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt \
    && pip install qav5 -i http://pypi.rccchina.com/simple/ --extra-index-url https://mirrors.aliyun.com/pypi/simple/ --trusted-host pypi.rccchina.com --trusted-host mirrors.aliyun.com \
    && rm -rf /var/cache/apk/* \
    && TZ="Asia/Shanghai" \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime

ENV HULK_LOG_DIR=/rcc/log
ENV HULK_LOG_NAME=stdout.log

ENTRYPOINT ["entrypoint"]
CMD ["--junit-xml=/rcc/rcc_app_api/report.xml", "--color=yes", "--env=dev", "-reportportal"]
