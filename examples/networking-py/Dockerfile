# Networking Python example on Hyperlight
#
# Extends the Python base runtime with networking test scripts
# and DNS configuration.

ARG BASE=ghcr.io/hyperlight-dev/hyperlight-unikraft/python-base:latest
FROM ${BASE} AS rootfs
COPY http_get.py /http_get.py
COPY echo_server.py /echo_server.py

# DNS configuration for glibc's getaddrinfo
RUN mkdir -p /etc && \
    echo "nameserver 8.8.8.8" > /etc/resolv.conf && \
    echo "nameserver 8.8.4.4" >> /etc/resolv.conf && \
    echo "hosts: files dns" > /etc/nsswitch.conf && \
    echo "127.0.0.1 localhost" > /etc/hosts

# --- CPIO rootfs builder ---
FROM alpine:3.20 AS cpio
RUN apk add --no-cache cpio findutils
COPY --from=rootfs / /rootfs/
RUN cd /rootfs && find . | cpio -o -H newc > /output.cpio 2>/dev/null
