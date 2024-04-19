package ru.dmfrpro.app;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

import java.util.HashMap;

import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

@RestController
public class Controller {
  private static final String VISITS_FILE = "app/data/visits.txt";

  @GetMapping("/")
  public ModelAndView index() {
    int res = 0;

    try (var reader = new BufferedReader(new FileReader(VISITS_FILE))) {
      res = Integer.parseInt(reader.readLine());
    } catch (IOException e) {
      e.printStackTrace();
    }

    try (var writer = new PrintWriter(new FileWriter(VISITS_FILE))) {
      writer.println(String.valueOf(res + 1));
    } catch (IOException e) {
      e.printStackTrace();
    }

    var moscowZone = ZoneId.of("Europe/Samara");
    var currentTime = LocalDateTime.now(moscowZone);
    var formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
    var time = currentTime.format(formatter);
    var modelAndView = new ModelAndView("index");
    modelAndView.addObject("currentTime", time);
    return modelAndView;
  }

  @GetMapping("/visits")
  public Object visits() {
    int res = 0;

    try (var reader = new BufferedReader(new FileReader(VISITS_FILE))) {
      res = Integer.parseInt(reader.readLine());
    } catch (IOException e) {
      e.printStackTrace();
    }

    var map = new HashMap<String, Integer>();
    map.put("visits", res);
    return new ResponseEntity<>(map, HttpStatus.OK);
  }
}
