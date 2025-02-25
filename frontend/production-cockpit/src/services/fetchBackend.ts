import { checkReqestError } from "../helpers/utils";
import type { IndexSignature } from "../types/global";

interface IfetchBackend {
  path: string;
  method?: string;
  data?: any;
  headers?: IndexSignature;
  checkError?: boolean;
}

export const fetchBackend = async ({
  path,
  method,
  data,
  headers,
  checkError,
}: IfetchBackend) => {
  const res = await fetch(`http://localhost:8000/api/v1/${path}`, {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      ...headers,
    },
    method: method ?? "GET",
    body: data ? JSON.stringify(data) : null,
  });
  if (checkError) {
    const error = await checkReqestError(res);
    if (error) {
      throw error;
    }
  }
  return res.status === 204 ? {} : res.json();
};
