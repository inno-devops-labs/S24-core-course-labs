package ru.innopolis.demo.controller

import org.springframework.web.bind.annotation.RestController
import org.springframework.web.bind.annotation.GetMapping
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import java.time.ZoneId
import java.time.LocalTime

@RestController
class TimeController {

    @GetMapping
    fun getCurrentTime() :String {
        return "Current time in Moscow " + LocalTime.now(ZoneId.of("Europe/Moscow")).format(DateTimeFormatter.ofPattern("HH:mm:SS"))
    }
}