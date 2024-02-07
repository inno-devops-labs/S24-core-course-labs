#[cfg(test)]
mod test;

#[macro_use]
extern crate rocket;

use rocket::{Build, Rocket};
use rocket::request::Request;


#[get("/<number_1>/<number_2>")]
fn plus(number_1: i32, number_2: i32) -> String {
    return format!("Plus operation: {} + {} = {}", number_1, number_2, number_1 + number_2);
}

#[get("/<number_1>/<number_2>")]
fn minus(number_1: i32, number_2: i32) -> String {
    return format!("Minus operation: {} - {} = {}", number_1, number_2, number_1 - number_2);
}

#[get("/<number_1>/<number_2>")]
fn multiply(number_1: i32, number_2: i32) -> String {
    return format!("Multiplication operation: {} * {} = {}", number_1, number_2, number_1 * number_2);
}

#[get("/<number_1>/<number_2>")]
fn divide(number_1: i32, number_2: i32) -> String {
    return if number_2 != 0 {
        format!("Division operation: {} / {} = {}", number_1, number_2, number_1 / number_2)
    } else {
        format!("Error: Division by Zero - {} / {}", number_1, number_2)
    };
}

#[catch(404)]
fn not_found() -> String {
    format!("Sorry, not found")
}

#[catch(default)]
fn default_catcher(status: rocket::http::Status, _request: &Request) -> String {
    format!("ERROR: {} - {:?}", status.code, status.reason())
}

#[launch]
fn rocket_build() -> Rocket<Build> {
    rocket::build().mount("/plus", routes![plus])
        .mount("/minus", routes![minus])
        .mount("/multiply", routes![multiply])
        .mount("/divide", routes![divide])
        .register("/", catchers![not_found, default_catcher])
}

// Code based on this tutorial: https://www.shuttle.rs/blog/2023/12/13/using-rocket-rust