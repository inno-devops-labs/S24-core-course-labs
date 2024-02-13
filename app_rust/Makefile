run:
	. start.sh

test:
	cd app; cargo test

docker-run:
	docker run -p 8000:8000 --rm -ti devops-lab-02-rust

docker-build:
	docker build . -t devops-lab-02-rust

docker-pull:
	docker pull adarika/devops-lab-02-rust

docker-pull-run: docker-pull
	docker run -p 8000:8000 --rm -ti adarika/devops-lab-02-rust

docker-push:
	docker tag devops-lab-02-rust  adarika/devops-lab-02-rust
	docker push adarika/devops-lab-02-rust