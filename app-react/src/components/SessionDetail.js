import React, { useState } from "react";

function SessionDetail(props) {
  // detail modes are READ, EDIT and DELETE
  const READ = "READ";
  const EDIT = "EDIT";
  const DELETE = "DELETE";
  const [detailMode, setDetailMode] = useState(READ);
  const { session, closeSession, updateSession /*, deleteSession */ } = props;
  const [newFocus, setNewFocus] = useState(session?.focus);
  const [newWin, setNewWin] = useState(session?.win);
  const [newChallenge, setNewChallenge] = useState(session?.challenge);
  const [newNextStep, setNewNextStep] = useState(session?.nextStep);

  function handleUpdateClick() {
    const newSession = {
      // will this store stale values? Might need to pass values in
      focus: newFocus,
      win: newWin,
      challenge: newChallenge,
      nextStep: newNextStep
    };
    updateSession(newSession, session.id);
  }

  return (
    <div>
      <h3>Session: {new Date().toDateString()}</h3>
      {detailMode === READ && (
        <div className="readMode">
          <h4>Focus: {session.focus}</h4>
          <p>Win: {session.win}</p>
          <p>Challenge: {session.challenge}</p>
          <p>Next Step: {session.nextStep}</p>
          <button onClick={closeSession}>Close</button>
          <button onClick={() => setDetailMode(EDIT)}>Edit</button>
          <button onClick={() => setDetailMode(DELETE)}>Delete</button>
        </div>
      )}
      {detailMode === EDIT && (
        <div className="editMode">
          <label htmlFor="focus">Focus: </label>
          <input
            id="focus"
            type="text"
            defaultValue={newFocus}
            onChange={e => setNewFocus(e.target.value)}
          ></input>
          <label htmlFor="win">Win: </label>
          <input
            id="win"
            type="text"
            defaultValue={newWin}
            onChange={e => setNewWin(e.target.value)}
          ></input>
          <label htmlFor="challenge">Challenge: </label>
          <input
            id="challenge"
            type="text"
            defaultValue={newChallenge}
            onChange={e => setNewChallenge(e.target.value)}
          ></input>
          <label htmlFor="nextStep">Next Step: </label>
          <input
            id="nextStep"
            type="text"
            defaultValue={newNextStep}
            onChange={e => setNewNextStep(e.target.value)}
          ></input>
          <button onClick={() => setDetailMode(READ)}>Cancel</button>
          <button>Save Changes</button>
        </div>
      )}
      {detailMode === "DELETE" && (
        <div htmlClass="deleteMode">
          <div htmlClass="warningBox">
            <h2>Do you want to delete this session?</h2>
          </div>
          <button onClick={() => setDetailMode(READ)}>No</button>
          <button onClick={handleUpdateClick}>Yes</button>
        </div>
      )}
    </div>
  );
}

export default SessionDetail;
