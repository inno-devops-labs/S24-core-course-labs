import "./App.css";

function App() {
  const date = new Date().toLocaleTimeString("ru-RU", {
    timeZone: "Europe/Moscow",
  });
  return (
    <div className="App">
      <div className="card">
        <h1>Current time in Moscow</h1>
        <h2>{date}</h2>
      </div>
    </div>
  );
}

export default App;
