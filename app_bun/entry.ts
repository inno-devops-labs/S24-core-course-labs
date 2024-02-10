// Purpose: Entry point for the Bun server.

import { index } from "./app.ts";

const server = Bun.serve({ fetch: index });
console.log(`Running http://localhost:${server.port}`);
