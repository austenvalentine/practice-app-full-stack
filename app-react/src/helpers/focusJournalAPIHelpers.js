const focusJournalAPI = {
  createSession: function(session) {
    const newSession = { ...session };
    newSession.created = new Date().getTime();
    newSession.modified = newSession.created;
    this.data.push(newSession);
  },
  getSessions: function() {
    return this.data.reverse();
  },
  getSession: function(sessionId) {
    return this.data[sessionId];
  },
  init: function() {
    const dummyData = [
      {
        focus: "Play Stairway slowly",
        win: "played really slowly",
        challenge: "could've been slower",
        nextStep: "use the metronome"
      },
      {
        focus: "swinging",
        win: "swung",
        challenge: "meaning a thing",
        nextStep: "swing harder"
      }
    ];
    dummyData.forEach(session => this.createSession(session));
  },
  data: []
};
focusJournalAPI.init();
export { focusJournalAPI };
