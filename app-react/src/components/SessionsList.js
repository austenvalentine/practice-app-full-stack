import React, { useState, useEffect } from "react";
import { practiceAppAPI } from "../helpers/practiceJournalAPIHelpers";

function SessionsList() {
  const [sessions, setSessions] = useState([]);
  useEffect(function() {
    const newSessions = practiceAppAPI.getSessions();
    setSessions(newSessions);
  }, []);
  return (
    <div>
      <ul>
        {sessions
          ? sessions.map(session => (
              <li>{`${new Date(session.created).toDateString()}: ${
                session.focus
              }`}</li>
            ))
          : [null]}
      </ul>
    </div>
  );
}

export default SessionsList;
