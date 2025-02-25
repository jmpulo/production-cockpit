import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import { useState } from "react";
import { fetchBackend } from "../services/fetchBackend";

interface IProps {
  machineName?: string;
  machineReference?: string;
}

export const MachineForm = ({
  machineName = "",
  machineReference = "",
}: IProps) => {
  const [name, setName] = useState(machineName);
  const [reference, setReference] = useState(machineReference);

  const handleClick = async () => {
    await fetchBackend({
      path: "machine",
      data: { name: name, reference: reference },
      method: "POST",
    });
  };
  return (
    <>
      <TextField
        label="Name"
        value={name}
        onChange={(v) => setName(v.target.value)}
      />
      <TextField
        label="Reference"
        onChange={(v) => setReference(v.target.value)}
      />
      <Button onClick={handleClick} variant="outlined">
        Create
      </Button>
    </>
  );
};
