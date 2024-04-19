package ru.dmfrpro.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.PrintWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.File;

@SpringBootApplication
public class Application {
  private static final String VISITS_FILE = "app/data/visits.txt";

  public static void main(String[] args) {
    createVisits();
    SpringApplication.run(Application.class, args);
  }

  private static void createVisits() {
    var file = new File(VISITS_FILE);

    if (file.exists()) {
      return;
    }

    try {
      file.getParentFile().mkdirs();
      file.createNewFile();
    } catch (IOException e) {
      e.printStackTrace();
    }

    try (var writer = new PrintWriter(new FileWriter(file))) {
      writer.println("0");
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
