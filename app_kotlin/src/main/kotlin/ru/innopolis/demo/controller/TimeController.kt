package ru.innopolis.demo.controller

import org.springframework.web.bind.annotation.RestController
import org.springframework.web.bind.annotation.GetMapping
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import java.time.ZoneId
import java.time.LocalTime
import java.io.File
import java.util.concurrent.atomic.AtomicInteger

@RestController
class TimeController {
    private var visits = AtomicInteger(0)
    private val visit_path = "data/visits"
    
    private fun saveVisits() {
        if (!File("data").exists()) {
            File("data").mkdir()
        }
        File(visit_path).writeText(visits.toString())
    }

    fun incVisits() {
        visits.addAndGet(1)
        saveVisits()
    }

    @GetMapping
    fun getCurrentTime() :String {
        incVisits()
        return "Current time in Moscow " + LocalTime.now(ZoneId.of("Europe/Moscow")).format(DateTimeFormatter.ofPattern("HH:mm:SS"))
    }
    
    @GetMapping("/visits")
    fun getVisits() :String {
        incVisits()
        return "{visits: ${visits.get()}}"
    }
}
