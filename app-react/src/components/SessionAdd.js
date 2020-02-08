import React, { useState } from "react";
import { practiceAppAPI } from "../helpers/practiceJournalAPIHelpers";

function SessionAdd() {
  const [focus, setFocus] = useState("");
  const [win, setWin] = useState("");
  const [challenge, setChallenge] = useState("");
  const [nextStep, setNextStep] = useState("");

  function clearForm() {
    setFocus("");
    setWin("");
    setChallenge("");
    setNextStep("");
  }

  function handleClick(e) {
    e.preventDefault();
    practiceAppAPI.createSession({ focus, win, challenge, nextStep });
    clearForm();
  }

  return (
    <div className="App">
      <h2>Log Session</h2>
      <form>
        <label htmlFor="focus">Focus: </label>
        <input
          id="focus"
          type="text"
          value={focus}
          onChange={e => setFocus(e.target.value)}
        ></input>
        <label htmlFor="win">Win: </label>
        <input
          id="win"
          type="text"
          value={win}
          onChange={e => setWin(e.target.value)}
        ></input>
        <label htmlFor="challenge">Challenge: </label>
        <input
          id="challenge"
          type="text"
          value={challenge}
          onChange={e => setChallenge(e.target.value)}
        ></input>
        <label htmlFor="nextStep">Next Step: </label>
        <input
          id="nextStep"
          type="text"
          value={nextStep}
          onChange={e => setNextStep(e.target.value)}
        ></input>
        <button onClick={handleClick}>Save Session</button>
      </form>
    </div>
  );
}

export default SessionAdd;
