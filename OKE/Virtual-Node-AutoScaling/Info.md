Install metrics service on cluster - Virtual nodes

`kubectl apply -f https://raw.githubusercontent.com/oracle-devrel/oci-oke-virtual-nodes/main/metrics-server/components.yml`

Ref: https://github.com/oracle-devrel/oci-oke-virtual-nodes/blob/main/metrics-server/README.md


Create HPA for the Deployment

`kubectl autoscale deployment my-nginx --cpu-percent=20 --min=1 --max=100`

Monitor HPA 

`kubectl get hpa -w`

You can test the load on the application using apache benchmark tool
example:

` ab -n 100000 -c 100 http://<loadbalancer-IP>/ `
