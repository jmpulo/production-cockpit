import { fetchBackend } from "../services/fetchBackend";
import type {
  IMachine,
  IMachineProbes,
  IMachineUpdate,
  IMetric,
  IMetricCreate,
  IProbe,
  IProbeCreate,
} from "../types/cockpit";

const machineGetAll = (): Promise<IMachine[]> => {
  return fetchBackend({ path: "machine" });
};

const machineCreate = (machine: IMachine): Promise<IMachine> => {
  return fetchBackend({ path: "machine", method: "POST", data: machine });
};
const machineGetOne = (id: string): Promise<IMachine> => {
  return fetchBackend({ path: `machine/${id}` });
};
const machineUpdate = (
  machineId: string,
  machine: IMachineUpdate
): Promise<IMachine> => {
  return fetchBackend({
    path: `machine/${machineId}`,
    method: "PUT",
    data: machine,
  });
};

const machineDelete = (id: string): Promise<IMachine> => {
  return fetchBackend({ path: `machine/${id}`, method: "DELETE" });
};

const machineProbeAdd = (
  machineId: string,
  probe: IProbeCreate
): Promise<IProbe> => {
  return fetchBackend({
    path: `machine/${machineId}/probe`,
    method: "PATCH",
    data: probe,
  });
};

const machineProbesGet = (machineId: string): Promise<IMachineProbes> => {
  return fetchBackend({ path: `machine/${machineId}/probe` });
};

const machineMetricAdd = (
  machineId: string,
  metric: IMetricCreate
): Promise<IMetric> => {
  return fetchBackend({
    path: `machine/${machineId}/metric`,
    method: "PATCH",
    data: metric,
  });
};

export {
  machineCreate,
  machineDelete,
  machineGetAll,
  machineGetOne,
  machineMetricAdd,
  machineProbeAdd,
  machineProbesGet,
  machineUpdate,
};
