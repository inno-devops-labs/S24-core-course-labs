package org.devops.devops_java.web.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import java.time.OffsetDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

@Controller
public class TimeController {
    @GetMapping("/")
    public ResponseEntity<String> index() {
        var mosTime = OffsetDateTime.now(ZoneId.of("Europe/Moscow"));;
        return ResponseEntity.ok(DateTimeFormatter.ISO_ZONED_DATE_TIME.format(mosTime));
    }
}
