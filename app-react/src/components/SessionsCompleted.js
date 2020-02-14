import React, { useState } from "react";
import { focusJournalAPI } from "../helpers/focusJournalAPIHelpers";
import SessionsList from "./SessionsList";
import SessionDetail from "./SessionDetail";

function SessionsCompleted({ sessions, updateSession, deleteSession }) {
  const [session, setSession] = useState(null);

  function showSession(e, sessionId) {
    (async () => {
      const pickSession = await focusJournalAPI.getSession(sessionId);
      setSession(pickSession);
    })();
  }

  function closeSession(e) {
    if (session !== null) {
      setSession(null);
    }
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
          deleteSession={deleteSession}
        ></SessionDetail>
      )}
    </div>
  );
}

export default SessionsCompleted;
