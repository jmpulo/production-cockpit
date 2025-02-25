import type { CustomError } from "../types/global";

const checkReqestError = async (response: any) => {
  if (!response.ok) {
    const error = new Error("Error fetching API") as CustomError;
    error.info = await response.json();
    error.status = response.status;
    throw error;
  }
  return null;
};

export { checkReqestError };
