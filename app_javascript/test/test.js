// test/test.js

const chai = require('chai');
const chaiHttp = require('chai-http');
const app = require('../app'); 
const expect = chai.expect;

chai.use(chaiHttp);

describe('Todo App', () => {
  it('should display the todo list page', (done) => {
    chai.request(app)
      .get('/')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.text).to.include('<h1>Todo List</h1>');
        done();
      });
  });

it('should add a new todo', (done) => {
  chai.request(app)
    .post('/add')
    .send({ todo: 'Test Todo' })
    .end((err, res) => {
      expect(res).to.have.status(200);
      done();
    });
});
});
