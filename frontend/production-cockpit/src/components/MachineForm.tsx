import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import { fetchBackend } from "../services/fetchBackend";

interface IProps {
  machineName?: string;
  machineReference?: string;
}

export const MachineForm = ({ machineName, machineReference }: IProps) => {
  const create = async (formData: any) => {
    const name = formData.get("name");
    const reference = formData.get("reference");
    await fetchBackend({
      path: "machine",
      data: { name: name, reference: reference },
      method: "POST",
    });
  };
  return (
    <>
      <form action={create}>
        <TextField size="small" name="name" label="Name" value={machineName} />
        <TextField
          name="reference"
          label="Reference"
          value={machineReference}
        />
        <Button type="submit" variant="contained">
          Create
        </Button>
      </form>
    </>
  );
};
