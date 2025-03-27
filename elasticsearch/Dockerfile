FROM docker.elastic.co/elasticsearch/elasticsearch:7.17.10

# Set environment variables to disable extra bootstrap checks and security
ENV discovery.type=single-node \
    ES_JAVA_OPTS="-Xms512m -Xmx512m" \
    bootstrap.memory_lock=true \
    xpack.security.enabled=false

# Copy initialization and entrypoint scripts
COPY init-elasticsearch.py /init-elasticsearch.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 9200 9300

# Healthcheck: wait until cluster health is at least yellow
HEALTHCHECK --interval=10s --timeout=10s --start-period=30s --retries=12 \
  CMD curl -s "http://localhost:9200/_cluster/health?wait_for_status=yellow&timeout=10s" > /dev/null || exit 1

ENTRYPOINT ["/entrypoint.sh"]