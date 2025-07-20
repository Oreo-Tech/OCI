

Command to run
```
oci ce node-pool create \
--cluster-id ocid1.cluster.--4cq \
--name ubuntuone-nodepool \
--node-image-id ocid1.image.oc1.--f2a \
--compartment-id ocid1.compartment.oc1..--xtwhq \
--kubernetes-version v1.33.1 \
--node-shape VM.Standard2.1 \
--placement-configs '[{"availabilityDomain":"<code>:US-ASHBURN-AD-1", "subnetId":"ocid1.subnet.--q"}]' \
--size 1 \
--region us-ashburn-1 \
--pod-subnet-ids '["ocid1.subnet.oc1.iad.--7iq"]' \
--node-metadata '{"user_data": "'$(cat cloud-init.yaml |  base64 -w 0)'"}'