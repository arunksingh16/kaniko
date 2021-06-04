# kaniko
Kaniko Testing and POC

### Create Secret before running Kaniko POD for image build

```
kubectl create secret docker-registry docker --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>

```
