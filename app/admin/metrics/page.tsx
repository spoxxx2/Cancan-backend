import { supabaseServer } from "@/lib/supabase-server";

export default async function MetricsPage() {
  const supabase = supabaseServer();
  const { data: metrics } = await supabase.from("metrics").select("*");

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Metrics</h1>
      <pre className="bg-white p-4 rounded shadow text-sm">
        {JSON.stringify(metrics, null, 2)}
      </pre>
    </div>
  );
}
