import { createClient } from "@/lib/supabase-server"

export default async function VolunteersPage() {
  const supabase = createClient()
  const { data: volunteers } = await supabase.from("volunteers").select("*")

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Volunteers</h1>
      <pre className="bg-white p-4 rounded shadow text-sm">
        {JSON.stringify(volunteers, null, 2)}
      </pre>
    </div>
  )
}

