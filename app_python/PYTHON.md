# Python web application

> Since I'm currently work as Python Backend Developer (for long time already), I would use all best practices (mostly archuitectural) + use experience-based dev tricks during labs.

### Framework 
A lot of web resources has its own top-10 list with pyton frameworks and usualy `Django` has top-1 place (also it is so popular), but it is so heavy for DevOps labs + complex for understanding.

Actually I have experience with `FastAPI`, `aiohttp` and `Flask`; it is really hard to choose exactly one technology for all labs. I really enjoy learn more about async + ASGI, so `Flask` is not suitable for me now, it's true even for its "brother" `Quart`.

There is hard choose between 2 good and familiar frameworks: `aiohttp` and `FastAPI` - one is more stable and flexible, another is more poplular with good community and docs. A decisive factor is perfomance, so **I have choose `FastAPI` web-framework.**

### Architecture

I'l choose base hexagonal architecture for microservices development. There are some layers: Application (core, buisiness logic), Service, Infrastructure + Adapters and Interface.

This idea provides principles to achieve low effort scale our application code in future and also make changes in one part without risk to "damage" other layers. Moreover, it will be much easier to test it as it allows to mock entire layer entity and integrate it with operational parts of implementation.

### Coding standarts

For following best coding standarts, there are some useful tools: `pylint` - linter + `isort` (linter for imports), `flake8` - utility for enforcing style consistency, `refurb` modernizing Python codebase, `pyright` - static type checker (helps to understand code logic).

Format features (linters + codebase style) can be run via `make format`, and typecheck with `make typecheck` commands.

Also, some of tools also run during pre-commit phase.


### Testing

There are 2 main classes of tests: unit + service. You run all together with `make tests`.


### Develop process

To simplify dev process, all most usefull actions were described in `Makefile`:
- `make init` a base actions for starting dev process; it installs all needed dependecies
- `make run` starts web app
- `make format` will unify code base to avoid diffs across developers
- `make tests` for running tests for the app
