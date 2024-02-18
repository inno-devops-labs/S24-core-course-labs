# CI best practices 
* the pipeline is split into modular blocks: 
  * code quality check 
  * security check 
  * docker image build and push 
* cache is utilized for optimization 
* blocks depend on each other, so the docker image is not built before necessary quality and security
 requirements are satisfied 