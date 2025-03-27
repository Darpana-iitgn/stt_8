FROM elasticsearch:7.17.0

ENV discovery.type=single-node \
    ES_JAVA_OPTS="-Xms512m -Xmx512m" \
    xpack.security.enabled=false

# Create data directory and set permissions
RUN mkdir -p /usr/share/elasticsearch/data && \
    chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/data

USER elasticsearch

COPY init-elasticsearch.py .
CMD ["bash", "-c", "elasticsearch & while ! curl -s http://localhost:9200; do sleep 5; done && python init-elasticsearch.py"]