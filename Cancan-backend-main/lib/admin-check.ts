import { createClient } from "./supabase-server";

export async function requireAdmin() {
  const supabase = createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();

  return !!user && user.email === "spoxxx2@gmail.com";
}
