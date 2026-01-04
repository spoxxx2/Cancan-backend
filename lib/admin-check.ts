import { supabaseServer } from "./supabase-server";

export async function requireAdmin() {
  const supabase = supabaseServer();
  const { data: { user } } = await supabase.auth.getUser();

  if (!user || user.user_metadata.role !== "admin") {
    return false;
  }

  return true;
}