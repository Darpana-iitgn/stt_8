FROM docker.elastic.co/elasticsearch/elasticsearch:7.17.10

# Switch to root to install python3 and adjust files, then revert to elasticsearch user.
USER root
RUN apt-get update && apt-get install -y python3 && rm -rf /var/lib/apt/lists/*

# Copy the initialization and entrypoint scripts
COPY init-elasticsearch.py /init-elasticsearch.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set environment variables for single-node mode and disable security
ENV discovery.type=single-node \
    ES_JAVA_OPTS="-Xms512m -Xmx512m" \
    bootstrap.memory_lock=true \
    xpack.security.enabled=false

# (Optional) Copy custom config if needed:
# COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

EXPOSE 9200 9300

# Healthcheck: wait until cluster health is at least yellow
HEALTHCHECK --interval=10s --timeout=10s --start-period=30s --retries=12 \
  CMD curl -s "http://localhost:9200/_cluster/health?wait_for_status=yellow&timeout=10s" > /dev/null || exit 1

# Switch back to the default user
USER elasticsearch

ENTRYPOINT ["/entrypoint.sh"]