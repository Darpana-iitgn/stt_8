FROM docker.elastic.co/elasticsearch/elasticsearch:7.17.10

ENV discovery.type=single-node \
    ES_JAVA_OPTS="-Xms512m -Xmx512m" \
    bootstrap.memory_lock=true \
    xpack.security.enabled=false

COPY init-elasticsearch.py .

HEALTHCHECK --interval=10s --timeout=30s --retries=12 \
  CMD curl --fail http://localhost:9200/_cluster/health || exit 1

CMD ["bash", "-c", "elasticsearch & while ! curl -s --fail http://localhost:9200; do sleep 5; done && python init-elasticsearch.py"]