import React, { useState, useEffect } from "react";
import SessionAdd from "./components/SessionAdd";
import SessionsCompleted from "./components/SessionsCompleted";
import { focusJournalAPI } from "./helpers/focusJournalAPIHelpers";
import "./App.css";

function App() {
  const CREATE = "CREATE";
  const LIST = "LIST";
  const [sessions, setSessions] = useState([]);
  const [journalMode, setJournalMode] = useState(CREATE);

  useEffect(function() {
    const newSessions = focusJournalAPI.getSessions();
    setSessions(newSessions);
  }, []);

  function updateSessions() {
    const newSessions = focusJournalAPI.getSessions();
    setSessions(newSessions);
  }

  function updateSession(updatedSession, sessionId) {
    console.log(updatedSession);
  }

  return (
    <div className="App">
      <h1>Focus Journal</h1>
      {journalMode === CREATE && (
        <div>
          <button onClick={() => setJournalMode(LIST)}>
            View Completed Journals
          </button>
          <SessionAdd updateSessions={updateSessions}></SessionAdd>
        </div>
      )}
      {journalMode === LIST && (
        <div>
          <button onClick={() => setJournalMode(CREATE)}>
            Log a New Session
          </button>
          <SessionsCompleted
            sessions={sessions}
            updateSession={updateSession}
          ></SessionsCompleted>
        </div>
      )}
    </div>
  );
}

export default App;
