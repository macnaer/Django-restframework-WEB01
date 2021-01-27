import React, { Component } from 'react';

class App extends Component {

  render() {
    return (
     <h2>Hello work</h2>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);