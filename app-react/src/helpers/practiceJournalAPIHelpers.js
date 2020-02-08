const practiceAppAPI = {
  createSession: function(session) {
    const newSession = { ...session };
    newSession.created = new Date().getTime();
    newSession.modified = newSession.created;
    this.data.push(newSession);
    console.log("data:", this.data);
  },
  getSessions: function() {
    return this.data;
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
practiceAppAPI.init();
export { practiceAppAPI };
