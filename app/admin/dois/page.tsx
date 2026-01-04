import { createClient } from "@/lib/supabase-server"

export default async function DoisPage() {
  const supabase = createClient()
  const { data: dois } = await supabase.from("dois").select("*")

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">DOIs</h1>
      <pre className="bg-white p-4 rounded shadow text-sm">
        {JSON.stringify(dois, null, 2)}
      </pre>
    </div>
  )
}

