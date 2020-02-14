import React, { useState, useEffect } from "react";
import SessionAdd from "./components/SessionAdd";
import SessionsCompleted from "./components/SessionsCompleted";
import { focusJournalAPI } from "./helpers/focusJournalAPIHelpers";
import "./App.css";

function App() {
  // ===================
  // UI state constants
  // ===================
  const CREATE = "CREATE";
  const LIST = "LIST";
  const [journalMode, setJournalMode] = useState(CREATE);
  //====================

  const [sessions, setSessions] = useState([]);

  useEffect(function() {
    // this fetching might need to be enclosed in an async function for the real API
    (async () => {
      const newSessions = await focusJournalAPI.getSessions();
      setSessions(newSessions);
    })();
  }, []);

  function updateSessions() {
    (async () => {
      const newSessions = await focusJournalAPI.getSessions();
      setSessions(newSessions);
    })();
  }

  function updateSession(updatedSession) {
    // this fetching might need to be enclosed in an async function for the real API
    (async () => {
      await focusJournalAPI.updateSession(updatedSession);
      const newSessions = await focusJournalAPI.getSessions();
      setSessions(newSessions);
    })();
  }

  function deleteSession(sessionId) {
    (async () => {
      const response = await focusJournalAPI.deleteSession(sessionId);
      const newSessions = await focusJournalAPI.getSessions();
      setSessions(newSessions);
      return response;
    })();
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
            deleteSession={deleteSession}
          ></SessionsCompleted>
        </div>
      )}
    </div>
  );
}

export default App;
