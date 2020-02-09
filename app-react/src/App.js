import React, { useState, useEffect } from "react";
import SessionAdd from "./components/SessionAdd";
import SessionsCompleted from "./components/SessionsCompleted";
import { focusJournalAPI } from "./helpers/focusJournalAPIHelpers";
import "./App.css";

function App() {
  const [sessions, setSessions] = useState([]);

  useEffect(function() {
    const newSessions = focusJournalAPI.getSessions();
    setSessions(newSessions);
  }, []);

  function updateSessions() {
    const newSessions = focusJournalAPI.getSessions();
    setSessions(newSessions);
    console.log("added new session", newSessions);
  }

  return (
    <div className="App">
      <h1>Focus Journal</h1>
      <SessionAdd updateSessions={updateSessions}></SessionAdd>
      <SessionsCompleted sessions={sessions}></SessionsCompleted>
    </div>
  );
}

export default App;
