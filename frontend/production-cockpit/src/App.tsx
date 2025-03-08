import { Drawer, ListItemButton } from "@mui/material";
import "./App.css";
import { MachineForm } from "./components/MachineForm";

function App() {
  return (
    <>
      <Drawer variant="permanent">
        <ListItemButton>Test</ListItemButton>
      </Drawer>
      <MachineForm />
    </>
  );
}

export default App;
