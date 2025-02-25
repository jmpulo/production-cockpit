import { useState } from "react";
import { MachineForm } from "./components/MachineForm";

import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <MachineForm />
    </>
  );
}

export default App;
