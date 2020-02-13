const focusJournalAPI = {
  createSession: function(session) {
    const newSession = { ...session };
    newSession.id = this.data.length;
    newSession.created = new Date().getTime();
    newSession.modified = newSession.created;
    const newData = [...this.data, newSession];
    this.data = newData;
  },
  getSessions: function() {
    const dataCopy = [...this.data];
    return dataCopy;
  },
  getSession: function(sessionId) {
    return this.data[sessionId];
  },
  init: function() {
    const dummyData = [
      {
        focus: "Play Stairway slowly",
        win: "played slowly",
        challenge: "could've been slower",
        nextStep: "slow down"
      },
      {
        focus: "swinging",
        win: "swung",
        challenge: "meaning a thing",
        nextStep: "swing harder"
      },
      {
        focus: "shredding",
        win: "shredded",
        challenge: "shredding too slowly",
        nextStep: "shred faster"
      }
    ];
    dummyData.forEach(session => this.createSession(session));
  },
  data: []
};
focusJournalAPI.init();
export { focusJournalAPI };
