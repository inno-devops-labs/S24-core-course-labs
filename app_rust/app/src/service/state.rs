use std::sync::Mutex;

pub struct AppState {
    pub counter: Mutex<i32>, // <- Mutex is necessary to mutate safely across threads
}