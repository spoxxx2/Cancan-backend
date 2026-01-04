import { createClient } from "@/lib/supabase-server"

export default async function CleanupsPage() {
  const supabase = createClient()
  const { data: cleanups } = await supabase.from("cleanups").select("*")

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Cleanups</h1>
      <pre className="bg-white p-4 rounded shadow text-sm">
        {JSON.stringify(cleanups, null, 2)}
      </pre>
    </div>
  )
}

