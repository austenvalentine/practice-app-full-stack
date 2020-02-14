const focusJournalAPI = {
  createSession: function(session) {
    const newSession = { ...session };
    newSession.id = this.data.length;
    newSession.created = new Date().getTime();
    newSession.modified = newSession.created;
    const newData = [...this.data, newSession];
    this.data = newData;
  },

  updateSession: function(newSession) {
    return new Promise(resolve => {
      const newData = this.data.map(function(session) {
        if (session.id === newSession.id) {
          newSession.created = session.created;
          newSession.modified = new Date().getTime();
          return newSession;
        }
        return session;
      });
      this.data = newData;
      resolve(200);
    });
  },
  getSessions: function() {
    return new Promise(resolve => {
      const dataCopy = this.data.filter(session => session !== null);
      console.log(dataCopy);
      resolve(dataCopy);
    });
  },
  getSession: function(sessionId) {
    return new Promise(resolve => {
      resolve(this.data[sessionId]);
    });
  },
  deleteSession: function(sessionId) {
    return new Promise(resolve => {
      const newData = this.data.map(function(session) {
        if (sessionId === session.id) {
          return null;
        }
        return session;
      });
      console.log("deleted sessions: ", newData);
      this.data = newData;
      resolve(200);
    });
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
