# LEARNING APPLICATION
![CI](https://github.com/Ejedavy/S24-core-course-labs/actions/workflows/ci.yaml/badge.svg)
![Test](https://github.com/Ejedavy/S24-core-course-labs/actions/workflows/test.yaml/badge.svg)


This is a learning app that helps students learn school materials using AI.

<!-- Badges -->


![LEARNING APPLICATION](https://www.managedoutsource.com/wp-content/uploads/2023/06/artificial-intelligence-is-transforming-the-education-industry.jpg)

## Description

This has features that enables students create subjects and upload materials and use these materials to prepare for exams and study.

### Features

- Creating Subjects
- Uploading materials to train your personal study assistant
- Authentication

## Getting Started

### Installing

Clone the repository and build the project:

```bash
# Clone the repository
git clone https://github.com/Ejedavy/S24-core-course-labs.git

# Navigate to the project directory
cd S24-core-course-labs && cd app_learning


# Build the project
cargo build
```

## Executing program

Run the requirements for the application with:
```bash
bash ./script/init_db.sh

docker compose up
```

Run the program with:

```bash
cargo run
```

[![Local Host Application](https://i.postimg.cc/3N7xYPhg/image.png)](https://postimg.cc/k61myYB4)

Run tests with:

```bash
cargo test
```

## Contributing

Contributions to this service are welcome!

To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Authors

- David Eje(https://github.com/ejedavy)

