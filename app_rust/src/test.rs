use crate::{plus, minus, multiply, divide};

#[test]
fn test_mathematical_expressions() {
    assert!(plus(1, 2).contains("3"));
    assert!(minus(8, 2).contains("6"));
    assert!(multiply(3, 3).contains("9"));
    assert!(divide(10, 2).contains("5"));
    assert!(divide(5, 0).contains("Error"));
}