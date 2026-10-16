import axios, { type AxiosInstance } from 'axios'
import { z } from 'zod'

export const apiClient: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '/api',
  headers: {
    'Content-Type': 'application/json'
  },
  timeout: 10000
})

/**
 * Executes a GET request and validates the response payload with a Zod schema.
 */
export async function getValidated<T>(url: string, schema: z.ZodType<T>): Promise<T> {
  const response = await apiClient.get(url)
  return schema.parse(response.data)
}
