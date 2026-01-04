import { cookies } from "next/headers"
import { createServerClient } from "@supabase/ssr"

export function createClient() {
  const cookieStore = cookies()

  return createServerClient(
    {
      cookies: {
        get(name: string) {
          return cookieStore.get(name)?.value
        }
      }
    }
  )
}

