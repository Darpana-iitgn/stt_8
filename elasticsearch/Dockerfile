FROM elasticsearch:7.17.0

# Create a non-root user and switch to it
RUN groupadd -r elasticsearch && useradd -r -g elasticsearch elasticsearch_user
USER elasticsearch_user

ENV discovery.type=single-node \
    ES_JAVA_OPTS="-Xms512m -Xmx512m"

COPY init-elasticsearch.py .
CMD ["bash", "-c", "elasticsearch & while ! curl -s http://localhost:9200; do sleep 5; done && python init-elasticsearch.py"]