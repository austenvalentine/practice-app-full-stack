import React, { useState, useEffect } from "react";

function SessionsList(props) {
  const { showSession } = props;
  const [sessions, setSessions] = useState(props.sessions);

  useEffect(() => {
    if (sessions !== props.sessions) {
      setSessions(props.sessions);
    }
  }, [sessions, props.sessions]);

  return (
    <div className={sessions.length}>
      <h2>Completed Sessions</h2>
      <ul>
        {sessions &&
          [...sessions].reverse().map((session, index) => (
            <li key={index}>
              <button onClick={e => showSession(e, session.id)}>{`${new Date(
                session.created
              ).toDateString()}: ${session.focus}`}</button>
            </li>
          ))}
      </ul>
    </div>
  );
}

export default SessionsList;
