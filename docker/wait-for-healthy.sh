#!/usr/bin/env bash

IMAGE=${CI_REGISTRY_IMAGE}:${CI_PIPELINE_IID}
echo "Wait for image ${IMAGE} to be healthy..."

for i in $(seq 60); do
  count=$(docker ps -f 'status=running' -f 'health=healthy' -f 'name=hanusovedni_web' --format '{{.Image}}' | grep -c "${IMAGE}")
  if [ "${count}" -gt 1 ]; then
    echo "Container is healthy after ${i} seconds."
    exit 0
  fi
  sleep 1
done
if [ "${count}" -lt 2 ]; then
  echo "Timeout exceeded. Count: ${count}"
  exit 1
fi
