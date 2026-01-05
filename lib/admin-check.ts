import supabaseServer from "./supabase-server";

export async function requireAdmin() {
  const supabase = supabaseServer();
  const {
    data: { user },
  } = await supabase.auth.getUser();

  return !!user && user.email === "spoxxx2@gmail.com";
}
