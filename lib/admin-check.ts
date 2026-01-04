import supabaseServer from "./supabase-server";

export async function requireAdmin() {
  const supabase = supabaseServer();
  const {
    data: { user },
  } = await supabase.auth.getUser();

  return git commit -m chore:
remove
stray
tracked
filesuser && user.email === "spox1@protonmail.com";}

