const request = require('supertest');
const express = require('express');
const { app, server } = require('./app');

afterAll(done => {
  server.close(done);
});

describe('GET /', () => {
  it('should respond with a 200 status code', async () => {
    const response = await request(app).get('/');
    expect(response.statusCode).toBe(200);
  });

  it('should respond with html content', async () => {
    const response = await request(app).get('/');
    expect(response.headers['content-type']).toEqual(expect.stringContaining('html'));
  });

  it('should respond with the current Moscow time', async () => {
    const response = await request(app).get('/');
    const moscowTime = new Date().toLocaleString("en-US", { timeZone: "Europe/Moscow" });
    expect(response.text).toContain(moscowTime);
  });
});

describe('GET /nonexistent', () => {
  it('should respond with a 404 status code', async () => {
    const response = await request(app).get('/nonexistent');
    expect(response.statusCode).toBe(404);
  });
});
