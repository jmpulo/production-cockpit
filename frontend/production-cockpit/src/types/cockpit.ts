export interface IMachine {
  id: string;
  name: string;
  reference?: string;
}

export interface IMachineUpdate {
  name?: string;
  reference?: string;
}

export interface IProbeBase {
  name?: string;
  units?: string;
  severity?: "low" | "medium" | "high";
  description?: string;
}

export interface IProbeCreate extends IProbeBase {
  name: string;
  severity: "low" | "medium" | "high";
}

export interface IProbe extends IProbeBase {
  id: string;
  machine_id: string;
}

export interface IMachineProbes extends IMachine {
  probes: IProbe[];
}

export interface IMetricBase {
  probe_name?: string;
  value?: any;
}

export interface IMetricCreate extends IMetricBase {
  probe_name: string;
  value: any;
}

export interface IMetric extends IMetricBase {
  id: string;
}
