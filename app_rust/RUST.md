### Framework choose

I have never used Rust as web-app dev tool, so have choose `actix-web` based on opinion among forums, framework documentation, community and the maintenance by authors. The description on official site says that Actix Web is *"a powerful and pragmatic framework"*. I really hope that I have made a good choice for the first time.

### *What does this web app do?*
Since I'm not well experienced with Rust web development, I would learn as much framework base "tricks" as I can.
For this time it would be counter of requests (upon page access or its refreshing).

### Code style + best practices

I think it's hard to write a bad quality code on Rust :) This programming language is so strict with its rules. 

I have used extensions in IDE to analyze my code, they are also show some hints.

I'm really don't know all keys best practices in Rust dev process, but I would use common accross different languages: separated logic, understandable variables names + SOLID principles.

All code placed in `app/src` folder.

### Testing

There are exist two simple integration tests described in `app/src/tests.rs`: on success http request + on correct counter number.
