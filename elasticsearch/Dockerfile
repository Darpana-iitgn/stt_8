FROM elasticsearch:7.17.0

RUN groupadd -r elasticsearch || true && useradd -r -g elasticsearch elasticsearch_user || true

USER elasticsearch_user

ENV discovery.type=single-node \
    ES_JAVA_OPTS="-Xms512m -Xmx512m"

COPY init-elasticsearch.py .
CMD ["bash", "-c", "elasticsearch & while ! curl -s http://localhost:9200; do sleep 5; done && python init-elasticsearch.py"]