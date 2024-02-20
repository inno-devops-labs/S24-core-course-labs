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
    let regex = /\d{1,2}\/\d{1,2}\/\d{4}, \d{1,2}:\d{2}:\d{2} (AM|PM)/g;
    const receivedTime = response.text.match(regex);
    const moscowTime = new Date().toLocaleString("en-US", { timeZone: "Europe/Moscow" });

    const time1 = new Date(receivedTime[0]);
    const time2 = new Date(moscowTime);

    const diff = Math.abs(time1.getTime() - time2.getTime());

    result = diff < 10000;
    
    expect(result).toBe(true);
  });
});

describe('GET /nonexistent', () => {
  it('should respond with a 404 status code', async () => {
    const response = await request(app).get('/nonexistent');
    expect(response.statusCode).toBe(404);
  });
});
