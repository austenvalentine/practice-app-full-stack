import React from "react";

function SessionDetail(props) {
  const { session, closeSession } = props;

  return (
    <div>
      <h3>Session: {new Date().toDateString()}</h3>
      <h4>{`Focus: ${session.focus}`}</h4>
      <p>{`Win: ${session.win}`}</p>
      <p>{`Challenge: ${session.challenge}`}</p>
      <p>{`Next Step: ${session.nextStep}`}</p>
      <button onClick={closeSession}>Close</button>
    </div>
  );
}

export default SessionDetail;
