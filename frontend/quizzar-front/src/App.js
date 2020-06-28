import React from "react";
import AppHeader from "./AppHeader";
import TestList from "./TestList";
import "./styles.css";

const App = () => {
  return (
    <div>
      <div>
        <AppHeader />
      </div>
      <div>
        <TestList />
      </div>
    </div>
  );
};

export default App;
