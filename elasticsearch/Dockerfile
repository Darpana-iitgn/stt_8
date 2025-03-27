FROM elasticsearch:7.17.0

ENV discovery.type=single-node \
    ES_JAVA_OPTS="-Xms512m -Xmx512m"

COPY init-elasticsearch.py .
RUN elasticsearch-plugin install analysis-icu

VOLUME /usr/share/elasticsearch/data

CMD ["bash", "-c", "elasticsearch & while ! curl -s http://localhost:9200; do sleep 5; done && python init-elasticsearch.py"]