package org.devops.devops_java.web.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import java.io.*;
import java.time.OffsetDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

@Controller
public class TimeController {
    private static final String VISITS_FILE_PATH = "/app/vol/visits";

    private int logVisits() {
        try {
            new File(VISITS_FILE_PATH).createNewFile();
            var bf = new BufferedReader(new FileReader(VISITS_FILE_PATH));
            String s = bf.readLine();
            if (s.isEmpty()) {
                s = "0";
            }
            int visits = Integer.parseInt(s) + 1;
            bf.close();
            var pw = new PrintWriter(VISITS_FILE_PATH);
            pw.print(visits);
            pw.close();
            return visits;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @GetMapping("/")
    public ResponseEntity<String> index() {
        logVisits();
        var mosTime = OffsetDateTime.now(ZoneId.of("Europe/Moscow"));
        return ResponseEntity.ok(DateTimeFormatter.ISO_ZONED_DATE_TIME.format(mosTime));
    }

    @GetMapping("/visits")
    public ResponseEntity<Integer> visits() {
        return ResponseEntity.ok(logVisits());
    }
}
