import { createClient } from "@/lib/supabase-server"

export default async function EventsPage() {
  const supabase = createClient()
  const { data: events } = await supabase.from("events").select("*")

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Events</h1>
      <pre className="bg-white p-4 rounded shadow text-sm">
        {JSON.stringify(events, null, 2)}
      </pre>
    </div>
  )
}

