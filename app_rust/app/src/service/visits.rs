use std::fs::OpenOptions;
use std::io::{Read, Seek, SeekFrom, Write};

fn file_mount(path: &String) -> std::io::Result<()> {
    if std::path::Path::new(path).exists() {
        return Ok(());
    }
    let mut file = OpenOptions::new().write(true).create_new(true).open(path)?;

    write!(file, "0")
}

pub struct VisitsFileStorage {
    file_path: String,
}

impl VisitsFileStorage {
    pub fn new(file_path_: String) -> Self {
        let _ = file_mount(&file_path_);
        Self {
            file_path: file_path_.clone(),
        }
    }

    pub fn read_data(&self) -> u64 {
        return std::fs::read_to_string(&self.file_path)
            .unwrap()
            .parse::<u64>()
            .unwrap();
    }

    pub fn increment(&self) -> std::io::Result<()> {
        let mut file = OpenOptions::new()
            .read(true)
            .write(true)
            .open(&self.file_path)?;

        let mut visits_number = String::new();
        file.read_to_string(&mut visits_number)?;

        let old_count: u64 = visits_number.trim().parse().unwrap();
        let new_count = old_count + 1;

        file.seek(SeekFrom::Start(0))?;

        write!(file, "{}", new_count)
    }
}
