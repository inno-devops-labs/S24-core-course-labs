// Purpose: This is the main logic section for the app. It handles the request and response logic.

import { returnTime } from "./utils.js";
import { Registry, Counter } from "prom-client";

// Create a Registry
const registry = new Registry();

registry.setDefaultLabels({
  app: "app_bun",
});

// export function index() {
//   return new Response(returnTime(), {
//     headers: { "content-type": "text/html" },
//   });
// }

// Collect default metrics without using the default function
const counter = new Counter({
  name: "app_bun_counter",
  help: "Example of a counter",
  registers: [registry],
});

export function index() {
  counter.inc();
  return new Response(returnTime(), {
    headers: { "content-type": "text/html" },
  });
}

export async function metrics() {
  return new Response(await registry.metrics(), {
    headers: { "content-type": "text/plain" },
  });
}