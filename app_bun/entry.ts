// Purpose: Entry point for the Bun server.

import { index, metrics, visits } from "./app.ts";
// use prom-client to expose metrics

const server = Bun.serve({
    fetch(req) {
        const url = new URL(req.url);
        if (url.pathname === "/metrics") {
            return metrics();
        }
        if (url.pathname === "/visits") {
            return visits();
        }
        return index();
    }
})
console.log(`Running http://localhost:${server.port}`);
