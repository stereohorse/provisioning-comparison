# Comparison of provisioning tools

Task: deploy distributed app on cluster of 3 Apache Mesos virtual nodes with different tools.

Motivation: understand pros and cons of them.

## Provisioners included

1. Fabric

## Setup

```bash
# install vagrant
$ brew cask install virtualbox
$ brew cask install vagrant

# install vagrant hostmanager
$ vagrant plugin install vagrant-hostmanager
```

## Execution

Provisioners are separated by subdirs.
Generally, work flow is following:

1. Setup 3 clean vagrant machines
2. Run provisoner

Each provisioner will do same steps:

1. Install Oracle JRE 8
2. Install Zookeeper
3. Install Mesos master
4. Install Marathon
5. Install Mesos agents
6. Deploy sample app

Quick info:

Zookeeper is used for distributed coordination.
Mesos master manages cluster resources.
Marathon uses these resources to run apps.
Mesos agents are immediate apps executors & resource manager of each node.

Zookeeper, Mesos master & Marathon are installed in HA mode (on all 3 nodes).
All vms are Mesos agents nodes.

### Endpoints

Machines host names are **vm1**, **vm2** & **vm3**.
They can be accessed by theses names thanks to vagrant hostmanager.

1. Mesos: [http://vm1:5050](http://vm1:5050)
2. Marathon: [http://vm1:8080](http://vm1:8080)

## Next

See readme files in each tool subdir for next steps.

1. [Fabric](https://github.com/stereohorse/provisioning-comparison/tree/master/fabric)
