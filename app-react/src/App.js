import React from "react";
import SessionAdd from "./components/SessionAdd";
import SessionsList from "./components/SessionsList";
import "./App.css";

function App() {
  return (
    <div className="App">
      <h1>Practice Journal</h1>
      <SessionAdd></SessionAdd>
      <SessionsList></SessionsList>
    </div>
  );
}

export default App;
