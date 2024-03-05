use crate::{plus, minus, multiply, divide};

#[test]
fn test_plus() {
    assert_eq!(plus(1, 2), "Plus operation: 1 + 2 = 3");
}

#[test]
fn test_minus() {
    assert_eq!(minus(8, 2), "Minus operation: 8 - 2 = 6");
}

#[test]
fn test_multiply() {
    assert_eq!(multiply(3, 3), "Multiplication operation: 3 * 3 = 9");
}

#[test]
fn test_divide() {
    assert_eq!(divide(10, 2), "Division operation: 10 / 2 = 5");
}

#[test]
fn test_divide_by_zero() {
    assert_eq!(divide(5, 0), "Error: Division by Zero - 5 / 0");
}

#[cfg(test)]
mod test {
    use crate::rocket_build;
    use rocket::local::blocking::Client;
    use rocket::http::Status;

    #[test]
    fn test_plus_response() {
        let client = Client::tracked(rocket_build()).expect("valid rocket instance");
        let response = client.get("/plus/1/2").dispatch();
        assert_eq!(response.status(), Status::Ok);
        assert_eq!(response.into_string().unwrap(), "Plus operation: 1 + 2 = 3");
    }

    #[test]
    fn test_minus_response() {
        let client = Client::tracked(rocket_build()).expect("valid rocket instance");
        let response = client.get("/minus/8/2").dispatch();
        assert_eq!(response.status(), Status::Ok);
        assert_eq!(response.into_string().unwrap(), "Minus operation: 8 - 2 = 6");
    }

    #[test]
    fn test_multiply_response() {
        let client = Client::tracked(rocket_build()).expect("valid rocket instance");
        let response = client.get("/multiply/3/3").dispatch();
        assert_eq!(response.status(), Status::Ok);
        assert_eq!(response.into_string().unwrap(), "Multiplication operation: 3 * 3 = 9");
    }

    #[test]
    fn test_divide_by_zero_response() {
        let client = Client::tracked(rocket_build()).expect("valid rocket instance");
        let response = client.get("/divide/5/0").dispatch();
        assert_eq!(response.status(), Status::Ok);
        assert_eq!(response.into_string().unwrap(), "Error: Division by Zero - 5 / 0");
    }

    #[test]
    fn test_divide_response() {
        let client = Client::tracked(rocket_build()).expect("valid rocket instance");
        let response = client.get("/divide/10/2").dispatch();
        assert_eq!(response.status(), Status::Ok);
        assert_eq!(response.into_string().unwrap(), "Division operation: 10 / 2 = 5");
    }
}