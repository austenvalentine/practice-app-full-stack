import React, { useState } from "react";
import { focusJournalAPI } from "../helpers/focusJournalAPIHelpers";
import SessionsList from "./SessionsList";
import SessionDetail from "./SessionDetail";

function SessionsCompleted({ sessions, updateSession }) {
  const [session, setSession] = useState(null);

  function showSession(e, sessionId) {
    e.preventDefault();
    const pickSession = focusJournalAPI.getSession(sessionId);
    setSession(pickSession);
  }

  function closeSession(e) {
    e.preventDefault();
    setSession(null);
  }

  return (
    <div>
      {session == null && (
        <SessionsList
          sessions={sessions}
          showSession={showSession}
        ></SessionsList>
      )}
      {session && (
        <SessionDetail
          closeSession={closeSession}
          session={session}
          updateSession={updateSession}
        ></SessionDetail>
      )}
    </div>
  );
}

export default SessionsCompleted;
