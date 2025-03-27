FROM docker.elastic.co/elasticsearch/elasticsearch:7.17.10

# Switch to root to install python3 and adjust file permissions
USER root
RUN apt-get update && apt-get install -y python3 && rm -rf /var/lib/apt/lists/*

# Copy initialization and entrypoint scripts
COPY init-elasticsearch.py /init-elasticsearch.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set environment variables for single-node mode and disable security features
ENV discovery.type=single-node \
    ES_JAVA_OPTS="-Xms512m -Xmx512m" \
    bootstrap.memory_lock=true \
    xpack.security.enabled=false

EXPOSE 9200 9300

# Healthcheck: Wait until the cluster health is at least yellow
HEALTHCHECK --interval=10s --timeout=10s --start-period=30s --retries=12 \
  CMD curl -s "http://localhost:9200/_cluster/health?wait_for_status=yellow&timeout=10s" > /dev/null || exit 1

# Switch back to default elasticsearch user
USER elasticsearch

ENTRYPOINT ["/entrypoint.sh"]