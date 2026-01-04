import { createClient } from "@/lib/supabase-server"

export default async function LogsPage() {
  const supabase = createClient()
  const { data: logs } = await supabase.from("logs").select("*")

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Logs</h1>
      <pre className="bg-white p-4 rounded shadow text-sm">
        {JSON.stringify(logs, null, 2)}
      </pre>
    </div>
  )
}

