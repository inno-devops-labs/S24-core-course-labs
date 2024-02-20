package ru.dmfrpro.app;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

@RestController
public class Controller {
  @GetMapping("/")
  public ModelAndView index() {
    var moscowZone = ZoneId.of("Europe/Samara");
    var currentTime = LocalDateTime.now(moscowZone);
    var formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
    var time = currentTime.format(formatter);
    var modelAndView = new ModelAndView("index");
    modelAndView.addObject("currentTime", time);
    return modelAndView;
  }
}
