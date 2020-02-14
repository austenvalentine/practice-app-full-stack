import React, { useState } from "react";
import { focusJournalAPI } from "../helpers/focusJournalAPIHelpers";

function SessionDetail(props) {
  // ==================
  // UI state constants
  // ==================
  // detail modes are READ, EDIT and DELETE
  const READ = "READ";
  const EDIT = "EDIT";
  const DELETE = "DELETE";
  const [detailMode, setDetailMode] = useState(READ);

  const { closeSession, updateSession, deleteSession } = props;
  const [session, setSession] = useState(props.session);
  const [newFocus, setNewFocus] = useState(session && session.focus);
  const [newWin, setNewWin] = useState(session && session.win);
  const [newChallenge, setNewChallenge] = useState(session?.challenge);
  const [newNextStep, setNewNextStep] = useState(session && session.nextStep);

  function handleClickSave() {
    const newSession = {
      // will this assign stale values? Might need to pass values in
      id: session.id,
      focus: newFocus,
      win: newWin,
      challenge: newChallenge,
      nextStep: newNextStep
    };
    (async () => {
      await updateSession(newSession);
      setSession(await focusJournalAPI.getSession(newSession.id));
      setDetailMode(READ);
    })();
  }

  function handleClickDelete() {
    (async () => {
      await deleteSession(session.id);
      closeSession();
    })();
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
          <button onClick={handleClickSave}>Save Changes</button>
        </div>
      )}
      {detailMode === DELETE && (
        <div className="deleteMode">
          <div className="warningBox">
            <h2>Do you want to delete this session?</h2>
          </div>
          <button onClick={() => setDetailMode(READ)}>No</button>
          <button onClick={handleClickDelete}>Yes</button>
        </div>
      )}
    </div>
  );
}

export default SessionDetail;
