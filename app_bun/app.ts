// Purpose: This is the main logic section for the app. It handles the request and response logic.

import { returnTime, incrementVisits, returnVisitCounts } from "./utils.js";
import { Registry, Counter, Histogram } from "prom-client";

// Create a Registry
const registry = new Registry();

registry.setDefaultLabels({
  app: "app_bun",
});

// Collect default metrics without using the default function
const counter = new Counter({
  name: "api_http_requests_total",
  help: "Number of http requests made",
  registers: [registry],
});

const histogram = new Histogram({
  name: "api_http_request_duration_seconds",
  help: "Duration of http requests in seconds",
  registers: [registry],
});

export function index() {
  counter.inc();
  incrementVisits();
  const end = histogram.startTimer();
  // get timezone from the environment variable
  const timezone = process.env.APP_TIMEZONE || "Europe/Moscow";
  const response = returnTime(timezone);
  end();
  return new Response(response, {
    headers: { "content-type": "text/html" },
  });
}

export async function visits() {
  return new Response(await returnVisitCounts(), {
    headers: { "content-type": "text/html" },
  });
}

export async function metrics() {
  return new Response(await registry.metrics(), {
    headers: { "content-type": "text/plain" },
  });
}
