import { createClient } from "@/lib/supabase-server"

export default async function DailyReportsPage() {
  const supabase = createClient()
  const { data: reports } = await supabase.from("daily_reports").select("*")

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Daily Reports</h1>
      <pre className="bg-white p-4 rounded shadow text-sm">
        {JSON.stringify(reports, null, 2)}
      </pre>
    </div>
  )
}

